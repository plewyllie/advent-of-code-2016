#!/usr/bin/env python3
"""--- Day 12: Leonardo's Monorail ---"""
import re

FILE = 'input.txt'
DEBUG_INPUT = "cpy 41 a\ninc a\ninc a\ndec a\njnz a 2\ndec a"
DEBUG = False

INSTRUCTIONS_BUS = []
INSTR_PTR = 0

class Register:
    def __init__(self):
        self.val = 0

# copy val in register r
def cpy(val, r):
    r.val = val
    global INSTR_PTR
    INSTR_PTR += 1
def inc(r):
    r.val += 1
    global INSTR_PTR
    INSTR_PTR += 1
def dec(r):
    r.val -= 1
    global INSTR_PTR
    INSTR_PTR += 1
# jump y instructions if x is not 0
def jnz(x, y):
    global INSTR_PTR

    try:
        x = x.val
    except AttributeError:
        pass

    if x == 0:
        INSTR_PTR += 1
        return
    #print("Increasing PTR", INSTR_PTR);
    INSTR_PTR += y
    #print("Increased PTR", INSTR_PTR);

def init(file):
    with open(file) as f:
        input = f.read()
    return input

if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    INSTRUCTIONS_BUS = inputd.splitlines()
    registers = {x:Register() for x in [chr(i) for i in range(ord('a'),ord('d')+1)]}

    while INSTR_PTR < len(INSTRUCTIONS_BUS):
        instr = INSTRUCTIONS_BUS[INSTR_PTR]
        ins = instr[:3]
        #print(instr)
        if ins == "cpy":
            try:
                val = int(re.search(r'[0-9]+', instr[3:]).group())
            except AttributeError:
                val = registers[instr[4]].val
            r = registers[instr[-1]]
            attrib = (val, r)
        elif ins == "jnz":
            x = int(instr[4]) if re.search(r'[0-9]+', instr[4]) else registers[instr[4]]
            y = int(re.search(r'(\+|\-)*[0-9]+', instr[5:]).group())
            attrib = (x, y)
        else:
            attrib = [registers[instr[4]]]
        
        method = eval(ins)
        method(*attrib)

    for r in registers:
        print(r, registers[r].val)






























