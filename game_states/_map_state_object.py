from utils import utils


class MapObject:
    def __init__(self, map_state, level, start_location_override = None):
        level_to_load = map_state.levels[level].get_level()
        split_map = level_to_load["map"].split("\n")
        self._MAP = level_to_load["map"]
        self.default_interactions = level_to_load["default_interactions"]
        self.solid_chars = level_to_load["solid_chars"]
        self.player_coords = level_to_load["starting_position"] if start_location_override is None else start_location_override
        self.escaped_tiles = level_to_load["escaped_tiles"]
        self.char_colours = {}
        for char,colour in level_to_load["colours"].items():
            self.char_colours[char] = getattr(utils,colour)
        map_state.GAME.dialog_box = level_to_load["entry_text"]

        self.enemy_register={}
        self.treasure_register={}
        self.interaction_register={}
        self.location_trigger_register={}

        for encounter in level_to_load.get("encounters",[]):
            e_x = encounter["location"]["x"]
            e_y = encounter["location"]["y"]
            split_map[e_y] = split_map[e_y][:e_x]+"𝍑 "+split_map[e_y][e_x+2:]
            if e_y not in self.enemy_register:
                self.enemy_register[e_y]={}
            self.enemy_register[e_y][e_x] = encounter["enemies"]


        for treasure in level_to_load.get("treasures",[]):
            t_x = treasure["location"]["x"]
            t_y = treasure["location"]["y"]
            split_map[t_y] = split_map[t_y][:t_x]+"⋐⋑"+split_map[t_y][t_x+2:]
            if t_y not in self.treasure_register:
                self.treasure_register[t_y]={}
            self.treasure_register[t_y][t_x] = treasure


        for interaction in level_to_load.get("custom_interactions",[]):
            i_x = interaction["location"]["x"]
            i_y = interaction["location"]["y"]
            if i_y not in self.interaction_register:
                self.interaction_register[i_y]={}
            self.interaction_register[i_y][i_x] = interaction


        for location_trigger in level_to_load.get("location_triggers",[]):
            l_x = location_trigger["location"]["x"]
            l_y = location_trigger["location"]["y"]
            if l_y not in self.location_trigger_register:
                self.location_trigger_register[l_y]={}
            self.location_trigger_register[l_y][l_x] = location_trigger
        self._MAP = "\n".join(split_map)

    def update_location(self, location=None):
        if location is not None:
            self.player_coords = location
        return self
