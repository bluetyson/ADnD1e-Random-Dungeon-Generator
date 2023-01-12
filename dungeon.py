import os
import json
import numpy as np
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

def in_dungeon(coord):
    inside = False
    if coord in dungeon:
        inside = True
    return inside

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

    #test purposes
    #pc_dict['direction'] = 'ahead'

    return pc_dict

def check_action(pc_dict, coord):
    ## need a current 'orientation' 'L R A B
    if pc_dict['direction'] == 'ahead':
        will_fit = True
        new_coord = coord
        for y in range(pc_dict['check']):

            will_fit = in_dungeon((coord[0],coord[1]+1+y,coord[2]))
            #print("Y",y, "WILLFIT:",will_fit)
            if not will_fit:
                dungeon[(coord[0],coord[1]+1+y,coord[2])] = {}
                dungeon[(coord[0],coord[1]+1+y,coord[2])]['fill'] = 'C'
                #handle not fitting
                new_coord = (coord[0],coord[1]+1+y,coord[2])
            else:
                break
    elif pc_dict['direction'] == 'exit':
        '''
            e_dict['beyond'] = 'P'
            e_dict['beyond'] = 'A'
            e_dict['beyond'] = '4AB'
            e_dict['beyond'] = '4BA'
            e_dict['beyond'] = 'Room'
        '''
        new_coord = coord
        e_dict = exit(coord)
        print("EDICT:",e_dict)
        if e_dict['direction'] == 'L':
            if e_dict['type'] == 'N':
                exit_stack[(coord[0]-1,coord[1],coord[2])] = {}
                if e_dict['beyond'] == 'P':
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1,coord[1]+x-1,coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]-1,coord[1]+x-1,coord[2])] = {}
                            dungeon[(coord[0]-1,coord[1]+x-1,coord[2])]['fill'] = 'C'
                            new_coord = (coord[0]-1,coord[1]+x-1,coord[2])
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1,coord[1]+x+1,coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])] = {}
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'C'
                            new_coord = (coord[0]-1,coord[1]+x+1,coord[2])

                if e_dict['beyond'] == 'A':              
                    d = roll_dice(1,20)              
                    if d >=3 and d >= 5:
                        will_fit = in_dungeon((coord[0]-1,coord[1],coord[2]))
                        if not will_fit:
                            exit_stack[(coord[0]-1,coord[1],coord[2])] = {}
                    else:
                        #30m passage that direction
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-x-1,coord[1],coord[2]))
                            if not will_fit:
                                dungeon[(coord[0]-x-1,coord[1],coord[2])] = {}
                                dungeon[(coord[0]-x-1,coord[1],coord[2])]['fill'] = 'C'
                                new_coord = ((coord[0]-x-1,coord[1],coord[2]))                        


                if e_dict['beyond'] == '4AB':   ##45 A
                    which_way = roll_dice(1,2)           
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == '4BA':   ##45 A
                    which_way = roll_dice(1,2)  #work out random direction         
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]+1+-x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == 'Room':
                    #want those we randomly position lr
                    new_coord = coord
                    shape_dict = room(coord, size='R')  ## different type to get slightly different table
                    #each room part check for inside

                    print("ROOM SHAPE:",shape_dict)
                    ## do simple version first of x directions and y directions of rectangular
                    if shape_dict['shape'] == 'R':
                        print("rectangular")
                        #H x W
                        #position based on size
                        adjust = 0
                        if shape_dict['size'][1] % 2 == 0:
                            lr = roll_dice(1,2)
                            if lr == 1:
                                adjust = -1
                            else:
                                adjust = 1

                        #if shape_dict['size'][1] == 2:
                        for j in range(shape_dict['size'][1]):
                            for i in range(shape_dict['size'][0]):
                                will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]))
                                if not will_fit:                
                                    dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])] = {}
                                    dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])]['fill'] = 'R'
                                else:
                                    break
                        
                    else:
                        pass
                        #fancy shape/size not yet implemented


        elif e_dict['direction'] == 'R':
            if e_dict['type'] == 'N':
                exit_stack[(coord[0]+1,coord[1],coord[2])] = {}
                if e_dict['beyond'] == 'P':
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]+1,coord[1],coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]+1,coord[1]+x-1,coord[2])] = {}
                            dungeon[(coord[0]+1,coord[1]+x-1,coord[2])]['fill'] = 'C'
                            new_coord = (coord[0]+1,coord[1]+x-1,coord[2])
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1,coord[1]+x+1,coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])] = {}
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'C'
                            new_coord = (coord[0]-1,coord[1]+x+1,coord[2])

                if e_dict['beyond'] == 'A':              
                    d = roll_dice(1,20)              
                    if d >=3 and d >= 5:
                        will_fit = in_dungeon((coord[0]+1,coord[1],coord[2]))
                        if not will_fit:
                            exit_stack[(coord[0]+1,coord[1],coord[2])] = {}
                    else:
                        #30m passage that direction
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-x-1,coord[1],coord[2]))
                            if not will_fit:
                                dungeon[(coord[0]+x+1,coord[1],coord[2])] = {}
                                dungeon[(coord[0]+x+1,coord[1],coord[2])]['fill'] = 'C'
                                new_coord = ((coord[0]+x+1,coord[1],coord[2]))      

                if e_dict['beyond'] == '4AB':   ##45 A - need to make facing for R different eventually
                    which_way = roll_dice(1,2)           
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == '4BA':   ##45 A
                    which_way = roll_dice(1,2)  #work out random direction         
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]+1+-x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == 'Room':
                    #want those we randomly position lr
                    new_coord = coord
                    shape_dict = room(coord, size='R')  ## different type to get slightly different table
                    #each room part check for inside

                    print("ROOM SHAPE:",shape_dict)
                    ## do simple version first of x directions and y directions of rectangular
                    if shape_dict['shape'] == 'R':
                        print("rectangular")
                        #H x W
                        #position based on size
                        adjust = 0
                        if shape_dict['size'][1] % 2 == 0:
                            lr = roll_dice(1,2)
                            if lr == 1:
                                adjust = -1
                            else:
                                adjust = 1

                        #if shape_dict['size'][1] == 2:
                        for j in range(shape_dict['size'][1]):
                            for i in range(shape_dict['size'][0]):
                                will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]))
                                if not will_fit:                
                                    dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])] = {}
                                    dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])]['fill'] = 'R'
                                else:
                                    break
                        
                    else:
                        pass
                        #fancy shape/size not yet implemented


                
        else:
            if e_dict['type'] == 'N':
                exit_stack[(coord[0],coord[1]+1,coord[2])] = {}
                if e_dict['beyond'] == 'P':
                    will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))
                    if not will_fit:
                        dungeon[(coord[0],coord[1]+1,coord[2])] = {}
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'R'
                        new_coord = (coord[0],coord[1]+1,coord[2])
                        # 10 x 10 room need to check contents!

        ## got to proceed with direction/type of exit

    elif pc_dict['direction'] == 'side':
        new_coord = coord
        s_dict = side(coord)
        print("S_DICT:",s_dict)
        if s_dict['direction'] == 'L90':
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1],coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1],coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]-1-x,coord[1],coord[2])
                else:
                    break

        elif s_dict['direction'] == 'R90':
            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1],coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1],coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]+1+x,coord[1],coord[2])
                else:
                    break

        elif s_dict['direction'] == 'L45':
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                else:
                    break

        elif s_dict['direction'] == 'R45':
            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                else:
                    break

        elif s_dict['direction'] == 'L135':
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1]-1-x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                else:
                    break

        elif s_dict['direction'] == 'R135':
            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                else:
                    break

        elif s_dict['direction'] == 'T':
            which_way = roll_dice(1,2)
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1],coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1],coord[2])]['fill'] = 'C'
                    if which_way == 1:
                        new_coord = (coord[0]-1-x,coord[1],coord[2])
                else:
                    break

            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1],coord[2]))
                if not will_fit:                
                    dungeon[(coord[0]+1+x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1],coord[2])]['fill'] = 'C'
                    if which_way == 2:
                        new_coord = (coord[0]+1+x,coord[1],coord[2])
                else:
                    break

            if which_way == 1:
                new_coord = (coord[0]-3,coord[1],coord[2])  ### got to move these up
            else:
                new_coord = (coord[0]+3,coord[1],coord[2])

        elif s_dict['direction'] == 'Y':
            which_way = roll_dice(1,2)  #got to move this up
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                if not will_fit:                
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    if which_way == 1:
                        new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                else:
                    break

            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                if not will_fit:                
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    if which_way == 2:
                        new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                else:
                    break

        elif s_dict['direction'] == 'P': #plus
            which_way = roll_dice(1,3)
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1],coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1],coord[2])]['fill'] = 'C'
                    if which_way == 1:
                        new_coord = (coord[0]-1-x,coord[1],coord[2])
                else:
                    break
            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1],coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1],coord[2])]['fill'] = 'C'
                    if which_way == 2:
                        new_coord = (coord[0]+1+x,coord[1],coord[2])
                else:
                    break
            for x in range(3):
                will_fit = in_dungeon((coord[0],coord[1]+1+x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0],coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0],coord[1]+1+x,coord[2])]['fill'] = 'C'
                    if which_way == 3:
                        new_coord = (coord[0],coord[1]+1+x,coord[2])
                else:
                    break

        else:
        #s_dict['direction'] == 'X': 45 and 135
            which_way = roll_dice(1,4) ##got to move this up
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    if which_way == 1:
                        new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                else:
                    break

            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    if which_way == 2:
                        new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                else:
                    break

            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1]-1-x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                    if which_way == 3:
                        new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                else:
                    break

            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                if not will_fit:                
                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                    if which_way == 4:
                        new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                else:
                    break

    elif pc_dict['direction'] == 'turn':
        new_coord = coord
        t_dict = turn(coord)
        print("T_DICT:",t_dict)

        t = roll_dice(1,20)
        if t_dict['direction'] == 'L90':
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1],coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1],coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]-1-x,coord[1],coord[2])
                else:
                    break

        elif t_dict['direction'] == 'L45':
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                else:
                    break

        elif t_dict['direction'] == 'L135':
            for x in range(3):
                will_fit = in_dungeon((coord[0]-1-x,coord[1]-1-x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                else:
                    break

        elif t_dict['direction'] == 'R90':
            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1],coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1],coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1],coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]+1+x,coord[1],coord[2])
                else:
                    break

        elif t_dict['direction'] == 'R45':
            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                else:
                    break

        else: # 'R135'
            for x in range(3):
                will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                if not will_fit:
                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                else:
                    break

        
    elif pc_dict['direction'] == 'room':
        '''
            lr = roll_dict(1,2)
            shape_dict['size'] = [2,2]
            shape_dict['size'] = [4,4]
            shape_dict['size'] = [1,2]
            shape_dict['size'] = [2,4]
            shape_dict['size'] = [4,6]
            shape_dict['size'] = [3,4]
            
            others
            shape_dict['size'] = [1,1]
            shape_dict['size'] = [3,3]
            shape_dict['size'] = [2,3]
            shape_dict['size'] = [2,3]
            shape_dict['size'] = [3,5]
    
            shape_dict = fancy_shape()
        '''
        #want those we randomly position lr
        new_coord = coord
        shape_dict = room(coord) #if another room pass not C="R"        
        #each room part check for inside

        print("ROOM SHAPE:",shape_dict)
        ## do simple version first of x directions and y directions of rectangular
        if shape_dict['shape'] == 'R':
            print("rectangular")
            #H x W
            #position based on size
            adjust = 0
            if shape_dict['size'][1] % 2 == 0:
                lr = roll_dice(1,2)
                if lr == 1:
                    adjust = -1
                else:
                    adjust = 1

            #if shape_dict['size'][1] == 2:
            for j in range(shape_dict['size'][1]):
                for i in range(shape_dict['size'][0]):
                    will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]))
                    if not will_fit:                
                        dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])] = {}
                        dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])]['fill'] = 'R'
                    else:
                        break
            
        else:
            pass
            #fancy shape/size

    elif pc_dict['direction'] == 'level':
        new_coord = coord
        level_dict = level(coord)
        new_coord = level_dict['new_coord']
        level_stack[new_coord] = level_dict
        
        if level_dict['check'] > 0:
            #go ahead 3 on check 3
            for y in range(level_dict['check']):
                will_fit = in_dungeon((coord[0],coord[1]+1+y,coord[2]))
                if not will_fit:
                    dungeon[(coord[0],coord[1]+1+y,coord[2])] = {}
                    dungeon[(coord[0],coord[1]+1+y,coord[2])]['fill'] = 'C'
                    new_coord = (coord[0],coord[1]+1+y,coord[2])
                else:
                    break


        if level_dict['room'] == 'Y':
            #do room check

            ## need to put roominess like this in a function?? as still need all exits and other stuff - maybe go in shape_dict??
            shape_dict = room(coord) #if another room pass not C="R"        
            #each room part check for inside

            print("ROOM SHAPE:",shape_dict)
            ## do simple version first of x directions and y directions of rectangular
            if shape_dict['shape'] == 'R':
                print("rectangular")
                #H x W
                #position based on size
                adjust = 0
                if shape_dict['size'][1] % 2 == 0:
                    lr = roll_dice(1,2)
                    if lr == 1:
                        adjust = -1
                    else:
                        adjust = 1

                #if shape_dict['size'][1] == 2:
                for j in range(shape_dict['size'][1]):
                    for i in range(shape_dict['size'][0]):
                        will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])] = {}
                            dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])]['fill'] = 'R'
                        else:
                            break
                
            else:
                pass
                #fancy shape/size
        return new_coord

    elif pc_dict['direction'] == 'stop':
        new_coord = coord
        check_coord_L = (new_coord[0]-1,new_coord[1],new_coord[2])
        check_coord_R = (new_coord[0]+1,new_coord[1],new_coord[2])
        check_coord_A = (new_coord[0],new_coord[1]+1,new_coord[2])

        dead_end = True
        if check_coord_L not in dungeon:
            ## need to check if in dungeons where putting Ds
            e_dict_f = fancy_exit(coord)
            if 'S' in e_dict_f:
                e_dict = {}
                e_dict['direction'] = 'L'
                e_dict['coord'] = (coord[0]-1,coord[1],coord[2])
                e_dict['type'] = e_dict_f['type']
                exit_stack[coord] = e_dict
                dead_end = False
        if check_coord_R not in dungeon:
            ## need to check if in dungeons where putting Ds
            e_dict_f = fancy_exit(coord)
            if 'S' in e_dict_f:
                e_dict = {}
                e_dict['direction'] = 'R'
                e_dict['coord'] = (coord[0]+1,coord[1],coord[2])
                e_dict['type'] = e_dict_f['type']
                exit_stack[coord] = e_dict
                dead_end = False
        if check_coord_A not in dungeon:
            ## need to check if in dungeons where putting Ds
            e_dict_f = fancy_exit(coord)
            if 'S' in e_dict_f:
                e_dict = {}
                e_dict['direction'] = 'R'
                e_dict['coord'] = (coord[0],coord[1]+1,coord[2])
                e_dict['type'] = e_dict_f['type']
                exit_stack[coord] = e_dict
                dead_end = False

        #this will also need checking
        if dead_end == True:
            dungeon[new_coord[0],new_coord[1]+1,new_coord[2]] = {}
            dungeon[new_coord[0],new_coord[1]+1,new_coord[2]]['fill'] = 'D'
            dungeon[new_coord[0]-1,new_coord[1],new_coord[2]] = {}
            dungeon[new_coord[0]-1,new_coord[1],new_coord[2]]['fill'] = 'D'
            dungeon[new_coord[0]+1,new_coord[1],new_coord[2]] = {}
            dungeon[new_coord[0]+1,new_coord[1],new_coord[2]]['fill'] = 'D'
            #need to retrace to last on exit stack?

            for key in exit_stack:
                ## this needs to be checked for level
                new_coord = key

            return new_coord
        



    elif pc_dict['direction'] == 'bad_things':
        new_coord = coord
        t_dict = bad_things(coord)
        
        if 'chute' in t_dict['trap']['type'] or 'elevator' in t_dict['trap']['type']:
            level_stack[new_coord] = t_dict

        new_coord = t_dict['coord']
        for x in range(3): #checking again in 3
            will_fit = in_dungeon((coord[0],coord[1]+x+1,coord[2]))
            if not will_fit:
                dungeon[(coord[0],coord[1]+x+1,coord[2])] = {}
                dungeon[(coord[0],coord[1]+x+1,coord[2])]['fill'] = 'C'
                new_coord = (coord[0],coord[1]+x+1,coord[2])
            else:
                break

        #check again in 3
        
    elif pc_dict['direction'] == 'random_encounter':
        new_coord = coord
        roll_first = random_check()
        "+1 like trap - wm"
        result_coord = check_action(roll_first, new_coord)
        new_coord = result_coord

        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2])) #square for monster
        if not will_fit:                                                
            dungeon[(coord[0],coord[1]+1,coord[2])+1] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])+1]['fill'] = 'wm'
        else:
            dungeon[(coord[0],coord[1]+1,coord[2])+1]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])+1]['fill'] + 'wm'

    return new_coord

