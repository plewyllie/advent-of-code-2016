#!/usr/bin/env python3
"""--- Day 14: One-Time Pad, part 2 using multithreading ---"""

import hashlib
import re
import multiprocessing

SALT = "ahsbgdzn"
RANGE = 35000
GATHERED_KEYS_INDEX = multiprocessing.Value('i', 0)
GATHERED_KEYS = multiprocessing.Array('i', [999999] * RANGE) # used by the threads
processLock = multiprocessing.Lock()

def hash_stretching(hashstr, stretch_count):
    for _ in range(0, stretch_count):
        hashstr = hashlib.md5(hashstr.encode('utf-8')).hexdigest()
    #print("Hash is", hashstr)
    return hashstr

def md5_contains_five_keys(index, key):
    md5_str = hashlib.md5()
    md5_str.update((SALT + str(index)).encode('utf-8'))

    hashstr = hash_stretching(md5_str.hexdigest(), 2016)

    # checking for five keys
    if re.search(r'({})\1\1\1\1'.format(key), hashstr):
        return True
    return False

def md5_is_key(index):
    print("Starting md5_is_key for index", index)
    md5_str = hashlib.md5()
    md5_str.update((SALT + str(index)).encode('utf-8'))
    hashstr = hash_stretching(md5_str.hexdigest(), 2016)
    # checking for triplet
    triplet_match = re.finditer(r'([0-9a-z])\1\1', hashstr)
    for triplet in triplet_match:
        for i in range(index + 1, index + 1001):
            if md5_contains_five_keys(i, triplet.group(1)):
                #print(triplet.group())
                #print(md5_str.hexdigest())
                processLock.acquire()
                print("inserting", GATHERED_KEYS, index)
                #bisect.insort(GATHERED_KEYS, self.index)
                GATHERED_KEYS[GATHERED_KEYS_INDEX.value] = index
                global GATHERED_KEYS_INDEX
                GATHERED_KEYS_INDEX.value += 1
                processLock.release()
                return True
        break # didn't read instructions correctly, we should only consider first triplet
    return False

if __name__ == '__main__':
    threads = []

    with multiprocessing.Pool(processes=3) as pool:
        pool.map(md5_is_key, range(RANGE))
    try:
        print(sorted(GATHERED_KEYS[:]))
        print(GATHERED_KEYS[63]) # printing 64th key
    except IndexError:
        print("There is no index 63, the search range is too small or impossible problem")
