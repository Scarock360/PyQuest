import math
from utils._skill_index import SKILL_INDEX
from utils._flag_index import FLAG_INDEX
from utils._item_index import ITEM_INDEX
from utils._class_index import CLASS_INDEX
from utils.utils import RED,YELLOW,GREEN,hr,vt,tl,tr,bl,br,FULL_BLOCK,HALF_BLOCK,EMPTY_BLOCK,ENDC,roll, WHITE
from utils._creature_index import CREATURE_INDEX
from functools import partial
import random

EXP_TO_LEVEL = 100

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

    true_prestige = False

    exp=0
    level=1

    stat_points = 5
    class_points = 10

    class_levels = {}

    class_investment = {}
    acquired_skills = []

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
        self.base_stats = {
            "max_hit_points":max_hit_points,
            "power":power,
            "resilience":resilience,
            "agility":agility,
            "attack_string":attack_string,
            "attack_type":attack_type,
            "accuracy":accuracy,
        }
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

        self.main_hand = None
        self.off_hand = None
        self.head = None
        self.body = None
        self.amulet = None
        self.ring_1 = None
        self.ring_2 = None

        self.true_prestige = False

        self.exp=0

        self.stat_points = 5
        self.class_points = 10

        self.class_levels = {}

        self.class_investment = {}
        self.acquired_skills = []

        self.end_of_turn_events = []

    @classmethod
    def from_index(cls,index, boss_name_override=None, level=1):
        definition = CREATURE_INDEX[index]
        lv = max(level-1,0)
        level_ups = [0,0,0]
        for _ in range(lv):
            level_ups[random.choice([0,1,2])] += 1

        c = cls(
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

        for i, item in enumerate(definition.get("equipment",[])):
            c.equip(i,item)

        for _, ability in enumerate(definition.get("abilities",[])):
            c.gain_ability(ability)

        return c

    def reset_stats(self):
        for slot,equiped_item in enumerate(self.get_gear()):
            if not self._validate(slot,None if equiped_item is None else ITEM_INDEX[equiped_item]):
                self.equip(slot,None)
        self.equip(0,self.get_gear()[0])
        new_stats = self.base_stats.copy()
        self.apply_flags(new_stats)
        for stat, value in new_stats.items():
            setattr(self,stat,value)

    def apply_flags(self, temp_stats = None):
        if temp_stats is None:
            stats = self.base_stats.copy()
            for stat in stats.keys():
                stats[stat]= getattr(self,stat)
        else:
            stats = temp_stats

        new_flags = self.flags.copy()
        for flag, value in self.flags.items():
            if isinstance(value,str):
                v = self.get_class_level(value)
            else:
                v = value
            if "skill" in FLAG_INDEX[flag]["tags"]:
                if not (FLAG_INDEX[flag]["skill"] in self.cooldown_skills.keys() or FLAG_INDEX[flag]["skill"] in self.limited_skills.keys()):
                    new_flags.pop(flag,None)
                    continue
            match flag:
                case "Power Stance":
                    stats["power"] += v*2
                    break
                case "Defence Stance":
                    stats["resilience"] += v*2
                    break
                case "Agile Stance":
                    stats["agility"] += v*2
                    break
                case "Balanced Stance":
                    stats["power"] += v
                    stats["resilience"] += v
                    stats["agility"] += v
                    break
        self.flags = new_flags

    def add_skill(self,skill):
        skill_details = SKILL_INDEX[skill]
        if "cooldown" in skill_details:
            self.cooldown_skills[skill] = 0
        if "uses" in skill_details:
            self.limited_skills[skill]=skill_details["uses"]
    
    def remove_skill(self,skill):
        if skill in self.cooldown_skills:
            self.cooldown_skills.pop(skill,None)
        if skill in self.limited_skills:
            self.limited_skills.pop(skill,None)

    def get_flag(self,flag):
        return self.flags.get(flag,0)

    def attack(self, foe, damage_override=None, type_override=None, accuracy_override=None, count_override=None, can_crit=True):
        """attack"""
        attack_roll = roll("1d100")-self.agility+foe.agility
        attack_count = self.attack_count if count_override is None else count_override
        if attack_roll < (self.accuracy if accuracy_override is None else accuracy_override ):
            damage_roll = self.attack_string if damage_override is None else damage_override
            damage_type = self.attack_type if type_override is None else type_override
            damage_delt = [foe.take_damage(roll(damage_roll) + self.power, damage_type) for _ in range(attack_count)]
            if attack_count == 1:
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

    def start_turn(self):
        self.reset_stats()

    def end_turn(self):
        self.cooldown_skills = {s:max(c-1,0) for s,c in self.cooldown_skills.items()}

    def get_gear(self):
        return [
            self.main_hand,
            self.off_hand,
            self.head,
            self.body,
            self.amulet,
            self.ring_1,
            self.ring_2,
        ]

    def equip(self,slot,item):
        stats, equipment = self._equip(slot,item)
        self.apply_flags(stats)
        for stat, value in stats.items():
            setattr(self,stat,value)
        old_equipment = [
            self.main_hand,
            self.off_hand,
            self.head,
            self.body,
            self.amulet,
            self.ring_1,
            self.ring_2,
        ]

        self.main_hand = equipment[0]
        self.off_hand = equipment[1]
        self.head = equipment[2]
        self.body = equipment[3]
        self.amulet = equipment[4]
        self.ring_1 = equipment[5]
        self.ring_2 = equipment[6]

        return [item for i , item in enumerate(old_equipment) if item != equipment[i]]

    def check_equip(self,slot,item):
        stats, _ = self._equip(slot,item)
        self.apply_flags(stats)
        return stats

    def _equip(self,slot,item):
        if self._validate(slot,None if item is None else ITEM_INDEX[item]):
            stats = self.base_stats.copy()
            equipment = [
                self.main_hand,
                self.off_hand,
                self.head,
                self.body,
                self.amulet,
                self.ring_1,
                self.ring_2,
            ]
            if item is not None and slot == 0 and ("2h_weapon" in ITEM_INDEX[item]["tags"] and self.get_flag("Powerful Hands") == 0):
                equipment[1] = None
            if item is not None and slot == 1 and equipment[0] is not None and ("2h_weapon" in ITEM_INDEX[self.main_hand]["tags"] and self.get_flag("Powerful Hands") == 0):
                equipment[0] = None
            equipment[slot] = item
            equipment_data = [ITEM_INDEX.get(e,None) for e in equipment]

            for i,e in enumerate(equipment_data):
                if e is not None:
                    if i == 0:
                        stats["attack_string"] = e["weapon"]["damage"]
                        stats["accuracy"] = e["weapon"]["accuracy"]
                        if "2h_weapon" in e["tags"] and equipment_data[1] is not None:
                            #raise Exception("test")
                            stats["accuracy"] -= 0 if self.get_flag("Powerful Hands") > 1 else 20
                        stats["attack_type"] = e["weapon"]["damage_type"]
                    for stat in list(stats.keys())[1:]:
                        multi = 1 + (self.get_flag("Shield Master") if "shield" in e["tags"] else 0)
                        if isinstance(stats[stat],int):
                            stats[stat] += e.get(stat,0) * multi
            return stats, equipment

    def get_valid_gear(self):
        valid_equipment_types = [
            ["1h_weapon","2h_weapon"],
            ["shield"],
            ["head"],
            ["body"],
            ["amulet"],
            ["ring"],
            ["ring"]
        ]
        if self.get_flag("Shield Master") > 0:
            valid_equipment_types[0].append("shield")
        if self.get_flag("Dual Wield"):
            valid_equipment_types[1].append("1h_weapon")
            if self.get_flag("Powerful Hands"):
                valid_equipment_types[1].append("2h_weapon")

        return valid_equipment_types

    def _validate(self,slot,item_data):
        if item_data is None:
            return True

        for t in self.get_valid_gear()[slot]:
            if t in item_data["tags"]:
                return True
        return False

    def get_class(self):
        if len(self.class_investment) > 0:
            return CLASS_INDEX[[k for k in self.class_investment.keys()][len(self.class_investment.keys())-1]]["class_name"]
        return "Peasant"

    def get_class_level(self,class_name):
        if self.true_prestige:
            return self.level
        else:
            c_level = self.class_investment.get(class_name,0)
            if len(self.class_investment) > 2:
                c_level += [l for l in self.class_investment.values()][-1]
            return c_level

    def gain_exp(self,exp):
        self.exp += exp
        level_ups = 0
        while self.exp > (self.level) * EXP_TO_LEVEL:
            self.exp -= (self.level) * EXP_TO_LEVEL
            level_ups += 1
        if level_ups > 0:
            self.level += level_ups
            self.stat_points += level_ups * 2
            self.class_points += level_ups

    def gain_ability(self, ability):
        if ability in self.acquired_skills:
            return
        if self.class_points > 0 and self.vlaidate_ability(ability):
            class_details, ability_details = self.get_ability(ability)
            if class_details["class_id"] not in self.class_investment:
                self.class_investment[class_details["class_id"]] = 0
                self.class_levels[class_details["class_id"]] = 0
            self.class_investment[class_details["class_id"]] += 1
            self.class_levels[class_details["class_id"]] += 1
            self.acquired_skills.append(ability_details["ability_id"])
            self.class_points -= 1

            effect = ability_details["effect"]
            if "increase" in effect:
                for k,v in effect["increase"].items():
                    setattr(self,k,getattr(self,k)+v)
            if "increase_flag" in effect:
                for k,v in effect["increase_flag"].items():
                    if k not in self.flags:
                        self.flags[k] = 0
                    self.flags[k] += v
            if "skills" in effect:
                for skill in effect["skills"]:
                    self.add_skill(skill)
            self.check_prestige()

    def check_prestige(self):
        invested_classes = list(self.class_investment.keys())
        for c in invested_classes:
            if self.class_investment[c] == 0:
                self.class_investment.pop(c)
                invested_classes.pop(invested_classes.index(c))
        add_prestige = True
        if len(invested_classes) == 2:
            for i_c in invested_classes:
                if CLASS_INDEX[i_c]["type"] == "Prestige":
                    add_prestige = False
            if add_prestige:
                for p_c in [c for c in CLASS_INDEX.values() if c["type"] == "Prestige"]:
                    if invested_classes[0] in p_c["required_base"] and invested_classes[1] in p_c["required_base"]:
                        self.class_investment[p_c["class_id"]] = 0
                        return
            else:
                self.class_investment.pop(invested_classes[-1],None)

    def lose_ability(self,ability):
        class_details, ability_details = self.get_ability(ability)
        if ability_details["ability_id"] in self.acquired_skills:
            self.acquired_skills.remove(ability_details["ability_id"])
            self.class_investment[class_details["class_id"]] -= 1
            self.class_levels[class_details["class_id"]] -= 1
            if self.class_investment[class_details["class_id"]] == 0 and class_details["type"] == "Prestige":
                self.class_investment.pop(class_details["class_id"],None)
            self.class_points += 1
            for a in [s for s in self.acquired_skills][::-1]:
                if a in self.acquired_skills:
                    c_d, a_d = self.get_ability(a)
                    self.acquired_skills.remove(a)
                    self.class_investment[c_d["class_id"]] -= 1
                    should_lose_a = not self.vlaidate_ability(a)
                    self.acquired_skills.append(a)
                    self.class_investment[c_d["class_id"]] += 1
                    if should_lose_a:
                        self.lose_ability(a)
            
            effect = ability_details["effect"]
            if "increase" in effect:
                for k,v in effect["increase"].items():
                    setattr(self,k,getattr(self,k)-v)
            if "increase_flag" in effect:
                for k,v in effect["increase_flag"].items():
                    self.flags[k] -= v
                    if self.flags[k] == 0:
                        self.flags.pop(k,None)
            if "skills" in effect:
                for skill in effect["skills"]:
                    self.remove_skill(skill)
            self.check_prestige()

    def get_levelable_classes(self):
        if len(self.class_investment) > 2:
            return self.class_investment.keys()
        else:
            return [c for c,d in CLASS_INDEX.items() if d["type"] == "Base"]

    def get_ability(self,ability):
        for _,class_details in CLASS_INDEX.items():
            for ability_name, ability_details in class_details["nodes"].items():
                if ability == ability_name:
                    return (class_details,ability_details)
        return (None,None)

    def vlaidate_ability(self,ability):
        class_details, ability_details = self.get_ability(ability)
        if class_details is None and ability_details is None:
            return None
        # Check class compatibility
        if len(self.class_investment) < 2:
            if class_details["type"] == "Prestige":
                return False
        else:
            if class_details["class_id"] not in self.class_investment:
                return False
        # Check ability requirements
        requirements = ability_details["requirements"]
        if "previous_nodes" in requirements:
            if "all_of" in requirements["previous_nodes"]:
                for required_node in requirements["previous_nodes"]["all_of"]:
                    if required_node not in self.acquired_skills:
                        return False
            if "number_of" in requirements["previous_nodes"]:
                count = 0
                for required_node in requirements["previous_nodes"]["number_of"]["of"]:
                    if required_node in self.acquired_skills:
                        count += 1
                if count < requirements["previous_nodes"]["number_of"]["number"]:
                    return False
        if "Investment" in requirements:
            for c,amount in requirements["Investment"].items():
                if self.class_investment.get(c,0) < amount:
                    return False

        # Default true
        return True