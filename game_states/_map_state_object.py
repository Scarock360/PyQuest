from utils import utils


class MapObject:

    def getLocationOf(self,tile):
        if tile is not None:
            for y,line in enumerate(self.split_map):
                for x,tile_half in enumerate(line):
                    if tile_half == tile[0]:
                        try:
                            if line[x+1] == tile[1]:
                                return x,y
                        except:
                            pass
        return None,None



    def __init__(self, map_state, level, start_location_override = None):
        level_to_load = map_state.levels[level].get_level()
        self.split_map = level_to_load["map"].split("\n")
        self._MAP = level_to_load["map"]
        self.default_interactions = level_to_load["default_interactions"]
        self.solid_chars = level_to_load["solid_chars"]
        psx,psy = self.getLocationOf("SP")
        self.player_coords = {"x":psx,"y":psy} if start_location_override is None else start_location_override
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
            self.split_map[e_y] = self.split_map[e_y][:e_x]+"⚠ "+self.split_map[e_y][e_x+2:]
            if e_y not in self.enemy_register:
                self.enemy_register[e_y]={}
            self.enemy_register[e_y][e_x] = encounter["enemies"]

        for tile, encounter in level_to_load.get("enemies",{}).items():
            e_x, e_y = self.getLocationOf(tile)
            self.split_map[e_y] = self.split_map[e_y][:e_x]+"⚠ "+self.split_map[e_y][e_x+2:]
            if e_y not in self.enemy_register:
                self.enemy_register[e_y]={}
            self.enemy_register[e_y][e_x] = encounter["enemies"]



        for tile, treasure in level_to_load.get("treasures",{}).items():
            t_x ,t_y = self.getLocationOf(tile)
            treasure["location"]={}
            treasure["location"]["x"]=t_x
            treasure["location"]["y"]=t_y
            self.split_map[t_y] = self.split_map[t_y][:t_x]+"⋐⋑"+self.split_map[t_y][t_x+2:]
            if t_y not in self.treasure_register:
                self.treasure_register[t_y]={}
            self.treasure_register[t_y][t_x] = treasure


        for tile,interaction in level_to_load.get("custom_interactions",{}).items():
            i_x ,i_y = self.getLocationOf(tile)
            interaction["location"]={}
            interaction["location"]["x"]=i_x
            interaction["location"]["y"]=i_y
            if i_y not in self.interaction_register:
                self.interaction_register[i_y]={}
            self.interaction_register[i_y][i_x] = interaction


        for tile,location_trigger in level_to_load.get("location_triggers",{}).items():
            l_x ,l_y = self.getLocationOf(tile)
            if l_y not in self.location_trigger_register:
                self.location_trigger_register[l_y]={}
            self.location_trigger_register[l_y][l_x] = location_trigger
        self._MAP = "\n".join(self.split_map)

    def update_location(self, location=None):
        if location is not None and location is not (None,None):
            self.player_coords = {"x":location[0],"y":location[1]}
        return self
