from equiped_creature import EquipedCreature
from utils._item_index import ITEM_INDEX
from utils._class_index import CLASS_INDEX

EXP_TO_LEVEL = 100

class PlayerCreature(EquipedCreature):

    true_prestige = False

    exp=0
    level=1

    stat_points = 5
    class_points = 10

    class_levels = {}

    class_investment = {}
    acquired_skills = []

    def __init__(self, name, max_hit_points, power, resilience, agility, attack_string, attack_type, accuracy, resistances, skills=[], boss=False):
        super().__init__(name, max_hit_points, power, resilience, agility, attack_string, attack_type, accuracy, resistances, skills, boss)

    def get_class(self):
        if len(self.class_investment) > 0:
            return CLASS_INDEX[[k for k in self.class_investment.keys()][len(self.class_investment.keys())-1]]["class_name"]
        return "Peasant"

    def get_class_level(self,class_name):
        if self.true_prestige:
            return self.level
        else:
            c_level = self.class_investment[class_name]
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