#specific functions
def exit(coord):
    '''
    note fancy exit for doors on locations already mapped  
    '''
    e_dict = {}
    e_dict['type'] = 'N'
    d = roll_dice(1,20)
    print("EXIT CHECK",d)
    if d <= 6:
        e_dict['direction'] = 'L'
        will_fit = in_dungeon((coord[0]-1,coord[1],coord[2]))
        if not will_fit:
            e_dict['coord'] = (coord[0]-1,coord[1],coord[2])
        else:
            e_dict['coord'] = (coord[0]-1,coord[1],coord[2])
            e_dict['type'] = 'S'

    elif d>=7 and d <= 12:
        e_dict['direction'] = 'R'
        will_fit = in_dungeon((coord[0]-1,coord[1],coord[2]))
        if not will_fit:
            e_dict['coord'] = (coord[0]+1,coord[1],coord[2])
        else:
            e_dict['coord'] = (coord[0]+1,coord[1],coord[2])
            e_dict['type'] = 'S'
    else:
        e_dict['direction'] = 'A'
        will_fit = in_dungeon((coord[0]-1,coord[1],coord[2]))
        if not will_fit:        
            e_dict['coord'] = (coord[0],coord[1]+1,coord[2])
        else:
            e_dict['coord'] = (coord[0],coord[1]+1,coord[2])
            e_dict['type'] = 'S'

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

