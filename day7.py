#!/usr/bin/env python3
"""--- Day 7: Internet Protocol Version 7 ---"""

FILE = 'input.txt'
DEBUG_INPUT = "epmnxkubnsnykyubv[ydzhcoytayiqmxlv]edmbahbircojbkmrg[dlxyprugefqzkum]svdaxilkrkukfg[eacekyzjchfpzghltn]ofwgevwnnwhoivrevueaj\nabba[mnop]qrst\naabcd[bddb]xyyx\naaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn\nifoxxorj[asoxxodfgh]zxoxxocvbn\nvjqhodfzrrqjshbhx[lezezbbswydnjnz]ejcflwytgzvyigz[hjdilpgdyzfkloa]mxtkrysovvotkuyekba"
DEBUG = False

import re

def init(file):
    with open(file) as f:
        input = f.read()
    return input

def str_has_ABBA(s):
    res = re.search(r'(.)(?!\1)(.)\2\1', s)
    if DEBUG:
        print("matching on " + s)
    if res:
        print("Matched " + res.group())
        return res.group()
    else:
        return False

class IPv7:

    def __init__(self, ipv7str):
        print(" NEW IP " + ipv7str)
        self.ipv7str = ipv7str
        iterator = re.finditer(r'\[.*?\]', ipv7str)
        start = 0
        no_hypernet = True
        self.tls = False
        for patt in iterator:
            str1 = ipv7str[start:patt.start()]
            str2 = ipv7str[patt.start() + 1:patt.end() - 1] # avoid []

            if str_has_ABBA(str2):
                self.tls = False
                no_hypernet = False
                break
            elif str_has_ABBA(str1):
                self.tls = True

            start = patt.end()

        if no_hypernet and str_has_ABBA(ipv7str[start:]):
            self.tls = True


    def tls_support(self):
        return self.tls
        


if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    inputd_lines = inputd.splitlines()

    tls_support_nb = 0
    for line in inputd_lines:
        ipv7 = IPv7(line)
        if ipv7.tls_support() == True:
            print("IPv7 " + ipv7.ipv7str +  " supports TLS")
            tls_support_nb += 1
    print("There are " + str(tls_support_nb) + " IPv7 supporting TLS")


