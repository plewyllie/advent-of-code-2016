#!/usr/bin/env python3
"""--- Day 7: Internet Protocol Version 7 ---"""

FILE = 'input.txt'
DEBUG_INPUT = "zazbz[bzb]cdb"

DEBUG = False

import regex as re

def init(file):
    with open(file) as f:
        input = f.read()
    return input

def str_has_ABBA(s):
    res = re.search(r'(.)(?!\1)(.)\2\1', s)
    if res:
        return res.group()
    else:
        return False

def str_has_ABA(s):
    res = [m.group() for m in re.finditer(r'(.)(?!\1)(.)\1', s, overlapped=True)]
    if res:
        print("Matched")
        print(res)
        return res
    else:
        return False

def str_has_BAB(s, aba):
    bab = aba[1] + aba[0] + aba[1]
    if bab in s:
        return True
    else:
        return False

class IPv7:

    def __init__(self, ipv7str):
        print(" NEW IP " + ipv7str)
        self.ipv7str = ipv7str
        iterator = re.finditer(r'\[.*?\]', ipv7str)
        start = 0
        self.tls = False
        self.ssl = False

        supernets = []
        hypernets = []

        for patt in iterator:
            str1 = ipv7str[start:patt.start()]
            str2 = ipv7str[patt.start() + 1:patt.end() - 1] # avoid []
            start = patt.end()
            supernets.append(str1)
            hypernets.append(str2)
        supernets.append(ipv7str[start:])

        print(supernets)
        print(hypernets)

        abas = []
        for supernet in supernets:
            if str_has_ABBA(supernet):
                self.tls = True

            aba = str_has_ABA(supernet)
            if aba:
                abas += aba

        print("Testing for abas:")
        print(abas)
        for aba in abas:
            for hypernet in hypernets:
                if str_has_BAB(hypernet, aba):
                    self.ssl = True

        for hypernet in hypernets:
            if str_has_ABBA(hypernet):
                self.tls = False


        #if aba and str_has_BAB(str2, aba):
            #   self.ssl = True

    def tls_support(self):
        return self.tls
    def ssl_support(self):
        return self.ssl
        


if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    inputd_lines = inputd.splitlines()

    tls_support_nb = 0
    ssl_support_nb = 0
    for line in inputd_lines:
        ipv7 = IPv7(line)
        if ipv7.tls_support() == True:
            print("IPv7 " + ipv7.ipv7str +  " supports TLS")
            tls_support_nb += 1
        if ipv7.ssl_support() == True:
            print("IPv7 " + ipv7.ipv7str +  " supports SSL")
            ssl_support_nb += 1


    print("There are " + str(tls_support_nb) + " IPv7 supporting TLS")
    print("There are " + str(ssl_support_nb) + " IPv7 supporting SSL")



