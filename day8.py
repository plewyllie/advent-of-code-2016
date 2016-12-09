#!/usr/bin/env python3
"""--- Day 8: Two-Factor Authentication ---"""

FILE = 'input.txt'
DEBUG_INPUT = "rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1"

DEBUG = False

import numpy as np
import re

def init(file):
    with open(file) as f:
        input = f.read()
    return input

class Screen:
    def __init__(self, h, l):
        self.scr = np.empty( (h,l), dtype='unicode_' )
        self.scr[:] = '_'
    def on(self, l, h):
        self.scr[0:h,0:l] = '#'
    def rotate(self, axis, axis_nb, amount):
        if axis == 'y': # horizontal roll
            self.scr[axis_nb] = np.roll(self.scr[axis_nb], amount)
        elif axis == 'x': # vertical roll
            self.scr[:,axis_nb] = np.roll(self.scr[:, axis_nb], amount)
    def pixels_lit(self):
        return len(np.where(self.scr == "#")[0])

if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
        scr = Screen(3, 7)
    else:
        scr = Screen(6, 50)
        inputd = init(FILE)

    inputd_lines = inputd.splitlines()

    for line in inputd_lines:
        if line.startswith("rect"):
            res = re.search(r'([0-9])+x([0-9])+', line)
            size = res.group().split('x')
            scr.on(int(size[0]), int(size[1]))
        if line.startswith("rotate"):
            res = re.search(r'(x|y)=([0-9]+) by ([0-9])+', line)
            inst = res.group()
            inst_nb = res.group()[2:].split(' by ')
            scr.rotate(inst[0], int(inst_nb[0]), int(inst_nb[1]))
        #print(scr.scr)

    np.set_printoptions(linewidth=400)
    print(scr.scr)
    print("There are " + str(scr.pixels_lit()) + " pixels lit")