def fancy_exit(coord):
    e_dict_f = {}
    s = roll_dice(1,20)
    if s < 5:
        e_dict_f['type'] = 'S'
    elif s>=5 and s <= 10:
        e_dict_f['type'] = 'OW'
    else:
        e_dict_f['type'] = 'OPP'

    return e_dict_f


def side(coord):
    s_dict = {}
    s = roll_dice(1,20)
    print("SIDE CHECK",s)
    if s <= 2:
        s_dict['direction'] = 'L90'
    if s >= 3 and s <= 4:
        s_dict['direction'] = 'R90'
    if s == 5 :
        s_dict['direction'] = 'L45'
    if s == 6 :
        s_dict['direction'] = 'R45'
    if s == 7 :
        s_dict['direction'] = 'L135'
    if s == 8 :
        s_dict['direction'] = 'R135'
    if s == 9 :
        s_dict['direction'] = 'L45'
    if s == 10 :
        s_dict['direction'] = 'R45'
    if s >= 11 and s <= 13:
        s_dict['direction'] = 'T'
    if s >= 14 and s <= 15:
        s_dict['direction'] = 'Y'
    if s >= 16 and s <= 19:
        s_dict['direction'] = 'P'
    if s == 20:
        s_dict['direction'] = 'X'

    return s_dict

