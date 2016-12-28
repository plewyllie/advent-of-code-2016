#!/usr/bin/env python3
"""--- Day 11: Radioisotope Thermoelectric Generators ---"""

DEBUG = False

class InvalidState(Exception):
    pass

class State:
    # Elevator should be an integer reprensenting Elevator floor #
    # state_array should represent represent the following
    # < MicrochipFloor, MicrochipGeneratorFloor, DifferentMCFloor, DifferentMCGeneratorFloor... >
    def __init__(self, elevator, state_array, nb_steps):
        self.e = elevator
        self.s = state_array
        self.n = nb_steps

        if not (self.valid()):
            raise InvalidState


    def __eq__(self, other):
        if self.e != other.e:
            return False
        if self.s != other.s:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def valid(self):
        if not 1 <= self.e <= 4:
            return False

        if self.e < 1 or self.e > 4:
            return False

        for chip, gen in zip(self.s[::2], self.s[1::2]):
            if chip < 1 or chip > 4 or gen < 1 or gen > 4:
                return False
            if (chip != gen) and any(chip == gen for gen in self.s[1::2]):
                return False

        return True

    def resolved(self):
        if self.s == [4 for x in self.s]:
            return True

    def normalize(self):
        # compute the number of chips on a given floor
        c = [sum(1 for v in self.s[::2] if v == fn) for fn in range(1, 5)]
        # compute the number of generators on a given floor
        g = [sum(1 for v in self.s[1::2] if v == fn) for fn in range(1, 5)]
        return ''.join([str(x) for x in c + g]) + str(self.e)


if __name__ == '__main__':
    states_q = [State(1, [1,1,1,1,2,2,2,2,3,2,1,1,1,1], 0)]
    visited = set() # remember visited states to avoid looping
    while len(states_q) > 0:
        s = states_q.pop(0)
        
        if s.normalize() in visited: # we don't revisit visited states
            continue
        visited.add(s.normalize())

        state_array = s.s

        if s.resolved():
            print("resolved in ", s.n, "nb_steps")
            exit()

        for i in range(len(state_array)):
            if s.e != state_array[i]:
                continue # cannot move because not in elevator

            # moving only 1 object
            state_array[i] += 1 # going up one floor
            try:
                states_q.append(State(s.e + 1, list(state_array), s.n + 1))
            except InvalidState:
                #print("State ", state_array, "is invalid")
                pass

            state_array[i] -= 2 # going down one floor
            try:
                states_q.append(State(s.e - 1, list(state_array), s.n + 1))
            except InvalidState:
                #print("State ", state_array, "is invalid")
                pass
            state_array[i] += 1

            # moving two objects
            for j in range (i + 1, len(state_array)):
                if s.e != state_array[j]:
                    continue # cannot move because not in elevator

                state_array[i] -= 1
                state_array[j] -= 1
                try:
                    states_q.append(State(s.e - 1, list(state_array), s.n + 1)) # floor + 1
                except InvalidState:
                    #print("State ", state_array, "is invalid")
                    pass
                state_array[i] += 2
                state_array[j] += 2
                try:
                    states_q.append(State(s.e + 1, list(state_array), s.n + 1)) # floor -1
                except InvalidState:
                    #print("State ", state_array, "is invalid")
                    pass
                state_array[i] -= 1
                state_array[j] -= 1


















