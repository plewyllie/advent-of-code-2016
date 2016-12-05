import hashlib
import sys
import random
import _thread
import threading
import time

PSSWD = ['_'] * 8
INDEX = 0
FLICKERING = ['_', '\\', '?']
K = 0
sema = threading.BoundedSemaphore(1)


def md5str(x):
    m = hashlib.md5()
    m.update(x.encode('utf-8'))
    return m.hexdigest()

def flickerpw():
    for i in range(0,len(PSSWD)):
        if PSSWD[i] in FLICKERING:
            PSSWD[i] = random.choice(FLICKERING)
    
    if not sema.acquire(False):
        exit()
    
    sys.stdout.write("Decrypting psswd:%s at index %d \r" % (''.join(PSSWD), INDEX) )
    sys.stdout.flush()

    sema.release()


def flickerpw_thread():
    while True:
        flickerpw()
        time.sleep(.4)

if __name__ == "__main__":
    doorid = "uqwqemis"

    try:
        tr = _thread.start_new_thread( flickerpw_thread, () )
    except:
        print ("Error: unable to start flickering thread")
        exit()
    while K < 8:
        md5 = md5str(doorid + str(INDEX))
        if md5[:5] == "00000":
            try:
                pos = int(md5[5])
            except ValueError:
                INDEX += 1
                continue
            if pos >= 0 and pos < 8:
                if PSSWD[pos] in FLICKERING:
                    PSSWD[pos] = md5[6]
                    K += 1
                    flickerpw()
        INDEX += 1

    sema.acquire()
    print("DECRYPTED. PSSWD is " + ''.join(PSSWD))