def turn(coord):
    t_dict = {}
    t = roll_dice(1,20)
    print("TURN CHECK",t)
    if t <= 8:
        t_dict['direction'] = 'L90'
    if t == 9:
        t_dict['direction'] = 'L45'
    if t == 10 :
        t_dict['direction'] = 'L135'
    if t >= 11 and t <= 18:
        t_dict['direction'] = 'R90'
    if t == 19:
        t_dict['direction'] = 'R45'
    if t == 20:
        t_dict['direction'] = 'R135'

    return t_dict


def room(coord, size="C"):
    '''
    can pass anything in that is not C for size and will work, just using R for room not Chamber
    just rectangular results for now
    '''
    r = roll_dice(1,20)
    room_size = [0,0]
    shape_dict = {}
    shape_dict['shape'] = 'R'
    shape_dict['size'] = [0,0]
    
    if r <= 2:
        if size=="C":
            shape_dict['size'] = [2,2]
        else:
            shape_dict['size'] = [1,1]
    if r >= 3 and r<=4:
        shape_dict['size'] = [2,2]
    if r >= 5 and r<=6:
        shape_dict['size'] = [3,3]
    if r >= 7 and r<=8:
        shape_dict['size'] = [4,4]
    if r >= 9 and r <=10:
        if size=="C":
            shape_dict['size'] = [2,3]
        else:
            shape_dict['size'] = [1,2]
    if r >= 11 and r<=13:
        shape_dict['size'] = [2,3]
    if r >= 14 and r <=15:
        if size=="C":
            shape_dict['size'] = [3,5]
        else:
            shape_dict['size'] = [2,4]
    if r >= 16 and r <=17:
        if size=="C":
            shape_dict['size'] = [4,6]
        else:
            shape_dict['size'] = [3,4]
    if r >= 18:
            #shape_dict = fancy_shape()
            ##MAKE ALL ROOMS RECTANGULAR TO START
            shape_dict['size'] = [4,6]

    return shape_dict

#not implemented yet
def width():
    '''
        to do 5 foot wide passage, need to redo and the 'default' is then to do 2 squares for everything
        get a basic version going first, then this slower version later
    '''
    w = roll_dice(1,20)
    pw = '10'
    if w >=13 and w <=16:
        pw = '20'
    elif w ==17:
        pw = '30'
    elif w ==18:
        pw = '5'
    else:
        pw = fancy_width()
    return pw

def fancy_width():
    w = roll_dice(1,20)
    if w <=4:
        pw = '40CL'
    elif w >=5 and w <=7:
        pw = '40CLCR'
    elif w >=8 and w <=10:
        pw = '50CLCR'
    if w >=11 and w <=12:
        pw = '50CLCRGA'
    if w >=13 and w <=15:
        pw = '10S'
    if w >=16 and w <=17:
        pw = '20R'
    elif w ==18:
        pw = '40R'
    elif w ==19:
        pw = '60R'
    else:
        pw = '20C'
    return pw

