import math
import sys
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from game_state import AbstractGameState
from utils.selectors import Selector, GroupedSelector, TieredSelector
from utils.utils import GREEN, RED, ENDC, GREY, tl, vt, bl, hr, tt, rt, bt, raw_text
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
    def pre_shift(cls, creature, previous_state, level_up=False):
        cls.level_up_view = "Summary"
        cls.previous_state = previous_state
        cls.creature = creature
        if level_up:
            cls.menu_options = [
                "Attributes",
                "Classes",
                "Back"
            ]
        else:
            cls.menu_options = ["Back"]

        cls.class_selection = TieredSelector({c: list(CLASS_INDEX[c]["nodes"].keys()) for c in CLASS_INDEX},6)
        cls.ability_selection = None
        cls.class_view_level = "class"

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
                        match cls.class_view_level:
                            case "abilities":
                                cls.ability_selection.down()
                            case "class":
                                cls.class_selection.down()
                    case "'w'":
                        match cls.class_view_level:
                            case "abilities":
                                cls.ability_selection.up()
                            case "class":
                                cls.class_selection.up()
                    case "'a'":
                        if cls.class_view_level == "abilities":
                            cls.class_view_level = "class"
                    case "'d'":
                        match cls.class_view_level:
                            case "class":
                                selected_class = cls.class_selection.getSelected()
                                if selected_class in cls.creature.get_levelable_classes():
                                    cls.class_view_level = "abilities"
                                    cls.ability_selection = cls.class_selection.get_sub_selector()
                            case "abilities":
                                ability = cls.ability_selection.getSelected()
                                if ability in cls.creature.acquired_skills:
                                    cls.creature.lose_ability(ability)
                                else:
                                    cls.creature.gain_ability(ability)
                                cls.creature.reset_stats()
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
                if cls.level_up_view == "Summary":
                    cls.GAME.change_state(cls.previous_state)
                else:
                    cls.level_up_view = "Summary"

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
                view += "\nClasses:\n" + "\n".join([f"    {c}:{cls.creature.class_investment.get(c,0)}" for c in cls.creature.get_levelable_classes()])
            case "Attributes":
                view += "\n\nAttributes:\n" + "\n".join([f"{att}:{(15-len(att))*' '} - {cls.attributes[att[2:]]} + >> {cls.compare_attribute(att[2:])}{cls.creature.base_stats[att[2:]]}{ENDC}" for att in cls.attribute_selection.getView()])

                view += f"\n\n    Remaining Attribute Points: {cls.creature.stat_points}"
            case "Classes":
                selector_view = cls.class_selection.getView()
                selector_view = [f"{x[0:2]}{GREY if x[2:] not in cls.creature.get_levelable_classes() else ''}{x[2:]}{ENDC}" for x in selector_view]
                selected_class = cls.class_selection.getSelected()
                match(cls.class_view_level):
                    case "class":
                        cls.GAME.dialog_box = f"{selected_class}\n{CLASS_INDEX[selected_class]['description']}"
                    case "abilities":

                        #message = "\n"
                        abilities_view = cls.ability_selection.getView()
                        separator = f"{tl}{hr}{vt} {vt} {vt} {vt} {bl}{hr}"
                        separator_swap = {
                            f"{tl}{hr}":f"{tt}{hr}",
                            f"{vt} "   :f"{rt} ",
                            f"{bl}{hr}":f"{bt}{hr}"
                        }
                        c = cls.class_selection.current - cls.class_selection.v_min
                        max_len = 0
                        for cl in CLASS_INDEX.keys():
                            max_len = max(max_len, len(cl))

                        for i in range(6):
                            selected = i == c
                            padding = f'{hr}' if selected else ' '
                            separator_char = separator_swap[f"{separator[i*2]}{separator[i*2+1]}"] if selected else f"{separator[i*2]}{separator[i*2+1]}"
                            pre_ability = abilities_view[i][0:2]
                            ability = abilities_view[i][2:]
                            ability_colour = (
                                GREEN if ability in cls.creature.acquired_skills else
                                GREY if not cls.creature.vlaidate_ability(ability) else
                                ''
                            )
                            ability = f"{ability_colour}{ability}{ENDC}"
                            selector_view[i]+=f"{padding*((max_len+3)-len(raw_text(selector_view[i])))}{separator_char}  {pre_ability}{ability}"

                        _, ability_details = cls.creature.get_ability(cls.ability_selection.getSelected())
                        cls.GAME.dialog_box = ability_details["ability_id"] + "\n" + (
                            ability_details["description"]
                            if cls.creature.vlaidate_ability(ability_details["ability_id"])
                            else ability_details["requirements"]["description"]
                        )


                view += f"\n Classes:{' '*19}Class Points:{cls.creature.class_points}\n" + "\n".join([ f"  {s}" for s in selector_view])

                # 



        while len(view.split("\n")) < 11:
            view += "\n"
        cls.GAME.play_area = view
