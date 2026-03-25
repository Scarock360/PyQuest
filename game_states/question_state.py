import sys
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from game_state import AbstractGameState
from utils._item_index import ITEM_INDEX
from utils.utils import GREY, ENDC, chunks, text_len


class QuestionState(AbstractGameState):
    menu_options = ["Select"]

    options = {}

    @classmethod
    def setup(cls,game):
        cls.GAME = game

    
    @classmethod
    def pre_shift(cls,previous_state,question,options):
        cls.previous_state = previous_state
        cls.question = question
        cls.max_selection = len(options)-1
        cls.options = options
        cls.selected_item = 0

    @classmethod
    def handle_inputs(cls,key):
        if f"{key}" in ["'a'","Key.left"]:
            cls.change_selection(-1)
        elif f"{key}" in ["'d'","Key.right"]:
            cls.change_selection(1)

    @classmethod
    def change_selection(cls,value):
        new_value = cls.selected_item + value
        if new_value >= 0 and new_value <= cls.max_selection:
            cls.selected_item = new_value
        cls.generate_display()

    @classmethod
    def handle_menu_event(cls,event):
        list(cls.options.items())[cls.selected_item][1]()

    @classmethod
    def generate_display(cls):

        answers = "".join([f"{'  ' if i != cls.selected_item else '➤ '}{a}" for i,a in enumerate(list(cls.options.keys()))])

        view = f"{cls.question}\n{answers}"

        cls.GAME.dialog_box = view