def fancy_shape():
    s = roll_dice(1,20)
    shape_dict = {}    
    shape_dict['water'] = 'N'
    shape_dict['size'] = 0

    if s <= 5:
        shape_dict['shape'] = 'C'
        p = roll_dice(1,20)
        if p <= 5:
            shape_dict['water'] = 'P'
        if p >=6 and p <= 7:
            shape_dict['water'] = 'W'
        if p >=8 and p <= 10:
            shape_dict['water'] = 'S'

    if s >= 6 and s <=8:
        shape_dict['shape'] = 'T'
    if s >= 9 and s <=11:
        shape_dict['shape'] = 'Z'
    if s >= 12 and s <=13:
        shape_dict['shape'] = 'S'
    if s >= 14 and s <=15:
        shape_dict['shape'] = 'V'
    if s >= 16 and s <=17:
        shape_dict['shape'] = 'H'
    if s >= 18 and s <=19:
        shape_dict['shape'] = 'O'
    if s >= 18 and s <=19:
        shape_dict['shape'] = 'CV'

    z = roll_dice(1,20)     
    if z <=3:
        shape_dict['size'] = 5
    if z >=4 and z <= 6:
        shape_dict['size'] = 9
    if z >=7 and z <= 8:
        shape_dict['size'] = 13
    if z >=9 and z <= 10:
        shape_dict['size'] = 20
    if z >=11 and z <= 12:
        shape_dict['size'] = 27
    if z >=13 and z <= 14:
        shape_dict['size'] = 34
    if z >=15:
        rollflag = True
        while flag == True:
            zr = roll_dice(1,20)
            shape_dict['size'] = shape_dict['size'] + 2000 + zr
            if zr <= 15:
                rollflag = False

    return shape_dict

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

def level(coord):
    level_dict = {}
    s = roll_dice(1,20)
    new_coord = coord
    level_dict['check'] = 0
    level_dict['type'] = 'stair'
    level_dict['room'] = 'N'
    level_dict['new_coord'] = new_coord
    if s <= 5:
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2])  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2]-1)  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
    if s == 6:
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2])  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])-1] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])-1]['fill'] = 'st'

            dungeon[(coord[0],coord[1]+1,coord[2])-2] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])-2]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2]-2)  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
    if s == 7:
        new_coord = (coord[0],coord[1],coord[2]-3)  ##3 in 20 closes
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2])  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])-1] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])-1]['fill'] = 'st'

            dungeon[(coord[0],coord[1]+1,coord[2]-2)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-2)]['fill'] = 'st'

            dungeon[(coord[0],coord[1]+1,coord[2]-3)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-3)]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[3]-2)  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
    if s == 8:
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2])  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]+1))  #down 1#facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2]+1)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]+1)]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2]+1)  ##1 in 20 closes
            level_dict['new_coord'] = new_coord
    if s == 9:
        #UD 
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'D'
            #new_coord = (coord[0],coord[1]+1,coord[2])  ##1 in 20 closes     
            level_dict['type'] = 'UD'   
            level_dict['new_coord'] = new_coord    
        d = roll_dice(1,6)
        if d == 1:
            #chute down
            will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing
            if not will_fit:                            
                dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
                dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'ch'

                dungeon[(coord[0],coord[1]+1,coord[2]-2)] = {}
                dungeon[(coord[0],coord[1]+1,coord[2]-2)]['fill'] = 'ch'
                new_coord = (coord[0],coord[1]+1,coord[2]-2)
                level_dict['type'] = 'UD-chute'       
                level_dict['new_coord'] = new_coord
    if s == 10:
        #DD
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #facing
        if not will_fit:                            
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'D'
            #new_coord = (coord[0],coord[1]+1,coord[2])  ##1 in 20 closes            
            level_dict['type'] = 'DD'       
            level_dict['new_coord'] = new_coord
        d = roll_dice(1,6)
        if d == 1:
            #chute down
            will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]+1))  #down 1#facing
            if not will_fit:                            
                dungeon[(coord[0],coord[1]+1,coord[2]+1)] = {}
                dungeon[(coord[0],coord[1]+1,coord[2]+1)]['fill'] = 'ch'
                new_coord = (coord[0],coord[1]+1,coord[2]-1)
                level_dict['type'] = 'DD-chute'       
                level_dict['new_coord'] = new_coord
    if s == 11:  ## account for all dungeon chimney levels
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]+1))  #down 1#facing
        if not will_fit:                            
            new_coord = (coord[0],coord[1],coord[2]+1)
            dungeon[(coord[0],coord[1],coord[2]+1)] = {}
            dungeon[(coord[0],coord[1],coord[2]+1)]['fill'] = 'cm'
            level_dict['check'] = 3
            level_dict['type'] = 'chimney'       
            level_dict['new_coord'] = new_coord
    if s == 12:
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]+1))  #down 1#facing
        if not will_fit:                            
            new_coord = (coord[0],coord[1],coord[2]+2)
            dungeon[(coord[0],coord[1],coord[2]+1)] = {}
            dungeon[(coord[0],coord[1],coord[2]+1)]['fill'] = 'cm'

            dungeon[(coord[0],coord[1],coord[2]+2)] = {}
            dungeon[(coord[0],coord[1],coord[2]+2)]['fill'] = 'cm'
            level_dict['check'] = 3
            level_dict['type'] = 'chimney'       
            level_dict['new_coord'] = new_coord
    if s == 13:
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing #need all the level well fits eventually
        if not will_fit:                            
            new_coord = (coord[0],coord[1],coord[2]-2)
            dungeon[(coord[0],coord[1],coord[2]-1)] = {}
            dungeon[(coord[0],coord[1],coord[2]-1)]['fill'] = 'cm'

            dungeon[(coord[0],coord[1],coord[2]-2)] = {}
            dungeon[(coord[0],coord[1],coord[2]-2)]['fill'] = 'cm'
            level_dict['check'] = 3
            level_dict['type'] = 'chimney'       
            level_dict['new_coord'] = new_coord
    if s >= 14 and s <=16:
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing #need all the level well fits eventually
        if not will_fit:                            
            new_coord = (coord[0],coord[1],coord[2]-1)
            dungeon[(coord[0],coord[1],coord[2]-1)] = {}
            dungeon[(coord[0],coord[1],coord[2]-1)]['fill'] = 'td'
            level_dict['check'] = 3
            level_dict['type'] = 'trapdoor'       
            level_dict['new_coord'] = new_coord
    if s == 17:
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing #need all the level well fits eventually
        if not will_fit:                            
            new_coord = (coord[0],coord[1],coord[2]-2)
            dungeon[(coord[0],coord[1],coord[2]-1)] = {}
            dungeon[(coord[0],coord[1],coord[2]-1)]['fill'] = 'td'

            dungeon[(coord[0],coord[1],coord[2]-2)] = {}
            dungeon[(coord[0],coord[1],coord[2]-2)]['fill'] = 'td'
            level_dict['check'] = 3
            level_dict['type'] = 'trapdoor'       
            level_dict['new_coord'] = new_coord
    if s >= 18:            
        #Up 1 then down 2 (total down 1), chamber at end (roll on TABLE V.)
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]+1))  #down 1#facing
        if not will_fit:                            
            new_coord = (coord[0],coord[1]+1,coord[2]+1)
            dungeon[(coord[0],coord[1],coord[2]+1)] = {}
            dungeon[(coord[0],coord[1],coord[2]+1)]['fill'] = 'st'

            coord = new_coord #up then down
            
            dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'td'

            coord = new_coord #up then down

            dungeon[(coord[0],coord[1],coord[2]-2)] = {}
            dungeon[(coord[0],coord[1],coord[2]-2)]['fill'] = 'td'

            new_coord = (coord[0],coord[1],coord[2]-2)


            level_dict['check'] = 3
            level_dict['new_coord'] = new_coord

            level_dict['room'] = 'Y'

    #level_dict['new_coord'] = new_coord
    return level_dict

