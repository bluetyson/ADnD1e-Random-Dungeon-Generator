import os
import json
import numpy as numpy
import pandas as pd
import random
import time
import datetime
import copy
import json
from tqdm import tqdm

#pass location?
def coord_limits(dungeon):
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    minz = 0
    maxz = 0

    for key in dungeon:
        if key[0] > maxx:
            maxx = key[0]
        if key[0] < minx:
            minx = key[0]
        if key[1] > maxy:
            maxy = key[1]
        if key[1] < miny:
            miny = key[1]
        if key[2] > maxz:
            maxz = key[2]

    coord_min = (minx,miny,minz)
    coord_max = (maxx,maxy,maxz)

    ##make arrrays for each level

def random_check():
    pc_dict = {}
    pc = roll_dice(1,20)
    if pc <= 2:
        pc_dict['direction'] = 'ahead'
        pc_dict['check'] = 6
    elif pc >= 3 and pc <= 5:
        pc_dict['direction'] = 'exit'
        pc_dict['check'] = 6
    elif pc >= 6 and pc <= 10:
        pc_dict['direction'] = 'side'
        pc_dict['check'] = 3
    elif pc >= 11 and pc <= 13:
        pc_dict['direction'] = 'turn'
        pc_dict['check'] = 3
    elif pc >= 14 and pc <= 16:
        pc_dict['direction'] = 'side'
        pc_dict['check'] = 3
    elif pc == 17:
        pc_dict['direction'] = 'level'
        pc_dict['check'] = 'up_down'
    elif pc == 18:
        pc_dict['direction'] = 'stop'
        pc_dict['check'] = 'spy_things'
    elif pc == 19:
        pc_dict['direction'] = 'bad_things'
        pc_dict['check'] = 3
    elif pc == 20:
        pc_dict['direction'] = 'random_encounter'
        pc_dict['check'] = 'roll_again'

        return pc_dict

def check_action(pc_dict):
    pass
    return 0

#need data structure
#do we have an exit order stack?
#array of corridors and walls, where corridor can be room/staircase etc odd corridor, even wall
#how big a fake canvas to make - or do we just have a dictionary and add parts in as they go
#eg have 1000 x 1000 and fake easting and northing
#direction preference - n,w,e,s?

PERIODIC_CHECKS = 10  #number of rolls to make before stopping algorithm  #don't count first one down
#make this a script argument
START_LEVEL = 0

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

exit_stack = {}  #only non-dead ends etc?
door_stack= {}
level_stack = {}

dungeon = {}
dungeon[(0,0,0)] = {}
dungeon[(0,0,0)]['direction'] = 'level'
dungeon[(0,0,0)]['check'] = 'up_down'
dungeon[(0,0,0)]['go'] = -1

START_COORD = (0,0,-1)

roll_first = random_check()
while roll_first == 18:
    roll_first = random_check()





   
    