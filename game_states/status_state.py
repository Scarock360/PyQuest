import sys
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from player_creature import PlayerCreature
from game_state import AbstractGameState

class StatusState(AbstractGameState):
    
    menu_options = [
        "Attributes",
        "Classes",
        "Back"
    ]

    level_up_view = "summary"
    attribute_selection = {"min":0,"c":0,"max":3}
    base_attributes = ["power","resilience","agility"]

    @classmethod
    def setup(cls,game):
        cls.GAME = game

    @classmethod
    def pre_shift(cls, creature, previous_state):
        cls.previous_state = previous_state
        cls.creature = creature
        cls.level_up = isinstance(creature,PlayerCreature)

    @classmethod
    def handle_inputs(cls,key):
        pass#raise NotImplementedError()

    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "Attributes":
                cls.attributes={ k:v for k,v in cls.creature.base_stats.items() if k in cls.base_attributes}
                cls.level_up_view = event
                cls.generate_display()
            case "Classes":
                pass
            case "Back":
                cls.GAME.change_state(cls.previous_state)

    @classmethod
    def generate_display(cls):
        
        view = f"""{cls.creature.create_health_bar(58)}
Lv {cls.creature.level} {cls.creature.get_class()}"""
        match(cls.level_up_view):
            case "summary":

                p = f"{cls.creature.power}"
                r = f"{cls.creature.resilience}"
                a = f"{cls.creature.agility}"

                p = (3 - len(p))*"0"+p
                r = (3 - len(r))*"0"+r
                a = (3 - len(a))*"0"+a

                view += f"""\n    Power ------ {p}   Resilience - {r}   Agility ---- {a}"""
                if cls.creature == cls.GAME.party["hero"]:
                    view += "\nClasses:\n" + "\n".join([f"    {c}:{cls.creature.class_investment.get(c,0)}" for c in cls.creature.get_levelable_classes()])
            case "Attributes":
                
                p = cls.creature.base_stats["power"]
                r = cls.creature.base_stats["resilience"]
                a = cls.creature.base_stats["agility"]

                # view += "\nAttributes:\n" + "\n".join(
                #     [
                #         f"    {k}:{(10-len(k))*' '} - {cls.attributes[k]} + >> {v}"
                #         for k,v in cls.creature.base_stats.items() if k in cls.base_attributes
                #     ])
                view += "\nAttributes:\n" + "\n".join(
                    [
                        f"    {'>' if index == cls.attribute_selection['c'] else ' '}{att}:{(10-len(att))*' '} - {cls.attributes[att]} + >> {cls.creature.base_stats[att]}"
                        for index, att in enumerate(cls.base_attributes)
                    ])

        while len(view.split("\n")) < 11:
            view += "\n"
        cls.GAME.play_area = view