def bad_things(coord):
    new_coord = coord    
    #all traps located ahead plus 1?
    t_dict = {}
    t_dict['new_coord'] == new_coord
    t_dict['trap'] == {}
    t_dict['secretdoor'] == 'N'
    t_dict['trap']['type'] == 'secretdoor'
    t_dict['trap']['chance'] = 1.0
    t_dict['trap']['fits'] = 'N'

    will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #down 1#facing
    if not will_fit:                                                
        dungeon[(coord[0],coord[1]+1,coord[2])+1] = {}

        t = roll_dice(1,20)
        if t <= 5:
            t_dict['secretdoor'] == 'Y'
            s = roll_dice(1,20)
            t_dict['trap']['chance'] = 0.15
            t_dict['trap']['chance_elf'] = 0.25
            t_dict['trap']['damage'] = roll_dice(1,6)
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pi'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord
            ## do stuff for exits!!
        if t >= 6 and t <= 7:
            t_dict['trap']['type'] = 'pit'
            t_dict['trap']['chance'] = 3.0/6.0
            t_dict['trap']['damage'] = roll_dice(1,6)
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pi'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t == 8:
            t_dict['trap']['type'] = 'pit'
            t_dict['trap']['chance'] = 3.0/6.0
            t_dict['trap']['effect'] = 'spikes'
            t_dict['trap']['damage'] = roll_dice(2,6)
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pis'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t >= 9 and t <= 11: #fitting in elevator room
            t_dict['trap']['type'] = 'elevator'
            adjust = 0
            lr = roll_dice(1,2)
            if lr == 1:
                adjust = -1
            else:
                adjust = 1
            if t == 9:
                #here we have checked if one straight ahead fits so random check if LR 2x2 branch from there
                d = 1
                # loop this for level descent -put in descent will fit checks
                t_dict['trap']['type'] = 'elevator'
                t_dict['trap']['duration'] = 30
                
            elif t == 10:
                d = 2
                t_dict['trap']['duration'] = 30
            else:
                if t == 11:
                    t_dict['trap']['duration'] = 60
                    d = roll_dice(1,4) + 1
                    # loop this for level descent - 

            #2x2 room
            for k in range(d):
                for j in range(2):
                    for i in range(2):
                        will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]-d-1))
                        if not will_fit:                
                            dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-d-1)] = {}
                            dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-d-1)]['fill'] = 'el'
                            new_coord (coord[0],coord[1]+3,coord[2]-d-1) #past elevator 2 and down
                        else:
                            break
        if t == 12:
            #12 Wall 10’ behind slides across passage blocking it for from 40-60 turns.
            t_dict['trap']['type'] = 'slidingwall'
            t_dict['trap']['chance'] = roll_dice(1,20) + 40
            t_dict['trap']['effect'] = 'blocked'
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'bw'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t == 13:
            t_dict['trap']['type'] = 'oil'
            t_dict['trap']['chance'] = roll_dice(1,20) + 40
            t_dict['trap']['effect'] = 'random person'
            t_dict['trap']['damage'] = roll_dice(2,6)
            t_dict['trap']['save'] = 'magic'
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'sw'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t == 14:
            t_dict['trap']['type'] = 'pit'
            t_dict['trap']['chance'] = 3.0/6.0
            t_dict['trap']['effect'] = 'crush death'
            t_dict['trap']['damage'] = roll_dice(2,6)
            t_dict['trap']['duration'] = roll_dice(1,4) + 1
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pic'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t == 15:
            t_dict['trap']['type'] = 'arrow'
            t_dict['trap']['chance'] = 0.05
            t_dict['trap']['damage'] = roll_dice(1,3)  * roll_dice(1,6)
            t_dict['trap']['save'] = 'poison'
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ar'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t == 16:
            t_dict['trap']['type'] = 'spear'
            t_dict['trap']['chance'] = 0.05
            t_dict['trap']['damage'] = roll_dice(1,3)  * roll_dice(1,8)
            t_dict['trap']['save'] = 'poison'
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'sp'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t == 17:
            t_dict['trap']['type'] = 'gas'
            t_dict['trap']['details'] = stinky()
            for key in t_dict['details']:
                t_dict[key] = t_dict['details'][key]
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'gs'
            new_coord = (coord[0],coord[1]+1,coord[2])
            t_dict['new_coord'] = new_coord            
        if t == 18:
            what_fall = roll_dice(1,2)
            if what_fall == 1:
                t_dict['trap']['type'] = 'doorfalls'
                t_dict['trap']['chance'] = 0.05
                t_dict['trap']['damage'] = roll_dice(1,10)
                t_dict['trap']['save'] = 'petrification'
                dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'df'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord                            
            else:
                t_dict['trap']['type'] = 'stonefalls'
                t_dict['trap']['chance'] = 0.05
                t_dict['trap']['damage'] = roll_dice(2,10)
                t_dict['trap']['save'] = 'petrification'
                dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'sf'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord                            
        if t == 19:
            t_dict['trap']['type'] = 'illusionarywall'
            w = roll_dice(1,20)
            if w <= 6:
                t_dict['trap']['type'] = t_dict['trap']['type'] + 'pit'
                t_dict['trap']['chance'] = 3.0/6.0
                t_dict['trap']['damage'] = roll_dice(1,6)
                dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'pi'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord
            elif w>=7 and w<=10:
                t_dict['trap']['type'] = t_dict['trap']['type'] + 'chute'
                t_dict['trap']['effect'] = 'one way'
                dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
                dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ch'
                new_coord = (coord[0],coord[1]+1,coord[2]-1)
                t_dict['new_coord'] = new_coord
            else:
                pass #put room here

        if t == 20:        
            dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ch'
            new_coord = (coord[0],coord[1]+1,coord[2]-1)
            t_dict['trap']['type'] = 'chute'
            t_dict['trap']['effect'] = 'one way'
            t_dict['trap']['duration'] = 'permanent'
            t_dict['new_coord'] = new_coord

        t_dict['trap']['fits'] = 'Y'
    
    return t_dict

