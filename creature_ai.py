from creature import Creature
from utils._skill_index import SKILL_INDEX
from utils.utils import calculate, normalise
import math
import random



def get_action(
    creature: Creature,
    allies: list[Creature],
    foes: list[Creature],
    temperature: float,
    disposition: str
    ):
    disposition_multipliers = get_disposition_multipliers(disposition)
    options = []

    available_skills = []
    available_skills.extend([
        k for k, v in creature.limited_skills.items()
        if v > 0 and "battle" in SKILL_INDEX[k]["tags"]
    ])
    available_skills.extend([
        k for k, v in creature.cooldown_skills.items()
        if v == 0 and "battle" in SKILL_INDEX[k]["tags"]
    ])

    attack_skills = [skill for skill in available_skills if "attack" in SKILL_INDEX[skill]["tags"]]
    #heal_skills =   [skill for skill in available_skills if "restorative" in SKILL_INDEX[skill]["tags"]]
    #buff_skills =   []
    #debuff_skills = []

    options.extend(get_attack_options(creature,attack_skills,foes,disposition_multipliers["attack"]))
    #raise Exception(options)

    apply_temperature(options,temperature)

    return select_option(options)

def apply_temperature(options, temperature):
    options.sort(key=lambda option : option["probability"], reverse=True)
    if temperature < 1:
        options = options[0:1 + temperature.ceil(len(options)*temperature)]
    else:
        for option in options:
            option["probability"] = math.pow(option["probability"],1-(temperature-1))
    for option in options:
        option["probability"] = math.ceil(option["probability"]*100)

def select_option(options):
    total_rand = 0
    selection_value = -1
    for option in options:
        total_rand += option["probability"]
    rand = random.randint(0,total_rand)
    for option in options:
        selection_value += option["probability"]
        if selection_value > rand:
            return option
    return options[-1]

def get_attack_options(user:Creature ,skills:list[str], targets:list[Creature], multiplier:int):
    attack_options=[]
    # User HP for panic values
    user_hp = user.hit_points/user.max_hit_points
    user_hp_i = 1-user_hp

    # Skill damage string extraction
    skill_details=[SKILL_INDEX[skill] for skill in skills]
    skill_damage_calculations=[
        skill_detail["attack"]["dynamic_damage"](user.get_class_level(skill_detail["class"]))
        for skill_detail in skill_details
    ]
    skills.append("attack")
    skill_damage_calculations.append(user.attack_string)

    # calculate panic based multipliers
    averages=normalise([calculate(dmg,"average") * user_hp for dmg in skill_damage_calculations])
    maxes=normalise([calculate(dmg,"max") * user_hp_i for dmg in skill_damage_calculations])

    for index, skill in enumerate(skills):
        for target in targets:
            target_hp = target.hit_points/target.max_hit_points
            target_hp_i = 1-target_hp
            probability = (averages[index]*target_hp+maxes[index]*target_hp_i)*multiplier

            attack_options.append({
                "skill": skill,
                "target": target,
                "probability": probability
            })

    return attack_options

def get_healing_options(skill:str, targets:list[Creature]):
    pass

def get_disposition_multipliers(disposition: str):
    """ """
    match disposition:                       #atk,  heal, buff, debuff
        case "aggressive": raw_multipliers = [4,    1,    2,    1]
        case "support":    raw_multipliers = [1,    3,    4,    3]
        case "sapper":     raw_multipliers = [2,    1,    2,    3]
        case "healing":    raw_multipliers = [1,    4,    2,    1]
        case _:            raw_multipliers = [1,    1,    1,    1]

    return{
        "attack": raw_multipliers[0],
        "heal":   raw_multipliers[1],
        "buff":   raw_multipliers[2],
        "de-buff": raw_multipliers[3],
    }

# if __name__ == "__main__":
#     items = [
#         {"probability": 10},
#         {"probability": 5},
#         {"probability": 40},
#         {"probability": 250},
#         {"probability": 50},
#     ]

#     items.sort(key=lambda option : option["probability"], reverse=True)
#     print(items)


    # for dis in ["aggressive","support","sapper","healing","default"]:
    #     print(f"{dis}\n\t{get_disposition_multipliers(dis)}")