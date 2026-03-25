import math
import random
import sys, inspect
import time
sys.path.insert(0,"../PyQuest\\game_states" )
from utils._creature_index import CREATURE_INDEX
from game_state import AbstractGameState
from creature import Creature
from utils.utils import RED, ENDC, text_len, MAGENTA, WHITE

class BattleState(AbstractGameState):
    menu_options = [
        "Attack",
        "Defend",
        "Items",
        "Skills",
        "Examine",
        "Flee"
    ]

    selected_enemy = 0
    combat_log_selected = -1
    combat_log = []
    enemies = []

    turn_tracker = 0
    actors = []

    @classmethod
    def setup(cls,game):
        cls.GAME = game

    @classmethod
    def load_battle(cls,enemies):
        cls.raw_enemies = enemies
        cls.enemies = []
        for e_def in enemies:
            cls.enemies.append(Creature.from_index(
                e_def["creature"],
                e_def.get("boss_name", None),
                e_def["level"]))
            cls.is_boss = True if e_def.get("boss_name", None) is not None else False
        for e in cls.enemies:
            e.override_colours(box_colour= RED)
        cls.actors=[]
        cls.turn_tracker = 0
        cls.actors.extend([v for _,v in cls.GAME.party.items()])
        cls.actors.extend(cls.enemies)
        cls.selected_enemy = 0
        cls.combat_log_selected = -1
        cls.combat_log = [f"You've encountered some {RED}enemies{ENDC}\n"]
        cls.actors[cls.turn_tracker].override_colours(box_colour = MAGENTA)
        cls.GAME.update_health_bars()
        cls.generate_dialog()

    @classmethod
    def handle_inputs(cls,key):
        match f"{key}":
            case "'w'":
                cls.change_log_message(-1)
            case "'d'":
                cls.change_selection(1)
            case "'a'":
                cls.change_selection(-1)
            case "'s'":
                cls.change_log_message(1)

    @classmethod
    def change_selection(cls,change_amount):
        new_selection = cls.selected_enemy + change_amount
        if new_selection > len(cls.enemies)-1 or new_selection < 0:
            return
        cls.selected_enemy = new_selection
        cls.generate_display()

    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "Attack":
                cls.combat_log.append(
                    cls.actors[cls.turn_tracker].attack(cls.enemies[cls.selected_enemy])
                )
                cls.combat_log_selected = -1
                cls.end_turn()
            case "Defend":
                cls.end_turn()
            case "Skills":
                cls.GAME.states["skills"].pre_shift("battle",cls.actors[cls.turn_tracker])
                cls.GAME.change_state("skills")
            case "Flee":
                cls.GAME.change_state("map")
            case "Items":
                cls.GAME.states["inventory"].pre_shift("battle")
                cls.GAME.change_state("inventory")
            case "Examine":
                cls.GAME.states["status"].pre_shift(cls.enemies[cls.selected_enemy],"battle")
                cls.GAME.change_state("status")

    @classmethod
    def generate_dialog(cls):
        log_to_display_lines=cls.combat_log[cls.combat_log_selected].split("\n")
        bottom = cls.combat_log_selected == -1
        top = cls.combat_log_selected == (-len(cls.combat_log))
        if not top:
            line_len = text_len(log_to_display_lines[0])
            log_to_display_lines[0] += " "*(60-2-line_len) + "⮙ "
        if not bottom:
            line_len = text_len(log_to_display_lines[1])
            log_to_display_lines[-1] += " "*(60-2-line_len) + "⮛ "

        cls.GAME.dialog_box="\n".join(log_to_display_lines)

    @classmethod
    def change_log_message(cls,value):
        if len(cls.combat_log) == 0:
            return
        new_val = cls.combat_log_selected + value
        if new_val < 0 and new_val >= (-(len(cls.combat_log))):
            cls.combat_log_selected = new_val
        cls.generate_dialog()

    @classmethod
    def end_turn(cls):
        cls.actors[cls.turn_tracker].end_turn()
        cls.turn_tracker += 1
        if cls.turn_tracker >= len(cls.actors):
            cls.turn_tracker = 0
        cls.generate_dialog()
        cls.generate_display()
        player_actors = len([act for act in cls.actors if act in [pm[1] for pm in cls.GAME.party.items()]])
        if player_actors <= 0:
            return
        if len(cls.actors) - player_actors <= 0:
            return
        if cls.turn_tracker >= len([act for act in cls.actors if act in [pm[1] for pm in cls.GAME.party.items()]]):
            cls.enemy_turn()
            return cls.end_turn()

    @classmethod
    def enemy_turn(cls):
        creature = cls.actors[cls.turn_tracker]
        action_max = -1
        for a in creature.actions:
            action_max += a["chance"]
        target_max = len([act for act in cls.actors if act in [pm[1] for pm in cls.GAME.party.items()]])-1
        if target_max == -1:
            return False

        target = random.Random().randint(0,target_max)
        action_val = random.Random().randint(0,action_max)
        action=None
        for a in creature.actions:
            action_val -= a["chance"]
            if action_val <= 0:
                action = a
                break
            
        match(action["action"]):
            case "attack":
                cls.combat_log.append(
                    creature.attack(list(cls.GAME.party.items())[target][1])
                )
            case "nothing":
                cls.combat_log.append(
                    action["message"].replace("{NAME}",creature.name)
                )
        time.sleep(0.5)
        return True

    @classmethod
    def _calculate_exp(cls):
        exp = 0
        player_level = cls.GAME.party["hero"].level
        for e in cls.raw_enemies:
            exp_multi = -(player_level - e["level"])*0.1
            exp_multi += 1
            exp_multi = min(exp_multi,2)
            exp_multi = max(exp_multi,0)
            exp += e["level"] * CREATURE_INDEX[e["creature"]]["exp"] * exp_multi
        return int(exp)

    @classmethod
    def generate_display(cls):
        for a in cls.actors:
            if a.hit_points <=0:
                i = cls.actors.index(a)
                cls.actors.pop(i)
                if i < cls.turn_tracker:
                    cls.turn_tracker -= 1
                if a in cls.enemies:
                    cls.enemies.pop(cls.enemies.index(a))
        player_actor_count = len([act for act in cls.actors if act in [pm[1] for pm in cls.GAME.party.items()]])
        cls.GAME.update_health_bars()
        if player_actor_count <=0:
            cls.GAME.states["title"].pre_shift()
            return cls.GAME.change_state("title")
        if len(cls.enemies) <= 0:
            cls.GAME.states["map"].resolve_combat(cls._calculate_exp())
            cls.GAME.change_state("map")
            for a in cls.actors:
                a.override_colours(box_colour=WHITE)
            cls.GAME.update_health_bars()
            return
        if cls.selected_enemy > len(cls.enemies)-1:
            cls.selected_enemy = len(cls.enemies)-1

        for i,a in enumerate(cls.actors):
            a.override_colours(
                box_colour =
                    MAGENTA if i == cls.turn_tracker else
                    RED if a in cls.enemies else
                    WHITE
            )
        cls.GAME.update_health_bars()

        health_bars = [e.create_health_bar().split("\n") for e in cls.enemies]
        c = len(health_bars)
        padding = " "*math.floor((60-c*12)/(c+1))  if not cls.is_boss else ""
        view = []
        for i in range(11):
            if i < 3:
                view.append(padding.join(["",*[f'{bar[i]}'for j, bar in enumerate(health_bars)]]))
            elif i == 3:
                view.append(f"{' '*(5+len(padding)+(12+len(padding))*cls.selected_enemy)}⮙")
            else:
                view.append("")
        cls.GAME.play_area = "\n".join(view)
        





