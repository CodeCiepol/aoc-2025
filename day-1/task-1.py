import argparse

class Safe:
    def __init__(self):
        self.dial_position: int = 50
        self.no_of_position_0: int = 0

    def _check_dial(self):
        if self.dial_position >= 100:
            self.dial_position = self.dial_position - 100
        if self.dial_position < 0:
            self.dial_position = 100 + self.dial_position
        if self.dial_position >= 100 or self.dial_position < 0:
            self._check_dial()
        if self.dial_position == 0:
            self.no_of_position_0 += 1

    def move_dial(self,direction,clicks):
        if direction == "L":
            self.dial_position -= clicks
        elif direction == "R":
            self.dial_position += clicks
        self._check_dial()
        
def count_0_positions(filepath: str):
    safe=Safe()
    with open(filepath, "r") as f:
        for line in f:
            direction: str = line[0]
            clicks: int = int(line[1:])
            safe.move_dial(direction,clicks)
    print (safe.no_of_position_0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument("--filepath")
    args = parser.parse_args()
    count_0_positions(args.filepath)
