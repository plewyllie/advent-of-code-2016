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

def str_has_ABA(s):
    res = re.search(r'(.)(?!\1)(.)\1', s)
    if DEBUG:
        print("matching on " + s)
    if res:
        print("Matched " + res.group())
        return res.group()
    else:
        return False

def str_has_BAB_(s, bab):
    pass

class IPv7:

    def __init__(self, ipv7str):
        print(" NEW IP " + ipv7str)
        self.ipv7str = ipv7str
        iterator = re.finditer(r'\[.*?\]', ipv7str)
        start = 0
        self.tls = False

        supernets = []
        hypernets = []

        for patt in iterator:
            str1 = ipv7str[start:patt.start()]
            str2 = ipv7str[patt.start() + 1:patt.end() - 1] # avoid []
            start = patt.end()
            supernets.append(str1)
            hypernets.append(str2)
        supernets.append(ipv7str[start:])

        for supernet in supernets:
            if str_has_ABBA(supernet):
                self.tls = True
        for hypernet in hypernets:
            if str_has_ABBA(hypernet):
                self.tls = False

            #if aba and str_has_BAB(str2, aba):
             #   self.ssl = True

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


