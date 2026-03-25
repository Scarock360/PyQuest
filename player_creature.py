from equiped_creature import EquipedCreature
from utils._item_index import ITEM_INDEX

EXP_TO_LEVEL = 100

class PlayerCreature(EquipedCreature):

    exp=0
    level=1

    stat_points = 5
    class_points = 1

    def __init__(self, name, max_hit_points, power, resilience, agility, attack_string, attack_type, accuracy, resistances, skills=[], boss=False):
        super().__init__(name, max_hit_points, power, resilience, agility, attack_string, attack_type, accuracy, resistances, skills, boss)

    def gain_exp(self,exp):
        self.exp += exp
        level_ups = 0
        while self.exp > (self.level) * EXP_TO_LEVEL:
            self.exp -= EXP_TO_LEVEL
            level_ups += 1
        if level_ups > 0:
            self.level += level_ups
            self.stat_points += level_ups * 2
            self.class_points += level_ups
