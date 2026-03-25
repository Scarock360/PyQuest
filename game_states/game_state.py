class AbstractGameState:
    menu_options = []

    @classmethod
    def setup(cls,game):
        raise NotImplementedError()

    @classmethod
    def handle_inputs(cls,key):
        raise NotImplementedError()

    @classmethod
    def handle_menu_event(cls,event):
        raise NotImplementedError()

    @classmethod
    def generate_display(cls):
        raise NotImplementedError()
