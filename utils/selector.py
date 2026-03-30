class Selector:
    
    def __init__(self,minimum,maximum):
        self.min = minimum
        self.max = maximum
        self.current = 0

    def up(self, number):
        self.current -= number
        if self.current < self.min:
            self.current = self.min
    
    def down(self, number):
        self.current += number
        if self.current > self.max:
            self.current = self.max
