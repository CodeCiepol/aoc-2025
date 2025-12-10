import argparse

class Safe:
    def __init__(self):
        self.dial_position: int = 50
        self.no_of_position_0: int = 0

    def _check_pos_0(self):
        if self.dial_position == 0:
            self.no_of_position_0 += 1

    def _check_dial(self, prev_position):
        if self.dial_position >= 100:
            if self.dial_position > 100:
                self.no_of_position_0 += 1
                print("klikam bo powyzej 100")
            self.dial_position = self.dial_position - 100
            print("przeskoczylo bo wieksze od 100!")
        if self.dial_position < 0:
            self.dial_position = 100 + self.dial_position
            if prev_position != 0:
                self.no_of_position_0 += 1
            print("klikam bo ponizej 100")
            print("przeskoczylo bo mniejsze od 100!")
        if self.dial_position >= 100 or self.dial_position < 0:
            prev_position = 1
            self._check_dial(prev_position)

    def move_dial(self,direction,clicks):
        prev_position = self.dial_position
        if direction == "L":
            self.dial_position -= clicks
        elif direction == "R":
            self.dial_position += clicks
        self._check_dial(prev_position)
        self._check_pos_0()
        
def count_0_positions(filepath: str):
    safe=Safe()
    with open(filepath, "r") as f:
        for line in f:
            direction: str = line[0]
            clicks: int = int(line[1:])
            print("new move",direction,clicks)
            safe.move_dial(direction,clicks)
            print("current dial position: ", safe.dial_position)
            print("current 0 pos counter: ", safe.no_of_position_0)
    print (safe.no_of_position_0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument("--filepath")
    args = parser.parse_args()
    count_0_positions(args.filepath)
