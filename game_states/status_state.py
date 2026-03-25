import sys
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from player_creature import PlayerCreature
from game_state import AbstractGameState

class StatusState(AbstractGameState):
    menu_options = [
        "Back"
    ]

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
        cls.GAME.change_state(cls.previous_state)

    @classmethod
    def generate_display(cls):
        view = f"""{cls.creature.create_health_bar(58)}
Power ------ {cls.creature.power}
Resilience - {cls.creature.resilience}
Agility ---- {cls.creature.agility}
        """

        while len(view.split("\n")) < 11:
            view += "\n"



        cls.GAME.play_area = view

        #cls.GAME.play_area = "\n".join(["test","test","test","test","test","test","test","test","test","test","test",])
    