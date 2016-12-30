#!/usr/bin/env python3
"""--- Day 13: A Maze of Twisty Little Cubicles ---"""

FILE = 'input.txt'

DEBUG = True
MAGIC_NUMBER = 10

MAZE = {}

MAZE_COLS = 10
MAZE_LINES = 10
DEST_X = 4
DEST_Y = 7

import numpy as np

class Node:
    def __init__(self, x, y):
        self.dist = 9999999 # dijkstra high value
        self.x = x
        self.y = y

    def is_wall(self):
        formula = self.y*self.y + 3*self.y + 2*self.y*self.x + self.x + self.x*self.x
        global MAGIC_NUMBER
        formula += MAGIC_NUMBER
        if bin(formula)[2:].count('1') % 2 == 0:
            print(self.x, self.y, "Is not a Wall!")
            return False

        print(self.x, self.y, "Is a Wall!")
        return True

    def set_dijkstra_dist(self, dist):
        self.dist = dist

    def check_neighbor(self, neighb_x, neighb_y):
        global MAZE
        if neighb_x < 0 or neighb_y < 0:
            return
        if neighb_x >= MAZE_LINES or neighb_y >= MAZE_COLS:
            return
        if (not(MAZE[neighb_x][neighb_y].is_wall())
            and (MAZE[neighb_x][neighb_y].dist > self.dist + 1)):
            print("I am ", self.x, self.y)
            print("Setting dist for ", neighb_x, neighb_y, "to", self.dist + 1)
            MAZE[neighb_x][neighb_y].dist = self.dist + 1

    def check_neighbors(self):
        neighb_x = self.x
        neighb_y = self.y
        #print("I am ", self.x, self.y)
        #print("Checking neighbors", neighb_x + 1, neighb_y)
        #print("Checking neighbors", neighb_x - 1, neighb_y)
        #print("Checking neighbors", neighb_x, neighb_y + 1)
        #print("Checking neighbors", neighb_x, neighb_y - 1)

        self.check_neighbor(neighb_x + 1, neighb_y)
        self.check_neighbor(neighb_x - 1, neighb_y)
        self.check_neighbor(neighb_x, neighb_y + 1)
        self.check_neighbor(neighb_x, neighb_y - 1)


def init(file):
    with open(file) as f:
        input = f.read()
    return input

if __name__ == '__main__':
    MAZE = [[Node(x,y) for y in range(MAZE_COLS)] for x in range(MAZE_COLS)]
    MAZE[1][1].dist = 0 # starting square, distance is 0

    # make list of unvisited nodes and remove walls
    unvisited = {x for sublist in MAZE for x in sublist if not x.is_wall()}
    # dijkstra
    cur_node = MAZE[1][1]
    while not(cur_node.x == DEST_X and cur_node.y == DEST_Y):
        min_dist = 9999999
        for node in unvisited:
            if node.dist < min_dist:
                cur_node = node
                min_dist = cur_node.dist

        if len(unvisited) == 0 or min_dist == 9999999:
            print("Could not solve the challenge")
            exit()

        cur_node.check_neighbors()
        unvisited.remove(cur_node)
        print("Distance to",cur_node.x,",",cur_node.y,"is",cur_node.dist)

    print("Distance to",cur_node.x,",",cur_node.y,"is",cur_node.dist)









    