def wandering_monster(coord):    
    wm_dict['result'] = testmonster()
    return wm_dict

def fancy_cave():
    pass

def wet_small():
    #not implemented yet
    w = roll_dice(1,20)
    wet_dict = {}
    wet_dict['wet'] = 'N'
    wet_dict['monster'] = 'N'
    wet_dict['treasure'] = 'N'
    wet_dict['magic'] = 'N'

    if w <= 8:
        pass
    elif w >= 9 and w <=10:
        wet_dict['wet'] = 'Y'
    elif w >= 11 and w <=12:
        wet_dict['wet'] = 'Y'
        wet_dict['monster'] = 'Y'
    elif w >= 13 and w <=18:
        wet_dict['wet'] = 'Y'
        wet_dict['monster'] = 'Y'
        wet_dict['treasure'] = 'Y'
    else:
        wet_dict['magic'] = 'Y'


def wet_large():
    #not implemented yet
    w = roll_dice(1,20)
    wet_dict = {}
    wet_dict['wet'] = 'N'
    wet_dict['monster'] = 'N'
    wet_dict['treasure'] = 'N'
    wet_dict['magic'] = 'N'

    if w <= 10:
        pass
    elif w >= 11 and w <=15:
        wet_dict['wet'] = 'Y'
    elif w >= 11 and w <=12:
        wet_dict['wet'] = 'Y'
        wet_dict['monster'] = 'Y'
    elif w >= 16 and w <=18:
        wet_dict['wet'] = 'Y'
        wet_dict['monster'] = 'Y' #as per encounter
    else:
        wet_dict['magic'] = 'Y'  #portal to another realm/world/dungeon23
        m = roll_dice(1,20)
        if m <= 18:
            wet_dict['monster'] = 'Y'

def wet_magic():
    #not implemented yet
    w = roll_dice(1,20)
    wet_magic_dict = {}
    if w <=8:
        e = roll_dice(1,20)
        if e<= 11:
            wet_magic_dict['effect'] = 'Au to Pt'
        else:
            wet_magic_dict['effect'] = 'Au to Pb'
    if w >=9 and w<=15:
        e = roll_dice(1,6)
        wet_magic_dict['effect'] = 'Per Character'
        if e == 1:
            wet_magic_dict['characteristic'] = 'STR'
        elif e == 2:
            wet_magic_dict['characteristic'] = 'DEX'
        elif e == 3:
            wet_magic_dict['characteristic'] = 'CON'
        elif e == 4:                
            wet_magic_dict['characteristic'] = 'INT'
        elif e == 5:                            
            wet_magic_dict['characteristic'] = 'WIS'
        else:
            wet_magic_dict['characteristic'] = 'CHA'
        e = roll_dice(1,2)
        s = roll_dict(1,3)
        if e == 1:
            wet_magic_dict['sign'] = 1            
        else:
            wet_magic_dict['sign'] = -1            
            wet_magic_dict['add'] = s * wet_magic_dict['sign']
    if w >=16 and w<=17:
        wet_magic_dict['effect'] = 'Talking Pool'
        a = roll_dice(1,20)
        if a <= 6:
            wet_magic_dict['alignment'] = 'LG'
        elif a >= 7 and a <= 9:
            wet_magic_dict['alignment'] = 'LE'
        elif a >= 10 and a <= 12:
            wet_magic_dict['alignment'] = 'CG'
        elif a >= 13 and a <= 17:
            wet_magic_dict['alignment'] = 'CE'
        else:
            wet_magic_dict['alignment'] = 'N'
    if w >=18:
        l = roll_dice
        wet_magic_dict['effect'] = 'Teleport'
        if l <= 7:
            #back to surface
            new_coord = (0,0,0)
        elif l >= 8 and l <= 12:
            #elsewhere on leve
            #randomise from current available coords
            loclist = list(dungeon.keys())
            t = roll_dice(1,len(loclist))
            new_coord = loclist[t-1]
        else:
            #100 miles away or effectively
            new_coord = (0,0,0)

