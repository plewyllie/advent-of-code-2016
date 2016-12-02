FILE = 'input.txt'
DEBUG_INPUT = "ULL\nRRDDD\nLURDL\nUUUUD"
DEBUG = False

def init(file):
    with open(file) as f:
        # this will return a list containining all the instructions
        input = f.read()
    return input

class Keypad_finder:
    """ Keypad_finder is an object containing the necessary functions to find
    the keypad combination
    """

    def __init__(self, i, j, grid):
        self.grid = grid
        self.i = i
        self.j = j # starting at index 1,1

    def U(self):
        if self.i - 1 >= 0 and self.grid[self.i - 1][self.j] != 0:
            self.i -= 1
    def D(self):
        if self.i + 1 < len(self.grid) and self.grid[self.i + 1][self.j] != 0:
            self.i += 1
    def R(self):
        if self.j + 1 < len(self.grid[i]) and self.grid[self.i][self.j + 1] != 0:
            self.j += 1
    def L(self):
        if self.j - 1 >= 0 and self.grid[self.i][self.j - 1] != 0:
            self.j -= 1

if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    grid = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
    i = 2
    j = 0
    key = ""
    kf = Keypad_finder(i, j, grid)
    for line in inputd.splitlines():
        for k in range(0, len(line)):
            getattr(kf, line[k])()
        key += str(kf.grid[kf.i][kf.j])
    print("Key is " + key)


