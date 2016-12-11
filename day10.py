#!/usr/bin/env python3
"""--- Day 10: Balance Bots ---"""

FILE = 'input.txt'
DEBUG_INPUT = "value 3 goes to bot 1\nvalue 2 goes to bot 2\nvalue 5 goes to bot 2\nbot 2 gives low to bot 1 and high to bot 0\nvalue 3 goes to bot 1\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0\nvalue 2 goes to bot 2"
DEBUG = False

import re

BOTS = {}
OUTPUTS = {}
INPUTS = {}

class Bin:
    def __init__(self, ido):
        self.type = "bin"
        self.id = ido
        self.micros = []
    def push(self, micro):
        self.micros.append(micro)

class Bot:
    def __init__(self, bot_id):
        self.type = "bot"
        self.low = float("-inf")
        self.high = float("-inf")
        self.low_to = None
        self.high_to = None
        self.id = bot_id

    def push(self, val):
        if val > self.high:
            self.low = self.high
            self.high = val
        else:
            self.low = val

        if (self.low == 17 and self.high == 61):
            print("My bot id is " + str(self.id))

        self.try_to_give()           

    def giving(self, low_to, high_to):
        self.low_to = low_to
        self.high_to = high_to

        self.try_to_give()

    def try_to_give(self):
        if self.low > float("-inf") and self.high > float("-inf"):
            try:
                self.low_to.push(self.low)
                self.high_to.push(self.high)
                self.low = float("-inf")
                self.high = float("-inf")
            except AttributeError:
                print("Bot", self.id, "does not know where to give yet")
                pass # This means we still don't know who is getting the vals

def init(file):
    with open(file) as f:
        input = f.read()
    return input

if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    inputd_lines = inputd.splitlines()
    giving_lines = [l for l in inputd_lines if l.startswith('bot')]
    value_lines = [l for l in inputd_lines if l.startswith('value')]

    for line in giving_lines:
        res = re.match(r'bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)', line)
        if res:
            bot_id = res.group(1)
            low_to_type = res.group(2)
            low_to_id = res.group(3)
            high_to_type = res.group(4)
            high_to_id = res.group(5)

            try :
                BOTS[bot_id]
            except KeyError:
                BOTS[bot_id] = Bot(bot_id)

            giving_low = None
            giving_high = None
            if low_to_type == "bot":
                try:
                    BOTS[low_to_id]
                except KeyError:
                    BOTS[low_to_id] = Bot(low_to_id)
                giving_low = BOTS[low_to_id]
            elif low_to_type == "output":
                try:
                    OUTPUTS[low_to_id]
                except KeyError:
                    OUTPUTS[low_to_id] = Bin(low_to_id)
                giving_low = OUTPUTS[low_to_id]

            if high_to_type == "bot":
                try:
                    BOTS[high_to_id]
                except KeyError:
                    BOTS[high_to_id] = Bot(high_to_id)
                giving_high = BOTS[high_to_id]
            elif high_to_type == "output":
                try:
                    OUTPUTS[high_to_id]
                except KeyError:
                    OUTPUTS[high_to_id] = Bin(high_to_id)
                giving_high = OUTPUTS[high_to_id]

            BOTS[bot_id].giving(giving_low, giving_high)

    for line in value_lines:
        res = re.match(r'value ([0-9]+) goes to bot ([0-9]+)', line)
        if res:
            id_of_dest = res.group(2)
            try:
                BOTS[id_of_dest]
            except KeyError:
                BOTS[id_of_dest] = Bot(id_of_dest)

            BOTS[id_of_dest].push(int(res.group(1)))

    mult = 1
    for output in OUTPUTS.values():
        print(output.id)
        if output.id == '0' or output.id == '1' or output.id == '2':
            mult *= output.micros[0]

    print(mult)

























