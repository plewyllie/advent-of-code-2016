#!/usr/bin/env python3
"""Day 6: Signals and Noise"""

FILE = 'input.txt'
DEBUG = False

import collections

def init(file):
    with open(file) as f:
        input = f.read()
    return input


if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    inputd_list = [x for x in inputd.splitlines()]

    message = ""
    dics = [collections.defaultdict(int) for _ in range(0, len(inputd_list[0]))]
    for line in inputd_list:
        for i, c in enumerate(line):
            dics[i][c] += 1

    for d in dics:
        message += ''.join([v[0] for v in sorted(d.items(), key=lambda kv: (kv[1], kv[0]))][0])

    print(message)


        

