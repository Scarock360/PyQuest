import math
from utils._skill_index import SKILL_INDEX
from utils.utils import RED,YELLOW,GREEN,hr,vt,tl,tr,bl,br,FULL_BLOCK,HALF_BLOCK,EMPTY_BLOCK,ENDC,roll, WHITE
from utils._creature_index import CREATURE_INDEX
from functools import partial
import random


class Creature:
    name = None
    level = None
    hit_points = None
    max_hit_points = None
    power = None
    resilience = None
    agility = None
    attack_string = None
    attack_type = None
    accuracy = None
    boss = False
    cooldown_skills = None
    limited_skills = None
    attack_count = 1
    flags = {}

    end_of_turn_events = []

    box_colour = WHITE


    def __init__(
            self,
            name,
            max_hit_points,
            power,
            resilience,
            agility,
            attack_string,
            attack_type,
            accuracy,
            resistances,
            skills=[],
            actions=[],
            boss=False,
            level=1,
        ):
        self.name = name
        self.level = level
        self.hit_points = max_hit_points
        self.max_hit_points = max_hit_points
        self.power = power
        self.resilience = resilience
        self.agility = agility
        self.attack_string = attack_string
        self.attack_type = attack_type
        self.accuracy = accuracy
        self.resistances = resistances
        self.cooldown_skills = {s:0 for s in skills if "cooldown" in SKILL_INDEX[s]}
        self.limited_skills  = {s:SKILL_INDEX[s]["uses"] for s in skills if "uses" in SKILL_INDEX[s]}
        self.actions = actions
        self.boss = boss

    @classmethod
    def from_index(cls,index, boss_name_override=None, level=1):
        definition = CREATURE_INDEX[index]
        lv = max(level-1,0)
        level_ups = [0,0,0]
        for _ in range(lv):
            level_ups[random.choice([0,1,2])] += 1

        return cls(
            index if boss_name_override is None else boss_name_override,
            definition["max_hp"],
            definition["power"] + (lv * 1) + level_ups[0],
            definition["resilience"] + (lv * 1) + level_ups[1],
            definition["agility"] + (lv * 1) + level_ups[2],
            definition["damage"],
            definition["damage_type"],
            definition["accuracy"],
            definition["resistances"],
            definition.get("skills",[]),
            definition["actions"],
            boss_name_override is not None
        )

    def get_flag(self,flag):
        return self.flags.get(flag,0)

    def attack(self, foe, damage_override=None, type_override=None, accuracy_override=None):
        """attack"""
        attack_roll = roll("1d100")-self.agility+foe.agility
        if attack_roll < (self.accuracy if accuracy_override is None else accuracy_override ):
            damage_roll = self.attack_string if damage_override is None else damage_override
            damage_type = self.attack_type if type_override is None else type_override
            damage_delt = [foe.take_damage(roll(damage_roll) + self.power, damage_type) for _ in range(self.attack_count)]
            if self.attack_count == 1:
                return f"{self.name} deals {damage_delt[0]} {damage_type} damage to {'the ' if not foe.boss else ''}{RED}{foe.name}{ENDC}\n"
            total_damage = 0
            for i in range(len(damage_delt)):
                total_damage += damage_delt[i]
            return f"{self.name} deals {','.join([f'{dd}' for dd in damage_delt])} {damage_type} damage\nfor a total of {total_damage} to {'the ' if not foe.boss else ''}{RED}{foe.name}{ENDC}"
        return f"{self.name} missed {'the ' if not foe.boss else ''}{RED}{foe.name}{ENDC}\n"

    def take_damage(self, damage, damage_type="un-typed"):
        """damage"""
        damage_taken = damage * self.resistances.get(damage_type, 1)
        damage_taken = 0 if damage_taken == 0 else max(1,damage_taken-self.resilience)
        self.hit_points -= damage_taken
        self.hit_points = max(self.hit_points,0)
        return damage_taken

    def restore_hit_points(self,heal):
        previous_hp = self.hit_points
        self.hit_points = min(
            self.hit_points + roll(heal),
            self.max_hit_points
        )
        return self.hit_points - previous_hp

    def override_colours(self, box_colour = WHITE):
        self.box_colour = box_colour

    def create_health_bar(self, length_override = None):
        bar_length = 58 if self.boss else 10
        if length_override is not None:
            bar_length = length_override

        hp_percent = self.hit_points/self.max_hit_points
        greater = (hp_percent*bar_length).__floor__()
        if greater == bar_length:
            hp = f"{FULL_BLOCK*greater}"
            colour = GREEN
        else:
            lesser = ((hp_percent*bar_length) - greater)*bar_length
            final_block = EMPTY_BLOCK if lesser == 0 else HALF_BLOCK if lesser < 6 else FULL_BLOCK
            hp = f"{FULL_BLOCK*greater}{final_block}"
            hp = f"{hp}{EMPTY_BLOCK*(bar_length - 1 - greater)}"
            colour = GREEN if greater > math.floor(bar_length/2) else YELLOW if greater > math.floor(bar_length/5) else RED

        top = f"{self.box_colour}{tl}{hr}{self.name}{hr*(bar_length - 1 - len(self.name))}{tr}{ENDC}"
        hp_bar = f"{self.box_colour}{vt}{colour}{hp}{self.box_colour}{vt}{ENDC}"
        bottom = f"{self.box_colour}{bl}{hr*bar_length}{br}{ENDC}"
        return "\n".join([top, hp_bar, bottom])
    
    def end_turn(self):
        self.cooldown_skills = {s:max(c-1,0) for s,c in self.cooldown_skills.items()}