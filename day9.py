#!/usr/bin/env python3
"""--- Day 9: Explosives in Cyberspace ---"""

FILE = 'input.txt'
DEBUG_INPUT = "(3x3)XYZ\nX(8x2)(3x3)ABCY\n(27x12)(20x12)(13x14)(7x10)(1x12)A"
DEBUG = False

import re

def init(file):
    with open(file) as f:
        input = f.read()
    return input

def decompress(line):
    uncompressed = ""
    it = re.finditer(r'\(([0-9]+x[0-9]+)\)', line)
    start = 0
    for patt in it:
        if start > patt.start(): # previous iteration went over this marker
            continue
        uncompressed += line[start:patt.start()]
        numbers = patt.group(1).split('x')
        str_len_to_unc = numbers[0]
        times_to_unc = numbers[1]

        uncompressed += line[patt.end():patt.end() + int(str_len_to_unc)] * int(times_to_unc)
        start = patt.end() + int(str_len_to_unc)

    uncompressed += line[start:] # add trailing chars in line
    return uncompressed

def decompress_markers(line):
    uncompressed_length = 0
    it = re.finditer(r'\(([0-9]+x[0-9]+)\)', line)
    start = 0
    for patt in it:
        if start > patt.start(): # previous iteration went over this marker
            continue
        numbers = patt.group(1).split('x')
        str_len_to_unc = numbers[0]
        times_to_unc = numbers[1]

        uncompressed_length += decompress_markers(line[patt.end():patt.end() + int(str_len_to_unc)]) * int(times_to_unc)
        start = patt.end() + int(str_len_to_unc)

    uncompressed_length += len(line[start:]) # add trailing chars in line
    return uncompressed_length

if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    inputd_lines = inputd.splitlines()

    decompressed_length = 0
    for line in inputd_lines:
        #print(decompress_markers(line))
        decompressed_length += decompress_markers(line)
    print("Decompressed length is " + str(decompressed_length))


