from creature import Creature
from utils._item_index import ITEM_INDEX

class EquipedCreature(Creature):





    def __init__(self, name, max_hit_points, power, resilience, agility, attack_string, attack_type, accuracy, resistances, skills=[], boss=False):
        super().__init__(name, max_hit_points, power, resilience, agility, attack_string, attack_type, accuracy, resistances, skills, boss)
        self.base_stats = {
            "max_hit_points":max_hit_points,
            "power":power,
            "resilience":resilience,
            "agility":agility,
            "attack_string":attack_string,
            "attack_type":attack_type,
            "accuracy":accuracy,
        }

        self.main_hand = None
        self.off_hand = None
        self.head = None
        self.body = None
        self.amulet = None
        self.ring_1 = None
        self.ring_2 = None

    def _reset_stats(self):
        for stat, value in self.base_stats.items():
            setattr(self,stat,value)

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
                        multi = 1 + self.get_flag("Shield Master") if "shield" in e["tags"] else 0
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
