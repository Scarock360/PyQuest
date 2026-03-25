import sys,inspect
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from utils import utils
from utils.utils import GREEN,YELLOW,ENDC,RED,BRIGHT_GREEN, MAGENTA
from game_state import AbstractGameState
from maps.abstract_level import abstract_level
from _map_state_object import MapObject
import maps


class MapState(AbstractGameState):

    levels = {}
    previously_visited ={}
    current_level = None

    map_colour=YELLOW
    player_colour=BRIGHT_GREEN
    no_colour=ENDC

    u_c = "⮝ "
    r_c = "⮞ "
    l_c = "⮜ "
    d_c = "⮟ "
    player_icon = u_c

    menu_options = [
        "Interact",
        "Skills",
        "Items",
        "Equipment",
        "Level up",
        "Rest",
    ]

    @classmethod
    def setup(cls,game):
        cls.GAME = game
        for name, obj in inspect.getmembers(maps):
            if f"{type(obj)}" == "<class 'module'>":
                level = getattr(obj,name)
                if issubclass(level.__class__,abstract_level.__class__):
                    cls.levels[name] = getattr(obj,name)
        cls.levels.pop("abstract_level")

    @classmethod
    def load_level_from_file(cls, level, start_location_override = None):
        if level not in cls.previously_visited:
            cls.previously_visited[level] = MapObject(cls,level,start_location_override)
        cls.current_level = cls.previously_visited[level].update_location(start_location_override)

    @classmethod
    def handle_menu_event(cls, event):
        match event:
            case "Interact":
                cls.interact()
            case "Skills":
                cls.GAME.dialog_box = f"You have no abilities\n    {RED}Skill issue{ENDC}"
            case "Items":
                if len(cls.GAME.inventory.keys()) > 0:
                    cls.GAME.states["inventory"].pre_shift("map")
                    cls.GAME.change_state("inventory")
                else:
                    cls.GAME.dialog_box = "Your bag is empty.\n"
            case "Equipment":
                cls.GAME.states["equipment"].pre_shift("map")
                cls.GAME.change_state("equipment")
            case "Level up":
                cls.GAME.states["equipment"].pre_shift("map")
                cls.GAME.change_state("equipment")
                cls.GAME.states["status"].pre_shift(cls.GAME.party["hero"],"map")
                cls.GAME.change_state("status")
            case "Rest":
                cls.GAME.dialog_box = cls.Rest()
            case _:
                cls.GAME.dialog_box = f"{event} clicked\n"

    @classmethod
    def interact(cls):
        x = cls.current_level.player_coords["x"]
        y = cls.current_level.player_coords["y"]
        match cls.player_icon:
            case cls.u_c:
                y-=1
            case cls.r_c:
                x+=2
            case cls.l_c:
                x-=2
            case cls.d_c:
                y+=1
        split_map = cls.current_level._MAP.split('\n')

        special_interaction = cls.current_level.interaction_register.get(y,{}).get(x,None)
        if special_interaction is not None:
            cls.handle_custom_interaction(special_interaction)
        else:
            treasure_interaction = cls.current_level.treasure_register.get(y,{}).get(x,None)
            if treasure_interaction is not None:
                cls.handle_treasure_interaction(treasure_interaction)
            else:
                tile = f"{split_map[y][x:x+2]}"
                cls.GAME.dialog_box = cls.current_level.default_interactions.get(tile,f"What are you looking at\n{tile}")

    @classmethod
    def handle_custom_interaction(cls, interaction):
        for event in interaction["events"]:
            if "msg" in event:
                cls.GAME.dialog_box = event["msg"]
            if "replace_all" in event:
                cls.current_level._MAP = cls.current_level._MAP.replace(event["replace_all"]["replace"],event["replace_all"]["with"])
            if "change_level" in event:
                cls.load_level_from_file(
                    event["change_level"]["level"],
                    event["change_level"]["location"]
                )
        if interaction["one_time"]:
            cls.current_level.interaction_register[interaction["location"]["y"]].pop(interaction["location"]["x"])
        cls.generate_display()

    @classmethod
    def handle_treasure_interaction(cls, interaction):
        for item in interaction["items"]:
            cls.GAME.add_item(item["item"], item["quantity"])
        cls.GAME.dialog_box = "You found " + "\nand ".join([
            f"{'a' if i['quantity'] == 1 else i['quantity']} {MAGENTA}{i['item']}{'' if i['quantity'] == 1 else 's'}{ENDC}"
            for i in interaction["items"]]) + "."
        
        if len(cls.GAME.dialog_box.split("\n")) == 1:
            cls.GAME.dialog_box += "\n"
        cls.current_level.treasure_register[interaction["location"]["y"]].pop(interaction["location"]["x"])

    @classmethod
    def Skills(cls):
        pass

    @classmethod
    def Items(cls):
        pass

    @classmethod
    def Rest(cls):
        x = cls.current_level.player_coords["x"]
        y = cls.current_level.player_coords["y"]
        split_map = cls.current_level._MAP.split('\n')
        for ax,ay in [(0,0),(-2,0),(2,0),(0,1),(0,-1)]:
            if split_map[y+ay][x+ax:x+ax+2] == "▒▒":
                for _,c in cls.GAME.party.items():
                    c.hit_points = c.max_hit_points
                cls.GAME.update_health_bars()
                for y,e in cls.current_level.enemy_register.items():
                    for x,_ in e.items():
                        split_map[y] = split_map[y][:x]+"𝍑 "+split_map[y][x+2:]
                cls.current_level._MAP = "\n".join(split_map)
                cls.generate_display()
                return f"You feel {GREEN}rested{ENDC} but so do your {RED}foes{ENDC}\n"
        return "This is not a safe place.\n"

    @classmethod
    def handle_inputs(cls, key):
        match f"{key}":
            case "'w'":
                cls._up()
            case "'d'":
                cls._right()
            case "'a'":
                cls._left()
            case "'s'":
                cls._down()
            case _:
                return
        foe_check = cls._check_ajacency("𝍑 ")
        location_check = cls.current_level.location_trigger_register.get(
            cls.current_level.player_coords["y"],{}).get(cls.current_level.player_coords["x"],None)
        if foe_check:
            cls.GAME.states["battle"].load_battle(cls.current_level.enemy_register[foe_check[0]][foe_check[1]])
            cls.GAME.change_state("battle")
            cls.current_combat = foe_check
        elif location_check is not None:
            cls.handle_custom_interaction(location_check)

    @classmethod
    def resolve_combat(cls, exp):
        split_map = cls.current_level._MAP.split("\n")
        y,x = cls.current_combat
        boss = cls.current_level.enemy_register[y][x][0].get("boss_name",False)# isinstance(cls.current_level.enemy_register[y][x][0],dict)
        split_map[y] = split_map[y][:x]+"🕱🕱"+split_map[y][x+2:]
        cls.current_level._MAP = "\n".join(split_map)
        if boss:
            cls.current_level.enemy_register[y].pop(x)
        for k,c in cls.GAME.party.items():
            c.cooldown_skills = {k:0 for k,_ in c.cooldown_skills.items()}
        cls.GAME.dialog_box = f"You won, earning yourself {GREEN}{exp}{ENDC} exp"
        cls.GAME.party["hero"].gain_exp(exp)

    @classmethod
    def _check_valid(cls,y,x):
        return not cls.current_level._MAP.split("\n")[y][x] in cls.current_level.solid_chars

    @classmethod
    def _check_ajacency(cls,char_to_check):
        x = cls.current_level.player_coords["x"]
        y = cls.current_level.player_coords["y"]
        split_map = cls.current_level._MAP.split('\n')
        for ax,ay in [(0,0),(-2,0),(2,0),(0,1),(0,-1)]:
            if split_map[y+ay][x+ax:x+ax+2] == char_to_check:
                return (y+ay,x+ax)
        return False

    @classmethod
    def _up(cls):
        cls.player_icon = cls.u_c
        if cls._check_valid(cls.current_level.player_coords["y"]-1,cls.current_level.player_coords["x"]):
            cls.current_level.player_coords["y"] -= 1
        return cls.generate_display()

    @classmethod
    def _down(cls):
        cls.player_icon = cls.d_c
        if cls._check_valid(cls.current_level.player_coords["y"]+1,cls.current_level.player_coords["x"]):
            cls.current_level.player_coords["y"] += 1
        return cls.generate_display()

    @classmethod
    def _left(cls):
        cls.player_icon = cls.l_c
        if cls._check_valid(cls.current_level.player_coords["y"],cls.current_level.player_coords["x"]-2):
            cls.current_level.player_coords["x"] -= 2
        return cls.generate_display()

    @classmethod
    def _right(cls):
        cls.player_icon = cls.r_c
        if cls._check_valid(cls.current_level.player_coords["y"],cls.current_level.player_coords["x"]+2):
            cls.current_level.player_coords["x"] += 2
        return cls.generate_display()

    @classmethod
    def generate_display(cls):
        map_by_lines=cls.current_level._MAP.split("\n")

        width = 60
        height = 11

        center_x = 30
        center_y = 5

        left = cls.current_level.player_coords["x"] - center_x
        top = cls.current_level.player_coords["y"] - center_y

        lines = []
        for line in list(range(height)):
            y = line + top
            lines.append("")
            if y < 0 or y >= len(map_by_lines):
                continue
            else:
                if left < 0:
                    lines[-1] += " "*(-left)
                    x = 0
                else:
                    x = left
                lines[-1] += map_by_lines[y][x:]
                lines[-1] = lines[-1][:width]

        lines[center_y] = lines[center_y][:center_x]+\
                        f"{cls.player_colour}{cls.player_icon}{cls.map_colour}"+\
                        lines[center_y][center_x+2:]

        view = "\n".join([f"{cls.map_colour}{x}{cls.no_colour}" for x in lines])

        for char, colour in cls.current_level.char_colours.items():
            view = view.replace(char, f"{colour}{char}{cls.map_colour}")

        for escaped_tile, replacement in cls.current_level.escaped_tiles.items():
            view = view.replace(escaped_tile, replacement)


        cls.GAME.play_area = view

        return view