def stinky():
    s = roll_dice(1,20)
    stinky_dict = {}
    if s <=7:
        stinky_dict['type'] = 'smoke'
    elif s>=8 and s <= 9:
        stinky_dict['type'] = 'blinding'
        stinky_dict['effect'] = roll_dice(1,6)
        stinky_dict['duration'] = stinky_dict['effect']
    elif s>=10 and s <= 12:
        stinky_dict['type'] = 'fear'
        stinky_dict['effect'] = 'run back 12'
    elif s==13:
        stinky_dict['type'] = 'sleep'
        stinky_dict['effect'] = roll_dice(1,6)
        stinky_dict['duration'] = stinky_dict['effect']        
    elif s>=14 and s <= 18:
        stinky_dict['type'] = 'strength'
        stinky_dict['effect'] = roll_dice(1,6)
        stinky_dict['duration'] = roll_dice(1,10)
        stinky_dict['characters'] = 'fighters'
    elif s==19:
        stinky_dict['type'] = 'sickness'
        stinky_dict['effect'] = 'return to surface or die'
    else:
        stinky_dict['type'] = 'poison'
        stinky_dict['effect'] = 'save vs death or die'

    return stinky_dict

#need data structure
#do we have an exit order stack?
#array of corridors and walls, where corridor can be room/staircase etc odd corridor, even wall
#how big a fake canvas to make - or do we just have a dictionary and add parts in as they go
#eg have 1000 x 1000 and fake easting and northing
#direction preference - n,w,e,s? - roll randomly?
#not as yet checking for space already occupied
#not checking to backtrack the exit stack if dead-end
#not checking any level stacks to go up down, similarly
#not implemented passage width as yet - default only

from monsters import testmonster
from treasure import testtreasure
print (testmonster() + ' ' + testtreasure())
#testtreasure()

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

facing = 'A'
## got to implement for all here eventually, complicates things

START_COORD = (0,0,-1)
coord = START_COORD

roll_first = random_check()
#no possible dead_end on first action
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

coord_lim = coord_limits(dungeon)
xmin = coord_lim[0][0]
ymin = coord_lim[0][1]
zmin = coord_lim[0][2]
xmax = coord_lim[1][0]
ymax = coord_lim[1][1]
zmax = coord_lim[1][2]
print("MIN:",xmin,ymin,zmin)
print("MAX:",xmax,ymax,zmax)

xwidth = xmax - xmin + 1
ywidth = ymax - ymin + 1
zwidth = zmax - zmin + 1

zwidth = max(1, zwidth)

print("COORD:", coord, result_coord, coord_lim)

print("DUNGEON:", dungeon)
print("EXIT_STACK:", exit_stack)
print("LEVEL_STACK:", level_stack)

chararray = np.full((xwidth,ywidth,zwidth), 'B', dtype='U1')
print("SHAPE",chararray.shape)
#print("ARRAY",chararray)

#chararray[0,0,0] = 'S'

##make more than one level

## ignore any random tiny up level things for now on chimneys or trapdoros
for down in range(zwidth):

    for key in dungeon:
        #print("KEY:",key,"KEYWIDTH:",key[0]+xwidth-1,key[1]+ywidth-1,key[2]+zwidth-1)
        #print("KEY:",key,"KEYWIDTH:",key[0]+xmax-key[0],key[1]+ymax-key[1],key[2]+zmax - key[2])
        
        if key[2] == (down-1): #-1, -2, etc
            if 'fill' in dungeon[key] :  
                print("KEY:",key,"KEYWIDTH:",key[0]+xmin*-1,key[1]+ymin*-1,key[2]+zmin*-1,dungeon[key]['fill'])
                #chararray[[key][0],key[1],key[2]] = dungeon[key]['fill']
                #chararray[key[0]+xmax-key[0],key[1]+ymax-key[1],key[2]+zmax - key[2]] = dungeon[key]['fill']
                chararray[key[0]+xmin*-1,key[1]+ymin*-1,key[2]+zmin*-1] = dungeon[key]['fill']
            else:
                print("KEY:",key,"KEYWIDTH:",key[0]+xmin*-1,key[1]+ymin*-1,key[2]+zmin*-1)

    #only for first level        
    if down == 0:
        chararray[0+xmin*-1,0+ymin*-1,+zmin*-1] = 'S'        

    #need a multi-level maker, this is just doing first for now

    #make dungeon html
    strhead = '''
    <html>
    <head>
    <title>DUNGEON</title>
    <style>
        table,
        th,
        td {
            padding: 10px;
            border: 1px solid black;
            border-collapse: collapse;
        }
        .red_background {
                background-color: red;
            }

        .green_background {
                background-color: green;
            }
        .gray_background {
                background-color: gray;
            }
        .brown_background {
                background-color: brown;
            }

        .blue_background {
                background-color: blue;
            }
        .black_background {
                background-color: black;
            }

        </style>
    </head>
    <body>
    <table>
    '''

    strend = '''
    </table>
    </body>
    </html>
    '''

    with open('dungeon_' + str(down+1) + '.html','w') as f:
        f.write(strhead)
        
        for j in range(chararray.shape[1]):
            f.write('<TR>')
            for i in range(chararray.shape[0]):
                if chararray[i,j,0] == 'B':
                    strdata = '<td class="black_background">' + chararray[i,j,0] + '</td>'
                elif chararray[i,j,0] == 'C':
                    strdata = '<td>' + chararray[i,j,0] + '</td>'
                elif chararray[i,j,0] == 'R':
                    strdata = '<td class="gray_background">' + chararray[i,j,0] + '</td>'
                elif chararray[i,j,0] == 'D':
                    strdata = '<td class="gray_background">' + chararray[i,j,0] + '</td>'

                else:
                    strdata = '<td class="red_background">' + chararray[i,j,0] + '</td>'

                f.write(strdata)
            f.write('</TR>')

        f.write(strend)




   
    