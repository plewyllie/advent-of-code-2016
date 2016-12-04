FILE = 'input.txt'
DEBUG_INPUT = "5 10 25\n 20 10 31"
DEBUG = False

def init(file):
    with open(file) as f:
        # this will return a list containining all the instructions
        input = f.read()
    return input

class ImpossibleTriangle(Exception):
    pass
class Triangle:
    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:    
            raise ImpossibleTriangle("Invalid Triangle")

        

if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    amount = 0
    invalid = 0
    inputd.splitlines()

    inputd_list = [line.split() for line in inputd.splitlines()]

    for i in range(0, len(inputd_list), 3):
        for j in range(0, 3):
            try:
                Triangle(int(inputd_list[i][j]),int(inputd_list[i + 1][j]), int(inputd_list[i + 2][j]))
                amount += 1
                #print(tr)
            except ImpossibleTriangle:
                invalid += 1
                pass

    print("Amount of valid triangles: " + str(amount))
    print("Amount of invalid triangles: " + str(invalid))

