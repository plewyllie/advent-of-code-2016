#!/usr/bin/env python3
"""--- Day 14: One-Time Pad, part1 using multithreading ---"""

import hashlib
import re
import threading
import bisect

SALT = "abc"
GATHERED_KEYS = [] # used by the threads
threadLock = threading.Lock()

class Md5Computer(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        print ("Starting thread with index " + str(self.index))
        if md5_is_key(self.index):
            threadLock.acquire()
            bisect.insort(GATHERED_KEYS, self.index)
            threadLock.release()

def md5_contains_five_keys(index, key):
    md5_str = hashlib.md5()
    md5_str.update((SALT + str(index)).encode('utf-8'))
    # checking for five keys
    if re.search(r'({})\1\1\1\1'.format(key), md5_str.hexdigest()):
        #print(md5_str.hexdigest())
        return True
    return False

def md5_is_key(index):
    md5_str = hashlib.md5()
    md5_str.update((SALT + str(index)).encode('utf-8'))
    # checking for triplet
    triplet_match = re.finditer(r'([0-9a-z])\1\1', md5_str.hexdigest())
    for triplet in triplet_match:
        for i in range(index + 1, index + 1001):
            if md5_contains_five_keys(i, triplet.group(1)):
                #print(triplet.group())
                #print(md5_str.hexdigest())
                return True
        break # didn't read instructions correctly, we should only consider first triplet
    return False

if __name__ == '__main__':
    threads = []
    for index in range(0, 25000): # choose a range big enough
        thread = Md5Computer(index)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join() # waiting for all threads to finish
    try:
        print(GATHERED_KEYS)
        print(GATHERED_KEYS[63]) # printing 64th key
    except IndexError:
        print("There is no index 64, the search range is too small or impossible problem")
