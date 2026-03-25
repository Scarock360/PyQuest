import math
import sys
import re
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from game_state import AbstractGameState
from utils._item_index import ITEM_INDEX
from utils.utils import GREEN, GREY, ENDC, chunks, roll, text_len, raw_text
from functools import partial
from utils._skill_index import SKILL_INDEX

class SkillsState(AbstractGameState):
    menu_options = []
    previous_state=""
    creature = None

    @classmethod
    def setup(cls,game):
        cls.GAME = game

    @classmethod
    def pre_shift(cls,previous_state, creature):
        cls.previous_state = previous_state
        cls.selected_item = 0
        cls.creature = creature
        cls.menu_options = []

        cls.menu_options.extend([f"{GREY if cooldown > 0 or cls.previous_state not in SKILL_INDEX[skill]['tags'] else ''}{skill}{ENDC}" for skill,cooldown in creature.cooldown_skills.items()])
        cls.menu_options.extend([f"{GREY if uses <= 0 or cls.previous_state not in SKILL_INDEX[skill]['tags'] else ''}{skill}{ENDC}" for skill,uses in creature.limited_skills.items()])
        cls.menu_options.append("Back")

    @classmethod
    def handle_inputs(cls,key):
        if cls.previous_state == "battle" and f"{key}" in ["'a'","'d'"]:
            cls.GAME.states[cls.previous_state].handle_inputs(key)
        cls.generate_display()

    @classmethod
    def _use_restorative(cls,user, skill_detail, target):
        restored_hit_points = target.restore_hit_points(skill_detail["restorative"])
        cls.GAME.update_health_bars()
        message = f"{user.name} uses {skill_detail['name']} on {target.name} restoring {GREEN}{restored_hit_points}{ENDC} hit points.\n"
        if "cooldown" in skill_detail:
            user.cooldown_skills[skill_detail["name"]] = skill_detail["cooldown"]
        if "uses" in skill_detail:
            user.limited_skills[skill_detail["name"]] -= 1
        if cls.previous_state == "battle":
            cls.GAME.states["battle"].combat_log.append(message)
            cls.GAME.states["battle"].combat_log_selected = -1
            cls.GAME.change_state("battle")
            cls.GAME.states["battle"].end_turn()
        else:
            cls.GAME.dialog_box= message
            cls.GAME.change_state(cls.previous_state)
            cls.GAME.states[cls.previous_state].generate_display()

    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "Back":
                cls.GAME.change_state(cls.previous_state)
            case _:
                skill_detail = SKILL_INDEX[raw_text(event)]
                if raw_text(event)+ENDC in cls.menu_options:
                    if "attack" in skill_detail["tags"]:
                        cls.GAME.change_state(cls.previous_state)
                        cls.GAME.states["battle"].combat_log.append(
                            cls.creature.attack(
                                cls.GAME.states["battle"].enemies[cls.GAME.states["battle"].selected_enemy],
                                damage_override = skill_detail["attack"].get("damagee",None),
                                type_override = skill_detail["attack"].get("damage_type",None),
                                accuracy_override = skill_detail["attack"].get("accuracy",None),
                            ) + f"with {skill_detail['name']}."
                        )
                        cls.GAME.states["battle"].combat_log_selected = -1
                        cls.GAME.states["battle"].end_turn()
                    elif "restorative" in skill_detail["tags"]:
                        options = {v.name:partial(cls._use_restorative,cls.creature,skill_detail,v) for _,v in cls.GAME.party.items()}
                        options["Cancel"] = partial(cls.GAME.change_state,"inventory")
                        
                        cls.GAME.states["question"].pre_shift(
                            "battle",
                            f"Who will you use {skill_detail['name']} on?",
                            options
                        )
                        cls.GAME.change_state("question")
                        #cls.GAME.change_state(cls.previous_state)
                        return
                    else:
                        return
                    if raw_text(event) in cls.creature.cooldown_skills:
                        cls.creature.cooldown_skills[raw_text(event)] = skill_detail["cooldown"]
                    if raw_text(event) in cls.creature.limited_skills:
                        cls.creature.limited_skills[raw_text(event)] -= 1

    @classmethod
    def generate_display(cls):
        selected_item = raw_text(cls.menu_options[cls.GAME._menu_values["c"]])
        if selected_item != "Back":
            selected_skill_detail = SKILL_INDEX[selected_item]
            usage_indicator = ""
            if "cooldown" in selected_skill_detail:
                usage_indicator = f"Cooldown:{cls.creature.cooldown_skills[selected_item]}/{selected_skill_detail['cooldown']}"
            elif "uses" in selected_skill_detail:
                usage_indicator = f"Remaining uses:{cls.creature.limited_skills[selected_item]}/{selected_skill_detail['uses']}"
            buffer = 60-text_len(f"{selected_skill_detail['name']}:{usage_indicator}")
            line1 = f"{selected_skill_detail['name']}:{' '* buffer}{usage_indicator}"
            cls.GAME.dialog_box = f"{line1}\n{selected_skill_detail['description']}"
        else:
            cls.GAME.dialog_box = "go\nback"
