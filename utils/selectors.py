selector_icon = "➤"
up_icon = '⮙'
down_icon= '⮛'


class Selector:

    def __init__(self,items,view_height):
        self.v_min = 0
        self.items = items
        self.min = 0
        self.max = len(items) -1
        self.v_max = self.v_min - 1 + (view_height if view_height is not None else self.max)
        self.v_max = self.max if self.max < self.v_max else self.v_max
        self.current = 0
        self.v_height = view_height

    def getView(self):
        items = [f"  {i}" for i in self.items]
        if self.v_min is not self.min:
            items[self.v_min] = f"{up_icon} {self.items[self.v_min]}"
        if self.v_max is not self.max:
            items[self.v_max] = f"{down_icon} {self.items[self.v_max]}"
        items[self.current] = f"{selector_icon} {self.items[self.current]}"

        items = items[self.v_min: self.v_max+1]
        while len(items) < self.v_height:
            items.append("")

        return items

    def getSelected(self):
        return self.items[self.current]

    def up(self):
        self.current -= 1
        self.current = max(self.current, self.min)
        if self.current == self.v_min:
            if self.v_min > self.min:
                self.v_min -= 1
                self.v_max -= 1

    def down(self):
        self.current += 1
        self.current = min(self.current, self.max)
        if self.current == self.v_max:
            if self.v_max < self.max:
                self.v_min += 1
                self.v_max += 1


class GroupedSelector:
    def __init__(self, groups, view_height):
        self.groups = groups
        self.items = []
        self.master_list = []
        for k,v in groups.items():
            self.master_list.append(k)
            self.master_list.extend(v)
            self.items.append(k)
            self.items.extend([f"    {val}" for val in v])
        self.base_selector = Selector(self.items,view_height)
        self.base_selector.current = 1

    def updateGroups(self):
        pass

    def getView(self):
        view = self.base_selector.getView()
        prefix = view[0][0:6]
        value = view[0][6:]
        if view[0][2:] not in self.groups:
            for k,v in self.groups.items():
                if value in v:
                    view[0] = f"{prefix[0:2]}{k}"
        return view

    def getSelected(self):
        return self.master_list[self.base_selector.current]

    def up(self):
        self.base_selector.up()
        if self.base_selector.getSelected() in self.groups:
            if self.base_selector.current == 0:
                self.base_selector.down()
            else:
                self.base_selector.up()

    def down(self):
        self.base_selector.down()
        if self.base_selector.getSelected() in self.groups:
            self.base_selector.down()
