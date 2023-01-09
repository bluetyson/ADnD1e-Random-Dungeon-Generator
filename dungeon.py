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
def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

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

    return [coord_min, coord_max]

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
        pc_dict['direction'] = 'room'
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

    print("RANDOM_CHECK",pc, pc_dict['direction'])



    return pc_dict

def check_action(pc_dict, coord):
    if pc_dict['direction'] == 'ahead':
        new_coord = (coord[0],coord[1]+6,coord[2])
        for y in range(6):
            dungeon[(coord[0],coord[1]+1+y,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1+y,coord[2])]['fill'] = 'C'
    elif pc_dict['direction'] == 'exit':
        new_coord = coord
        e_dict = exit(coord)
        if 'L' in e_dict:
            exit_stack[(coord[0]-1,coord[1],coord[2])] = {}
        elif 'R' in e_dict:
            exit_stack[(coord[0]+1,coord[1],coord[2])] = {}
        else:
            exit_stack[(coord[0],coord[1]+1,coord[2])] = {}

    elif pc_dict['direction'] == 'side':
        new_coord = coord
        s_dict = side(coord)
        if s_dict['direction'] == 'L90':
            for x in range(3):
                dungeon[(coord[0]-1-x,coord[1],coord[2])] = {}
                dungeon[(coord[0]-1-x,coord[1],coord[2])]['fill'] = 'C'

        elif s_dict['direction'] == 'R90':
            for x in range(3):
                dungeon[(coord[0]+1+x,coord[1],coord[2])] = {}
                dungeon[(coord[0]+1+x,coord[1],coord[2])]['fill'] = 'C'

        elif s_dict['direction'] == 'L45':
            pass
        elif s_dict['direction'] == 'R45':
            pass
        elif s_dict['direction'] == 'L135':
            pass
        elif s_dict['direction'] == 'R135':
            pass
        elif s_dict['direction'] == 'L45':
            pass
        elif s_dict['direction'] == 'R45':
            pass
        elif s_dict['direction'] == 'T':
            pass
        elif s_dict['direction'] == 'Y':
            pass
        elif s_dict['direction'] == 'P':
            pass
        else:
        #s_dict['direction'] == 'X':
            pass

        

    elif pc_dict['direction'] == 'turn':
        new_coord = coord
        pass
    elif pc_dict['direction'] == 'room':
        new_coord = coord
        pass
    elif pc_dict['direction'] == 'level':
        new_coord = coord
        pass
    elif pc_dict['direction'] == 'stop':
        new_coord = coord
        pass
    elif pc_dict['direction'] == 'bad_things':
        new_coord = coord
        pass
    elif pc_dict['direction'] == 'random_encounter':
        new_coord = coord
        pass

    return new_coord

def exit(coord):
    e_dict = {}
    d = roll_dice(1,20)
    if d <= 6:
        e_dict['direction'] = 'L'
        e_dict['coord'] = (coord[0]-1,coord[1],coord[2])

    elif d>=7 and d <= 12:
        e_dict['direction'] = 'R'
        e_dict['coord'] = (coord[0]+1,coord[1],coord[2])
    else:
        e_dict['direction'] = 'A'
        e_dict['coord'] = (coord[0],coord[1]+1,coord[2])

    b = roll_dice(1,20)
    if b <= 4:
        e_dict['beyond'] = 'P'
    elif d>=5 and d <= 8:
        e_dict['beyond'] = 'A'
    elif d==9:
        e_dict['beyond'] = '4AB'
    elif d==10:
        e_dict['beyond'] = '4BA'
    else:
        e_dict['beyond'] = 'Room'

    exit_stack[coord] = e_dict

    return e_dict


def side(coord):
    s_dict = {}
    s = roll_dice(1,20)
    if s <= 2:
        s_dict['direction'] = 'L90'
    if s <= 3 and s <= 4:
        s_dict['direction'] = 'R90'
    if s <= 5 :
        s_dict['direction'] = 'L45'
    if s <= 6 :
        s_dict['direction'] = 'R45'
    if s <= 7 :
        s_dict['direction'] = 'L135'
    if s <= 8 :
        s_dict['direction'] = 'R135'
    if s <= 9 :
        s_dict['direction'] = 'L45'
    if s <= 10 :
        s_dict['direction'] = 'R45'
    if s <= 11 and s <= 13:
        s_dict['direction'] = 'T'
    if s <= 14 and s <= 15:
        s_dict['direction'] = 'Y'
    if s <= 16 and s <= 19:
        s_dict['direction'] = 'P'
    if s == 20:
        s_dict['direction'] = 'X'

    return s_dict

def turn(coord):
    pass

def room(coord):
    pass

def width():
    pass

def fancy_width():
    pass
def fancy_shape():
    pass
def fancy_size():
    pass

def exit_no():
    pass
def exit_loc():
    pass
def exit_dir():
    pass

def room_contents():
    pass

def loot():
    pass

def loot_store():
    pass

def loot_guard():
    pass

def loot_hide():
    pass

def level():
    pass

def bad_things():
    pass

def fancy_cave():
    pass

def wet_small():
    pass

def wet_large():
    pass

def wet_magic():
    pass

def stinky():
    pass

#need data structure
#do we have an exit order stack?
#array of corridors and walls, where corridor can be room/staircase etc odd corridor, even wall
#how big a fake canvas to make - or do we just have a dictionary and add parts in as they go
#eg have 1000 x 1000 and fake easting and northing
#direction preference - n,w,e,s?

PERIODIC_CHECKS = 1  #number of rolls to make before stopping algorithm  #don't count first one down
#make this a script argument
START_LEVEL = 0


exit_stack = {}  #only non-dead ends etc?
door_stack= {}
level_stack = {}

dungeon = {}
dungeon[(0,0,0)] = {}
dungeon[(0,0,0)]['direction'] = 'level'
dungeon[(0,0,0)]['check'] = 'up_down'
dungeon[(0,0,0)]['go'] = -1

START_COORD = (0,0,-1)
coord = START_COORD

roll_first = random_check()
while roll_first == 18:
    roll_first = random_check()

print("roll_first", roll_first)
first_action = check_action(roll_first, coord)    

i = 0
result_coord = first_action

while i < PERIODIC_CHECKS:
    print("ROLL:",i)
    roll_first = random_check()
    result_coord = check_action(roll_first, result_coord)
    i +=1

print(coord)
print(dungeon)
print(exit_stack)





   
    