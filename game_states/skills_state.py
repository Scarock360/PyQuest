import math
import sys
import re
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from creature import Creature
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
    def _check_skill(cls,skill,usage):
        skill_detail = SKILL_INDEX[skill]
        if cls.previous_state not in skill_detail['tags']:
            return False
        if skill_detail.get("cooldown",False):
            if usage > 0:
                return False
        elif skill_detail.get("uses",False):
            if usage <= 0:
                return False
        if "summon" in skill_detail["tags"]:
            if len(cls.GAME.party) >= 3:
                return False
        return True

    @classmethod
    def pre_shift(cls,previous_state, creature):
        cls.previous_state = previous_state
        cls.selected_item = 0
        cls.creature = creature
        cls.menu_options = []

        cls.menu_options.extend([f"{'' if cls._check_skill(skill,cooldown) else GREY}{skill}{ENDC}" for skill,cooldown in creature.cooldown_skills.items()])
        cls.menu_options.extend([f"{'' if cls._check_skill(skill,uses) else GREY}{skill}{ENDC}" for skill,uses in creature.limited_skills.items()])
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
    def attack(cls,user:Creature,target:Creature,foes:list[Creature],skill_detail, then_from=""):
        attack_detail = skill_detail[then_from]["then"]["attack"] if then_from != "" else skill_detail["attack"]
        name = skill_detail["name"]
        tags = skill_detail["tags"]
        damage_class= skill_detail.get("class",None)
        cls.GAME.change_state(cls.previous_state)
        if "dynamic_damage" in attack_detail:
            damage_override = attack_detail["dynamic_damage"](cls.creature.get_class_level(damage_class))
        else:
            damage_override = attack_detail.get("damage",None)

        cls.GAME.states["battle"].combat_log.append(
            user.attack(
                foes=foes,
                target=foes.index(target),
                tags = tags,
                damage_override = damage_override,
                type_override = attack_detail.get("damage_type",None),
                accuracy_override = attack_detail.get("accuracy",None),
                count_override = attack_detail.get("count",None),
            ) + f" with {name}."
        )
        cls.GAME.states["battle"].combat_log_selected = -1

    @classmethod
    def perform_action(cls,skill:str,allies:list[Creature],foes:list[Creature],user:Creature,target:Creature):
        messages = []
        skill_detail = SKILL_INDEX[raw_text(skill)]
        if "temp_buff" in skill_detail["tags"]:
            for k,v in skill_detail["temp_buff"]["stats"].items():
                opp = v[0]
                value = int(v[1:])
                match opp:
                    case "*":
                        setattr(user,k,getattr(user,k)*value)
                    case "/":
                        setattr(user,k,getattr(user,k)/value)
                    case "+":
                        setattr(user,k,getattr(user,k)+value)
                    case "-":
                        setattr(user,k,getattr(user,k)-value)
            if skill_detail["temp_buff"].get("then",False):
                if "attack" in skill_detail["temp_buff"]["then"]:
                    cls.attack(user,target,foes,skill_detail,"temp_buff")
            else:
                cls.GAME.states["battle"].combat_log_selected = -1
        elif "attack" in skill_detail["tags"]:
            cls.attack(user,target,foes,skill_detail)
        elif "restorative" in skill_detail["tags"]:
            restored_hit_points = target.restore_hit_points(skill_detail["restorative"])
            cls.GAME.update_health_bars()
            messages.append(f"{user.name} uses {skill_detail['name']} on {target.name} restoring {GREEN}{restored_hit_points}{ENDC} hit points.\n")
        elif "self_flag" in skill_detail["tags"]:
            for flag in skill_detail["self_flag"].get("remove",[]):
                user.flags.pop(flag,None)
            for flag,value in skill_detail["self_flag"].get("add",{}).items():
                user.flags[flag] = value
            user.reset_stats()
        elif "summon" in skill_detail["tags"]:
            name = skill_detail["summon"]["creature"]
            if f"{name}_1" not in allies:
                name = f"{name}_1"
            elif f"{name}_2" not in allies:
                name = f"{name}_2"
            allies.append(Creature.from_index(
                skill_detail["summon"]["creature"],
                None,
                user.get_class_level(skill_detail["class"])
            ))
            cls.GAME.update_health_bars()
            #cls.GAME.change_state(cls.previous_state)
            summon_message = f"{user.name} summoned a {name[0:-2]} to help them.\n"
            if cls.previous_state == "battle":
                cls.GAME.states["battle"].setup_actors()
                cls.GAME.states["battle"].combat_log.append(summon_message)
                cls.GAME.states["battle"].combat_log_selected = -1
            else:
                cls.GAME.dialog_box = summon_message
        else:
            return

        if raw_text(skill) in user.cooldown_skills:
            user.cooldown_skills[raw_text(skill)] = skill_detail["cooldown"]
        if raw_text(skill) in user.limited_skills:
            user.limited_skills[raw_text(skill)] -= 1

        cls.GAME.change_state(cls.previous_state)


    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "Back":
                cls.GAME.change_state(cls.previous_state)
            case _:
                if raw_text(event)+ENDC in cls.menu_options:
                    skill_detail = SKILL_INDEX[raw_text(event)]
                    if len([tag for tag in skill_detail["tags"] if tag in ["restorative"]]) > 0:
                        options = [(v.name,partial(
                            cls.perform_action,
                            raw_text(event),
                            cls.GAME.party,
                            cls.GAME.states["battle"].enemies,
                            cls.creature,
                            v
                        )) for v in cls.GAME.party]
                        options.append(("Cancel",partial(cls.GAME.change_state,cls.previous_state)))
                        cls.GAME.states["question"].pre_shift(
                            "battle",
                            f"Who will you use {skill_detail['name']} on?",
                            options
                        )
                        cls.GAME.change_state("question")
                    else:
                        cls.perform_action(
                            raw_text(event),
                            cls.GAME.party,
                            cls.GAME.states["battle"].enemies,
                            cls.creature,
                            cls.GAME.states["battle"].selected_enemy
                        )
                    
                        if cls.previous_state == "battle":
                            cls.GAME.states["battle"].end_turn()


    @classmethod
    def generate_display(cls):
        selected_item = raw_text(cls.GAME._menu_selector.getSelected())
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
            cls.GAME.dialog_box = "go back\n"
