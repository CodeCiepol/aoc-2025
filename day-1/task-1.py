class Safe:
    def __init__(self):
        self.dial_position = 50
        self.no_of_position_0 = 0

    def _check_dial(self):
        if self.dial_position > 99:
            self.dial_position = self.dial_position - 99
        if self.dial_position < 0:
            self.dial_position = 99 + self.dial_position
        if self.dial_position > 99 or self.dial_position < 0:
            self._check_dial()
        if self.dial_position == 0:
            self.no_of_position_0 += 1

    def move_dial(self,direction,clicks):
        if direction == "L":
            self.dial_position -= clicks
        elif direction == "R":
            self.dial_position += clicks
        self._check_dial()
        
safe=Safe()
print (safe.dial_position)
safe.move_dial("R",50)
print (safe.dial_position)

