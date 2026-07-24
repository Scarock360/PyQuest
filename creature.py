import math
from utils._skill_index import SKILL_INDEX
from utils._flag_index import FLAG_INDEX
from utils._item_index import ITEM_INDEX
from utils._class_index import CLASS_INDEX
from utils.utils import RED,YELLOW,GREEN,hr,vt,tl,tr,bl,br,FULL_BLOCK,HALF_BLOCK,EMPTY_BLOCK,ENDC,calculate, WHITE,CYAN, BG_FROM_COLOUR, raw_text
from utils._creature_index import CREATURE_INDEX
import random

EXP_TO_LEVEL = 100

class Creature:
    battleState = None

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
        # Basic stats
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
        self.additional_attack_tags = []
        self.inventory = {}
        self.flags={}
        self.attack_count = 1

        # Equipment
        self.main_hand = None
        self.off_hand = None
        self.head = None
        self.body = None
        self.amulet = None
        self.ring_1 = None
        self.ring_2 = None

        # Level up stats
        self.true_prestige = False
        self.exp=0
        self.stat_points = 2*level
        self.class_points = 10*level
        self.class_levels = {}
        self.class_investment = {}
        self.acquired_skills = []
        self.end_of_turn_events = []

        # other stats
        self.temp_hitpoints = 0
        self.acceleration = 0

    @classmethod
    def from_index(cls,index, boss_name_override=None, level=1):
        definition = CREATURE_INDEX[index]
        lv = max(level-1,0)
        level_up_stats = [0,0,0]
        for _ in range(lv):
            level_up_stats[random.choice([0,1,2])] += 1

        c = cls(
            index if boss_name_override is None else boss_name_override,
            definition["max_hp"],
            definition["power"] + (lv * 1) + level_up_stats[0],
            definition["resilience"] + (lv * 1) + level_up_stats[1],
            definition["agility"] + (lv * 1) + level_up_stats[2],
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

        for level_threshold, level_up_ability in definition.get("levels",{}).items():
            if level >= level_threshold:
                c.gain_ability(level_up_ability)


        # for i, ability in enumerate(definition.get("levels",[])):
        #     if i <= lv:
        #         c.gain_ability(ability)

        # for _, ability in enumerate(definition.get("abilities",[])):
        #     c.gain_ability(ability)

        return c

    def reset_stats(self):
        for slot,equiped_item in enumerate(self.get_gear()):
            if not self._validate(slot,None if equiped_item is None else ITEM_INDEX[equiped_item]):
                for i in self.equip(slot,None):
                    self.add_item(i)
        sts, inv = self._equip(0,self.get_gear()[0])
        for i in inv:
            self.add_item(i)
        self.apply_flags(sts)
        for stat, value in sts.items():
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

    def check_dual_wield(self):
        if self.get_flag("Dual Wield") <= 0 or self.off_hand is None:
            return None
        oh_detail = ITEM_INDEX[self.off_hand]
        tags = oh_detail["tags"]
        if "shield" in tags and self.get_flag("Shield Master") <= 0:
            return None
        if "weapon" in oh_detail:
            return oh_detail
        return None

    def replace_class_refs(self, string:str):
        for c in list(CLASS_INDEX.keys()):
            string = string.replace(c,f"{self.get_class_level(c)}")
        return string

    def _get_elemental_tag(self,damage_type):
        match damage_type:
            case "Fire":
                if self.get_flag(f"{damage_type} Adept") > 0:
                    return ["burn:Elemental"]
            case "Wind":
                if self.get_flag(f"{damage_type} Adept") > 0:
                    return ["haste:Elemental"]
            case "Cold":
                if self.get_flag(f"{damage_type} Adept") > 0:
                    return ["frost:Elemental"]
            case "Earth":
                if self.get_flag(f"{damage_type} Adept") > 0:
                    return ["stun:Elemental"]
        return []

    def _get_weapon_tags(self,weapon):
        if weapon is None:
            return []
        else:
            return ITEM_INDEX[weapon]["tags"]

    def attack(self, foes, target, tags=None, damage_override=None, type_override=None, accuracy_override=None, count_override=None):
        """attack"""
        mh_damage_type =  type_override or self.attack_type
        mh_damage_roll = damage_override or self.attack_string
        mh_accuracy = accuracy_override or self.accuracy
        attack_count = count_override or self.attack_count

        attack_tags=[]
        attack_tags.extend(tags or [])
        attack_tags.extend(self.additional_attack_tags)
        attack_tags.extend(self._get_elemental_tag(mh_damage_type))
        attack_tags = [self.replace_class_refs(tag) for tag in attack_tags]

        mh_tags = [tag for tag in attack_tags]
        mh_tags.extend(self._get_weapon_tags(self.main_hand))

        if not ("cleave" in attack_tags or ("explosive" in attack_tags and "spell" in attack_tags)):
            foes = [foes[target]]


        oh_detail = None
        if "weapon" in attack_tags:
            oh_detail = self.check_dual_wield()
            if oh_detail is not None:
                oh_damage_type = type_override or oh_detail["weapon"]["damage_type"]
                oh_damage_roll = damage_override or oh_detail["weapon"]["damage"]
                oh_accuracy = accuracy_override or oh_detail["weapon"]["accuracy"]
                oh_tags = [tag for tag in attack_tags]
                oh_tags.extend(self._get_weapon_tags(self.off_hand))

        self.pre_attack(attack_tags)

        damage_delt = []
        for _ in range(attack_count):
            for foe in foes:
                damage_delt.append(self._attack(foe,mh_tags,mh_accuracy,mh_damage_roll,mh_damage_type))
                if oh_detail is not None:
                    damage_delt.append(self._attack(foe,oh_tags,oh_accuracy,oh_damage_roll,oh_damage_type))
        total_damage = sum(damage_delt)
        match len(damage_delt):
            case 0:
                if len(foes) == 1:
                    return f"{self.name} missed {'the ' if not foes[0].boss else ''}{RED}{foes[0].name}{ENDC}\n"
                return f"{self.name} missed all enemies\n"
            case 1:
                if len(foes) == 1:
                    return f"{self.name} deals {damage_delt[0]} {mh_damage_type} damage to {'the ' if not foes[0].boss else ''}{RED}{foes[0].name}{ENDC}\n"
                return f"{self.name} deals {damage_delt[0]} {mh_damage_type} damage to one enemy\n"
            case _:
                if len(foes) == 1:
                    return f"{self.name} deals {','.join([f'{dd}' for dd in damage_delt])} {mh_damage_type} damage\nfor a total of {total_damage} to {'the ' if not foes[0].boss else ''}{RED}{foes[0].name}{ENDC}"
                return f"{self.name} deals {total_damage} {mh_damage_type} damage across all enemies"

    def _attack(self,foe,attack_tags,accuracy,damage_die,damage_type):

        attack_power = int(self.power *(
            1.5 if "heavy" in attack_tags else
            0.5 if "light" in attack_tags else
            1
        ))
        gravity_bonus = attack_power if "gravity" in attack_tags else 0

        damage_delt = 0
        attack_roll = calculate("1d100")-self.agility+foe.agility
        if attack_roll < accuracy + gravity_bonus:
            crit_multiplier = 1
            if attack_roll < accuracy + gravity_bonus - 90:
                crit_multiplier = 2
            damage_delt = foe.take_damage(
                (calculate(self.replace_class_refs(damage_die)) + attack_power) * crit_multiplier + self.get_flag("Counter"),
                attack_tags,
                damage_type
            )
            self.flags["Counter"] = 0
            self.post_attack(foe, attack_tags, damage_delt)

        return damage_delt

    def pre_attack(self, tags):
        for tag in tags:
            tag_split = tag.split(":")
            tag_name  = tag_split[0]
            match tag_name:
                case "frost":
                    self.temp_hitpoints += int(tag_split[1])
                    self.temp_hitpoints = min(self.temp_hitpoints, self.max_hit_points)
                case "haste":
                    self.flags[tag_name] = self.get_flag(tag_name) + int(tag_split[1])
                    self.acceleration += int(tag_split[1])

    def post_attack(self, foe, tags, damage):
        for tag in tags:
            tag_split = tag.split(":")
            tag_name  = tag_split[0]
            match tag_name:
                case "energy":
                    if self.get_flag("Fire Adept") > 0:
                        foe.flags["burn"] = foe.get_flag("burn") + int(tag_split[1])
                        foe.flags[tag_name] = 1
                case "vampiric":
                    self.restore_hit_points(int(damage/2))
                case "spirit":
                    foe.resistances["ALL"] = foe.resistances.get("ALL",1) + 0.05
                case _:
                    if tag_name in ["burn","stun","magnetic","mirage","pressure","poison"]:
                        foe.flags[tag_name] = foe.get_flag(tag_name) + int(tag_split[1])
                        if tag_name == "pressure" and foe.get_flag(tag_name) > 99:
                            foe.flags[tag_name] = foe.get_flag(tag_name) - 100
                            pressure_damage = foe.take_damage(int(foe.max_hit_points*(0.1 if foe.boss else 0.3)),["penetrating"])
                            if self.battleState:
                                self.battleState.combat_log.append(
                                    f"{'The ' if not foe.boss else ''}{RED}{foe.name}{ENDC} burst taking {pressure_damage} damage.\n"
                                )

    def take_damage(self, damage, tags, damage_type="un-typed"):
        """damage"""
        if self.flags.get("Fortress",0) > 0:
            self.flags["Counter"] = self.flags.get("Counter",0) + damage
            return 0
        damage_taken = damage * self.resistances.get("ALL", 1)
        damage_taken = damage_taken * self.resistances.get(damage_type, 1)
        if damage_taken > 0:
            damage_taken -= 0 if "penetrating" in tags else self.resilience
            damage_taken = max(damage_taken, 1)
            damage_taken = math.floor(damage_taken)
        else:
            damage_taken = 0

        self.temp_hitpoints -= damage_taken
        if self.temp_hitpoints < 0:
            self.hit_points += self.temp_hitpoints
            self.temp_hitpoints = 0
        self.hit_points = max(self.hit_points,0)
        return damage_taken

    def restore_hit_points(self,heal):
        previous_hp = self.hit_points
        amount_to_heal = 0
        if isinstance(heal,int):
            amount_to_heal = heal
        else:
            amount_to_heal = calculate(self.replace_class_refs(heal))
        self.hit_points = min(
            self.hit_points + amount_to_heal,
            self.max_hit_points
        )
        return self.hit_points - previous_hp

    def add_item(self,item,count=1):
        if item is None:
            return
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] += count
        self.inventory[item] = min(self.inventory[item],999)

    def remove_item(self,item,count=1):
        if item is None:
            return
        self.inventory[item] -= count
        if self.inventory[item] < 0:
            pass
        if self.inventory[item] == 0:
            self.inventory.pop(item)

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

            
        temp_hp_percent = self.temp_hitpoints/self.max_hit_points
        greater = (temp_hp_percent*bar_length).__floor__()
        if greater == bar_length:
            temp_hp = f"{FULL_BLOCK*greater}"
        else:
            if temp_hp_percent > 0:
                lesser = ((temp_hp_percent*bar_length) - greater)*bar_length
                final_block = EMPTY_BLOCK if lesser == 0 else HALF_BLOCK if lesser < 6 else FULL_BLOCK
                temp_hp = f"{FULL_BLOCK*greater}{final_block}"
                temp_hp = f"{temp_hp}"
            else:
                temp_hp = ""

        top = f"{self.box_colour}{tl}{hr}{self.name}{hr*(bar_length - 1 - len(self.name))}{tr}{ENDC}"

        hp_bar = f"{self.box_colour}{vt}{BG_FROM_COLOUR[colour]}{CYAN}{temp_hp}{ENDC}{colour}{hp[len(temp_hp):]}{self.box_colour}{vt}{ENDC}"

        # hp_bar_2 = f"{self.box_colour}{vt}{colour}{hp}{self.box_colour}{vt}{ENDC}"




        bottom = f"{self.box_colour}{bl}{hr*bar_length}{br}{ENDC}"
        return "\n".join([top, hp_bar, bottom])

    def start_turn(self):
        messages=[]
        if(self.get_flag("burn") > 0):
            burn_damage = self.get_flag("burn")
            real_damage = self.take_damage(burn_damage, ["penetrating"], "Fire")
            if self.battleState:
                self.battleState.combat_log.append(
                    f"{'' if self.boss else 'The '}{RED}{self.name}{ENDC} burnt for {real_damage} Fire damage.\n"
                )
            if(self.get_flag("energy") > 0):
                self.flags["energy"] = 0
            else:
                self.flags["burn"] = int(burn_damage/2)
        if(self.get_flag("poison") > 0):
            poison_damage = self.get_flag("poison")
            real_damage = self.take_damage(poison_damage, ["penetrating"], "Toxic")
            if self.battleState:
                self.battleState.combat_log.append(
                    f"{'' if self.boss else 'The '}{RED}{self.name}{ENDC} suffered for {real_damage} Toxic damage.\n"
                )
            self.flags["poison"] -= 1
        self.flags.pop("Fortress","")
        self.reset_stats()
        return messages

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
            self.base_stats["max_hit_points"] += 5 * level_ups
            self.max_hit_points += 5 * level_ups
            self.base_stats["power"] += 1 * level_ups
            self.power += 1 * level_ups
            self.base_stats["resilience"] += 1 * level_ups
            self.resilience += 1 * level_ups
            self.base_stats["agility"] += 1 * level_ups
            self.agility += 1 * level_ups
            self.level += level_ups
            self.stat_points += 2 * level_ups
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