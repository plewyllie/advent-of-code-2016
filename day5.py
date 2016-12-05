#!/usr/bin/env python3

"""Day 5: How About a Nice Game of Chess?"""

import hashlib
import sys
import random
import threading
import time
import _thread

PSSWD = ['_'] * 8
INDEX = 0
FLICKERING = ['_', '\\', '?']
K = 0
sema = threading.BoundedSemaphore(1)

def md5str(x):
    md5_str = hashlib.md5()
    md5_str.update(x.encode('utf-8'))
    return md5_str.hexdigest()

def flickerpw():
    for i, _ in enumerate(PSSWD):
        if PSSWD[i] in FLICKERING:
            PSSWD[i] = random.choice(FLICKERING)
    if not sema.acquire(False):
        exit()
    sys.stdout.write("Decrypting psswd:%s at index %d \r" % (''.join(PSSWD), INDEX))
    sys.stdout.flush()
    sema.release()

def flickerpw_thread():
    while True:
        flickerpw()
        time.sleep(.4)

if __name__ == "__main__":
    doorid = "uqwqemis"

    try:
        tr = _thread.start_new_thread(flickerpw_thread, ())
    except:
        print("Error: unable to start flickering thread")
        exit()
    while K < 8:
        md5 = md5str(doorid + str(INDEX))
        INDEX += 1
        if md5.startswith("00000"):
            try:
                pos = int(md5[5])
            except ValueError:
                continue
            if pos >= 0 and pos < 8 and PSSWD[pos] in FLICKERING:
                PSSWD[pos] = md5[6]
                K += 1
                flickerpw()

    sema.acquire()
    print("DECRYPTED. PSSWD is " + ''.join(PSSWD))
