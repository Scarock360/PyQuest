import math
import sys
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from game_state import AbstractGameState
from utils._item_index import ITEM_INDEX
from utils.utils import vt, hr, tt, bt,tl,tr,bl,br, BOLD, UNDRLN, ENDC, RED, GREEN, WHITE, text_len

class EquipmentState(AbstractGameState):
    menu_options = [
        "Equip",
        "Back"
    ]

    gear_type_selection = {"min":0,"c":0,"max":6}
    gear_selection = {"min":0,"c_min":0,"c":0,"c_max":0,"max":0}
    previous_state=""

    gear_types = [
        ["1h_weapon","2h_weapon"],
        ["shield"],
        ["head"],
        ["body"],
        ["amulet"],
        ["ring"],
        ["ring"]
    ]
    gear_type = None
    gear_list = []

    @classmethod
    def setup(cls,game):
        cls.GAME = game

    @classmethod
    def pre_shift(cls,previous_state):
        cls.previous_state = previous_state
        cls.gear_type = None
        cls.gear_type_selection["c"] = 0
        cls.previous_dialog = cls.GAME.dialog_box

    @classmethod
    def handle_inputs(cls,key):
        match f"{key}":
            case "'w'":
                if cls.gear_type:
                    cls.change_gear_selection(-1)
                else:
                    cls.change_gear_type_selection(-1)
            case "'d'":
                pass#cls.change_selection(1)
            case "'a'":
                pass#cls.change_selection(-1)
            case "'s'":
                if cls.gear_type:
                    cls.change_gear_selection(1)
                else:
                    cls.change_gear_type_selection(1)

    @classmethod
    def change_gear_type_selection(cls,change):
        gts = cls.gear_type_selection
        new_val = gts["c"]+change
        if not new_val > gts["max"] and not new_val < 0:
            gts["c"] = new_val
        cls.generate_display()

    @classmethod
    def change_gear_selection(cls,change):
        new_selection = cls.gear_selection["c"] + change
        if new_selection < 0 or new_selection > cls.gear_selection["max"]:
            return
        cls.gear_selection["c"] = new_selection
        
        r_s = cls.gear_selection
        r_s["c"] = new_selection

        if r_s["c"] == r_s["c_min"]:
            if r_s["c_min"] != r_s["min"]:
                r_s["c_min"] -= 1
                r_s["c_max"] -= 1

        if r_s["c"] == r_s["c_max"]:
            if r_s["c_max"] != r_s["max"]:
                r_s["c_max"] += 1
                r_s["c_min"] += 1

        #cls.GAME.dialog_box = f"{r_s}\n"
        cls.generate_display()

    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "Equip":
                if cls.gear_type:
                    new_item = cls.gear_list[cls.gear_selection["c"]]
                    cls.GAME.remove_item(new_item)
                    for old_item in list(cls.GAME.party.items())[0][1].equip(cls.gear_type_selection["c"],new_item):
                        cls.GAME.add_item(old_item)
                    cls.gear_type = None
                    cls.generate_display()
                else:
                    cls.set_gear_type()
            case "Back":
                if cls.gear_type:
                    cls.gear_type = None
                    cls.generate_display()
                else:
                    cls.GAME.change_state(cls.previous_state)

    @classmethod
    def set_gear_type(cls):
        cls.gear_type = cls.gear_types[cls.gear_type_selection["c"]]
        cls.gear_list = [None]
        for g_type in cls.gear_type:
            cls.gear_list.extend(
                [g for g in cls.GAME.inventory.keys() if g_type in ITEM_INDEX[g]["tags"]]
            )
        cls.gear_selection = {
            "min":0,
            "c_min":0,
            "c":0,
            "c_max":min(len(cls.gear_list)-1,6),
            "max":len(cls.gear_list)-1
        }
        cls.generate_display()

    @classmethod
    def compare(cls,old,new):
        if isinstance(new,int):
            return (
                GREEN if new > old else
                RED if old > new else
                WHITE
            )
        if isinstance(new,str):
            try:
                old_count, old_size = [int(i) for i in old.split("d")]
                new_count, new_size = [int(i) for i in new.split("d")]
                old_average = old_count*(old_size+1)/2
                new_average = new_count*(new_size+1)/2

                return (
                    GREEN if new_average > old_average else
                    RED if old_average > new_average else
                    GREEN if new_count > old_count else
                    RED if old_count > new_count else
                    WHITE
                )
            except:
                return WHITE

    @classmethod
    def generate_stats(cls,creature):
        view = [f"{bl}{hr}{br}{UNDRLN}{BOLD}         STATS             {ENDC}"]
        if cls.gear_type:
            for stat, new_val in creature.check_equip(cls.gear_type_selection["c"],cls.gear_list[cls.gear_selection["c"]]).items():
                old_val = getattr(creature,stat)
                colour = cls.compare(old_val,new_val)
                view.append(f"{stat.replace('_',' ')}{' '*(14-len(stat))}:{colour}{old_val}{' '*(5-len(f'{old_val}'))} >> {new_val}{ENDC}")
        else:
            for stat in creature.base_stats.keys():
                view.append(f"{stat.replace('_',' ')}{' '*(14-len(stat))}:{getattr(creature,stat)}")

        while len(view) < 8:
            view.append("")
        return view

    @classmethod
    def generate_gear(cls,creature):
        gear = {
            "Main hand": creature.main_hand,
            "Off hand ": creature.off_hand,
            "Head     ": creature.head,
            "Body     ": creature.body,
            "Amulet   ": creature.amulet,
            "Ring L   ": creature.ring_1,
            "Ring R   ": creature.ring_2
        }

        view = [f"{UNDRLN}{BOLD}            GEAR          {ENDC}{bl}{hr}{br}"]
        
        if cls.gear_type is None:
            for i,g in enumerate(list(gear.items())):
                view.append(f"{'➤ ' if i == cls.gear_type_selection['c'] else '  '}{g[0]}:{g[1]}")
            cls.GAME.dialog_box = "Select equipment to replace.\n"
        else:
            items = [f"{'➤ ' if cls.gear_selection['c'] == i else '  '}{g}" for i,g in enumerate(cls.gear_list)]
            view.extend(items[cls.gear_selection["c_min"]:])
            view = view[:8]
            un_equip_txt = "Unequip currently equipped item.\n"
            item = cls.gear_list[cls.gear_selection['c']]
            cls.GAME.dialog_box = un_equip_txt if item is None else ITEM_INDEX[item]["Description"]

        while len(view) < 8:
            view.append(" ")
        return view

    @classmethod
    def generate_display(cls):
        player = list(cls.GAME.party.items())[0][1]
        view_1 = cls.generate_stats(player)
        view_2 = cls.generate_gear(player)

        view = [f"{tl}{hr*29}{tt}{hr*28}{tr}"]
        for i in range(8):
            view.append(f"{view_1[i]}{' '*(30 - text_len(view_1[i]))}{vt}{view_2[i]}")
        view.append(f"{tl}{hr}{tr}{' '*27}{vt}{' '*26}{tl}{hr}{tr}")
        view.append(f"{bl}{hr*29}{bt}{hr*28}{br}")
        cls.GAME.play_area = "\n".join([f"{line}" for line in view])
