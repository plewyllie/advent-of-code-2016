FILE = 'input.txt'
DEBUG_INPUT = "qzmt-zixmtkozy-ivhz-343[zimth]\na-b-c-d-e-f-g-h-25[abcde]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]"
DEBUG = False

import collections
import re

def init(file):
    with open(file) as f:
        # this will return a list containining all the instructions
        input = f.read()
    return input

class InvalidRoomException(Exception):
    pass
class Room:
    def __init__(self, roomlist, checksum, sector_id):
        self.d = collections.defaultdict(int)
        self.sector_id = sector_id
        self.roomlist = roomlist

        roomstr = [item for sublist in roomlist for item in sublist]
        for c in roomstr:
            self.d[c] += 1

        sumlist = [v[0] for v in sorted(self.d.items(), key=lambda kv: (-kv[1], kv[0]))]
        if ''.join(sumlist[:5]) != checksum:
            raise InvalidRoomException

    def get_room_name(self):
        self.name = ""
        for n in self.roomlist:
            sub = ""
            for c in n:
                nchar = chr((((ord(c) - 96) + self.sector_id) % 26) + 96)
                if nchar == '`':
                    nchar = 'z'
                sub += nchar
            self.name += sub + " "
        return self.name


if __name__ == '__main__':
    if DEBUG:
        inputd = DEBUG_INPUT
    else:
        inputd = init(FILE)

    inputd_list = [room.split("-") for room in inputd.splitlines()]

    sector_id_sum = 0

    for room in inputd_list:
        try:
            r = Room(room[:len(room) - 1], 
                re.search(r'\[(.*)\]', room[-1]).group(1),
                int(room[-1].split("[")[0]))

            sector_id_sum += r.sector_id
            room_name = r.get_room_name()
            if room_name.startswith("northpole"):
                print(room_name)
                print(r.sector_id)

        except InvalidRoomException:
            pass

    #print("Sector ID sum = " + str(sector_id_sum))
