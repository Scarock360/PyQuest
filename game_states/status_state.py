import sys
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from player_creature import PlayerCreature
from game_state import AbstractGameState
from utils.selectors import Selector, GroupedSelector
from utils.utils import GREEN, RED, ENDC
from utils._class_index import CLASS_INDEX

class StatusState(AbstractGameState):
    
    menu_options = [
        "Attributes",
        "Classes",
        "Back"
    ]

    level_up_view = "Summary"
    attribute_selection = Selector(["power","resilience","agility"],3)

    @classmethod
    def setup(cls,game):
        cls.GAME = game

    @classmethod
    def pre_shift(cls, creature, previous_state):
        cls.level_up_view = "Summary"
        cls.previous_state = previous_state
        cls.creature = creature
        cls.level_up = isinstance(creature,PlayerCreature)
        cls.class_selection = GroupedSelector({c: CLASS_INDEX[c]["nodes"].keys() for c in cls.creature.get_levelable_classes()},6)

    @classmethod
    def handle_inputs(cls,key):
        match cls.level_up_view:
            case "Attributes":
                match f"{key}":
                    case "'s'":
                        cls.attribute_selection.down()
                    case "'w'":
                        cls.attribute_selection.up()
                    case "'a'":
                        if cls.creature.base_stats[cls.attribute_selection.getSelected()] > cls.creature.level + 1:
                            cls.creature.base_stats[cls.attribute_selection.getSelected()] -= 1
                            cls.creature.stat_points += 1
                            cls.creature.reset_stats()
                    case "'d'":
                        if cls.creature.stat_points > 0:
                            cls.creature.base_stats[cls.attribute_selection.getSelected()] += 1
                            cls.creature.stat_points -= 1
                            cls.creature.reset_stats()
            case "Classes":
                match f"{key}":
                    case "'s'":
                        cls.class_selection.down()
                    case "'w'":
                        cls.class_selection.up()
                    case "'a'":
                        pass
                    case "'d'":
                        pass
        cls.generate_display()

    @classmethod
    def compare_attribute(cls, attribute):
        return (
            "" if cls.attributes[attribute] == cls.creature.base_stats[attribute] else 
            f"{GREEN}" if cls.creature.base_stats[attribute] > cls.attributes[attribute] else 
            f"{RED}")

    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "Attributes":
                cls.attributes={ k:v for k,v in cls.creature.base_stats.items() if k in [a[2:] for a in cls.attribute_selection.getView()]}
                cls.level_up_view = event
                cls.generate_display()
            case "Classes":
                cls.level_up_view = event
                cls.generate_display()
            case "Back":
                cls.GAME.change_state(cls.previous_state)

    @classmethod
    def generate_display(cls):
        
        view = f"""{cls.creature.create_health_bar(58)}
Lv {cls.creature.level} {cls.creature.get_class()}"""
        match(cls.level_up_view):
            case "Summary":
                front_pad = lambda num_string: (3 - len(num_string))*"0"+num_string
                p = front_pad(f"{cls.creature.power}")
                r = front_pad(f"{cls.creature.resilience}")
                a = front_pad(f"{cls.creature.agility}")

                view += f"""\n    Power ------ {p}   Resilience - {r}   Agility ---- {a}"""
                if cls.creature == cls.GAME.party["hero"]:
                    view += "\nClasses:\n" + "\n".join([f"    {c}:{cls.creature.class_investment.get(c,0)}" for c in cls.creature.get_levelable_classes()])
            case "Attributes":
                # view += "\n\nAttributes:\n" + "\n".join([
                #     f"    {'➤' if index == cls.attribute_selection.current else ' '} {att}:{(10-len(att))*' '} - {cls.attributes[att]} + >> {cls.compare_attribute(att)}{cls.creature.base_stats[att]}{ENDC}"
                #     for index, att in enumerate(cls.attribute_selection.getView())
                # ])
                view += "\n\nAttributes:\n" + "\n".join([f"{att}:{(15-len(att))*' '} - {cls.attributes[att[2:]]} + >> {cls.compare_attribute(att[2:])}{cls.creature.base_stats[att[2:]]}{ENDC}" for att in cls.attribute_selection.getView()])

                view += f"\n\n    Remaining Attribute Points: {cls.creature.stat_points}"
            case "Classes":
                view += "\n Classes:\n" + "\n".join([ f"{s}" for s in cls.class_selection.getView()])
                cls.GAME.dialog_box = cls.class_selection.getSelected() + "\n"


        while len(view.split("\n")) < 11:
            view += "\n"
        cls.GAME.play_area = view
