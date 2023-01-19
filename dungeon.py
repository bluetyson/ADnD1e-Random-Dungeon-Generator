import sys
import os
import numpy as np
#import pandas as pd
import random
import time
import datetime
import copy
import json
import pickle
import math

PI = math.pi
ARGV = sys.argv

#standard algorithm
LEVEL = "Y"
if len(ARGV) > 2:
    LEVEL = ARGV[2]
    #stub to handle making a dungeon of just one level
    #this would be checked to disable level descent in periodi check
    #also in traps that go down, substitute

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
    minx = 9999
    maxx = -9999
    miny = 9999
    maxy = -9999
    minz = 9999
    maxz = -9999

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
        if key[2] < minz:
            minz = key[2]

    coord_min = (minx,miny,minz)
    coord_max = (maxx,maxy,maxz)

    return [coord_min, coord_max]

def coord_random(dungeon):
    
    coordlist = list(dungeon.keys())
    c = roll_dice(1,len(coordlist))

    for index, key in enumerate(dungeon):
        if index + 1 == c:
            #return dungeon[key]
            return (key[0],key[1],key[2])

    ##make arrrays for each level
def coord_edge(dungeon):
    minx = 9999
    maxx = -9999
    miny = 9999
    maxy = -9999
    minz = 9999
    maxz = -9999

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
        if key[2] < minz:
            minz = key[2]

    coord_min = (minx,miny,minz)
    coord_max = (maxx,maxy,maxz)

    coordlist = list(dungeon.keys())
    c = roll_dice(1,len(coordlist))

    non_edge = []
    for index, key in enumerate(dungeon):
        if key[0] != minx and key[1] != miny and key[0] != maxx and key[1] != maxy:
            non_edge.append((key[0],key[1],key[2]))
    
    return non_edge


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
        if LEVEL == "N": #make this what you like or could be config
            pc_dict['direction'] = 'room'
            pc_dict['check'] = 3
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

#def passage_make(coord, loop=3,xmod=0,ymod=0,zmod=0,xloop=0,yloop=1,zloop=0,xwidth=0,ywidth=0):
def passage_make(coord, loop=3,xmod=0,ymod=0,zmod=0,xloop=0,yloop=1,zloop=0,xwidth=0,ywidth=0):    #check this
    p_dict = width()
    #print("PDICTBEFORE:",p_dict)
    #print("CHECKWIDTH:",p_dict['width'],"LOOP:",loop,"COORD:",coord)
    #print("PDICT:",p_dict)
    if p_dict['width'] <= 1: #0.5 width do cosmetically later

        new_coord = coord
        print()
        for y in range(loop):                
            will_fit = in_dungeon((coord[0]+xmod+xloop*y,coord[1]+ymod+yloop*y,coord[2]+zmod+zloop*y))
            print("loop:","willfit:",will_fit,(coord[0]+xmod+xloop*y,coord[1]+ymod+yloop*y,coord[2]+zmod+zloop*y))
            if not will_fit:
                dungeon[(coord[0]+xmod+xloop*y,coord[1]+ymod+yloop*y,coord[2]+zmod+zloop*y)] = {}
                dungeon[(coord[0]+xmod+xloop*y,coord[1]+ymod+yloop*y,coord[2]+zmod+zloop*y)]['fill'] = 'C'
                new_coord = (coord[0]+xmod+xloop*y,coord[1]+ymod+yloop*y,coord[2]+zmod+zloop*y)
            else:
                break
    else: #do column width first, then do fancy parts #work out new_coord??  #default go to xpos/right for now
        print("FANCY WIDTH:",p_dict)
        for w in range(p_dict['width']):
            
            new_coord = coord
            for y in range(loop):
                #print("COORD BEFORE:",(coord[0]+xmod+xloop*y+xwidth*w,coord[1]+ymod+yloop*y+ywidth*w,coord[2]+zmod+zloop*loop))
                will_fit = in_dungeon((coord[0]+xmod+xloop*y+xwidth*w,coord[1]+ymod+yloop*y+ywidth*w,coord[2]+zmod+zloop*loop))
                #print("width:",w,"loop:","willfit:",will_fit,(coord[0]+xmod+xloop*y+xwidth*w,coord[1]+ymod+yloop*y+ywidth*w,coord[2]+zmod+zloop*loop))
                if not will_fit:
                    dungeon[(coord[0]+xmod+xloop*y+xwidth*w,coord[1]+ymod+yloop*y+ywidth*w,coord[2]+zmod+zloop*y)] = {}
                    
                    if y == 1: #approx midpoint fill - could random 3/4 it but for 3s will be in middle anyway wrong for 6 ok for 3
                        dungeon[(coord[0]+xmod+xloop*y+xwidth*w,coord[1]+ymod+yloop*y+ywidth*w,coord[2]+zmod+zloop*y)]['fill'] = 'C' + p_dict['fill']
                    else:
                        dungeon[(coord[0]+xmod+xloop*y+xwidth*w,coord[1]+ymod+yloop*y+ywidth*w,coord[2]+zmod+zloop*y)]['fill'] = 'C'
                    new_coord = (coord[0]+xmod+xloop*y+xwidth*w,coord[1]+ymod+yloop*y+ywidth*w,coord[2]+zmod+zloop*y)
                else:
                    break

    return new_coord


def check_action(pc_dict, coord, room_stack):
    ## need a current 'orientation' 'L R A B
    if pc_dict['direction'] == 'ahead':
        if 1 == 1:
            #new_coord = coord
            new_coord = passage_make(coord,loop=6,ymod=1,yloop=1,xwidth=1)


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
                            if x != 0:
                                dungeon[(coord[0]-1,coord[1]+x-1,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1,coord[1]+x-1,coord[2])]['fill'] = 'Cd'
                            new_coord = (coord[0]-1,coord[1]+x-1,coord[2])
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1,coord[1]+x+1,coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'Cd'
                            new_coord = (coord[0]-1,coord[1]+x+1,coord[2])

                if e_dict['beyond'] == 'A':              
                    d = roll_dice(1,20)              
                    if d >=3 and d <= 5:
                        will_fit = in_dungeon((coord[0]-1,coord[1],coord[2]))
                        if not will_fit:
                            exit_stack[(coord[0]-1,coord[1],coord[2])] = {}
                    else:
                        #30m passage that direction
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-x-1,coord[1],coord[2]))
                            if not will_fit:
                                dungeon[(coord[0]-x-1,coord[1],coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]-x-1,coord[1],coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]-x-1,coord[1],coord[2])]['fill'] = 'Cd'
                                new_coord = ((coord[0]-x-1,coord[1],coord[2]))                        


                if e_dict['beyond'] == '4AB':   ##45 A
                    which_way = roll_dice(1,2)           
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == '4BA':   ##45 A
                    which_way = roll_dice(1,2)  #work out random direction         
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-1-x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == 'Room':
                    #want those we randomly position lr
                    new_coord = coord
                    #new part!
                    #if coming from here pass door to room function?
                    #dungeon[coord]['fill'] = dungeon[coord]['fill'] + 'd'  #add door indicator
                    #not Rd room??
                    shape_dict = room(coord, room_stack, size='Rd' )  ## different type to get slightly different table pass Rd to indicate from door
                    #room_stack = shape_dict['room_stack']
                    #each room part check for inside

                    print("ROOM SHAPE:",shape_dict)
                    ## do simple version first of x directions and y directions of rectangular
                    rm = room_make(shape_dict, coord)
                    if rm == "GOOD":
                        secret_doors(shape_dict)                    


        elif e_dict['direction'] == 'R':
            if e_dict['type'] == 'N':
                exit_stack[(coord[0]+1,coord[1],coord[2])] = {}
                if e_dict['beyond'] == 'P':
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]+1,coord[1],coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]+1,coord[1]+x-1,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]+1,coord[1]+x-1,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+1,coord[1]+x-1,coord[2])]['fill'] = 'Cd'
                            new_coord = (coord[0]+1,coord[1]+x-1,coord[2])
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1,coord[1]+x+1,coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'Cd'
                            new_coord = (coord[0]-1,coord[1]+x+1,coord[2])

                if e_dict['beyond'] == 'A':              
                    d = roll_dice(1,20)              
                    if d >=3 and d <= 5:
                        will_fit = in_dungeon((coord[0]+1,coord[1],coord[2]))
                        if not will_fit:
                            exit_stack[(coord[0]+1,coord[1],coord[2])] = {}
                    else:
                        #30m passage that direction
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-x-1,coord[1],coord[2]))
                            if not will_fit:
                                dungeon[(coord[0]+x+1,coord[1],coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]+x+1,coord[1],coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]+x+1,coord[1],coord[2])]['fill'] = 'Cd'
                                new_coord = ((coord[0]+x+1,coord[1],coord[2]))      

                if e_dict['beyond'] == '4AB':   ##45 A - need to make facing for R different eventually
                    which_way = roll_dice(1,2)           
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                                if x!= 0:
                                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == '4BA':   ##45 A
                    which_way = roll_dice(1,2)  #work out random direction         
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-1-x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                                if x!= 0:
                                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                                if x!= 0:
                                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == 'Room':
                    #want those we randomly position lr
                    new_coord = coord
                    #dungeon[coord]['fill'] = dungeon[coord]['fill'] + 'd'  #add door indicator
                    ## check for room or chamber
                    rt = roll_dice(1,10)
                    if rt <=8:
                        #room
                        shape_dict = room(coord, room_stack,size='Rd')  ## different type to get slightly different table indicate room from door
                    else:
                        #chamber
                        shape_dict = room(coord, room_stack)
                    #each room part check for inside

                    print("ROOM SHAPE:",shape_dict)
                    rm = room_make(shape_dict, coord)
                    if rm == "GOOD":
                        secret_doors(shape_dict)                    

                
        else:  #final branch ahead
            if e_dict['type'] == 'N':
                exit_stack[(coord[0],coord[1]+1,coord[2])] = {}
                if e_dict['beyond'] == 'P':
                    will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))
                    if not will_fit:
                        #dungeon[(coord[0],coord[1]+1,coord[2])] = {}
                        #handle very first cool being cooridor door creation
                        if (coord[0],coord[1],coord[2]) not in dungeon:
                            dungeon[(coord[0],coord[1],coord[2])] = {}
                        dungeon[(coord[0],coord[1],coord[2])]['fill'] = 'Cd'
                        new_coord = (coord[0],coord[1]+1,coord[2])
                        # 10 x 10 room need to check contents!

                        #need to implement for set type room
                        new_coord = coord
                        shape_dict = room(coord, room_stack, size="10") #10 is special case to mandate 1 roll for size

                        print("ROOM SHAPE:",shape_dict)
                        #rm = room_make(shape_dict, coord)
                        # set Cd above for doors to indicate door to room ahead
                        rm = room_make(shape_dict, coord)
                        
                        if rm == "GOOD":
                            secret_doors(shape_dict)                    

                ### previously not in missing problem
                if e_dict['beyond'] == 'A':              
                    d = roll_dice(1,20)              
                    if d >=3 and d <= 5:
                        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))
                        if not will_fit:
                            exit_stack[(coord[0],coord[1]+1,coord[2])] = {}
                    else:
                        #30m passage that direction
                        for x in range(3):
                            will_fit = in_dungeon((coord[0],coord[1]+x+1,coord[2]))
                            if not will_fit:
                                dungeon[(coord[0],coord[1]+x+1,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0],coord[1]+x+1,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0],coord[1]+x+1,coord[2])]['fill'] = 'Cd'
                                new_coord = ((coord[0],coord[1]+x+1,coord[2]))                        


                if e_dict['beyond'] == '4AB':   ##45 A
                    which_way = roll_dice(1,2)           
                    if which_way == 1:  #corridor left
                        for x in range(3):
                            will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
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
                                if x != 0:
                                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                                if which_way == 1:
                                    new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                            else:
                                break
                    else:
                        for x in range(3): #corridor right
                            will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                            if not will_fit:                
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                                if x != 0:
                                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                                else:
                                    dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                                if which_way == 2:
                                    new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                            else:
                                break

                if e_dict['beyond'] == 'Room':
                    #want those we randomly position lr
                    new_coord = coord
                    #new part!
                    #if coming from here pass door to room function?
                    #dungeon[coord]['fill'] = dungeon[coord]['fill'] + 'd'  #add door indicator

                    shape_dict = room(coord, room_stack, size='Rd' )  ## different type to get slightly different table pass Rd to indicate from door
                    #room_stack = shape_dict['room_stack']
                    #each room part check for inside

                    print("ROOM SHAPE:",shape_dict)
                    ## do simple version first of x directions and y directions of rectangular
                    rm = room_make(shape_dict, coord)
                    if rm == "GOOD":
                        secret_doors(shape_dict)                    



        ## got to proceed with direction/type of exit

    elif pc_dict['direction'] == 'side':

        new_coord = coord
        s_dict = side(coord)
        print("S_DICT:",s_dict)

        if s_dict['direction'] == 'L90':
            new_coord = passage_make(coord,xmod=-1,xloop=-1,ywidth=1)    

        elif s_dict['direction'] == 'R90':
            new_coord = passage_make(coord,xmod=1,xloop=1,ywidth=1)    

        elif s_dict['direction'] == 'L45':
            new_coord = passage_make(coord,xmod=-1,xloop=-1,ymod=1,yloop=1,xwidth=1)    

        elif s_dict['direction'] == 'R45':
            new_coord = passage_make(coord,xmod=1,xloop=1,ymod=1,yloop=1,xwidth=1)    

        elif s_dict['direction'] == 'L135':
            new_coord = passage_make(coord,xmod=-1,xloop=-1,ymod=-1,yloop=-1,xwidth=1)    

        elif s_dict['direction'] == 'R135':
            new_coord = passage_make(coord,xmod=1,xloop=1,ymod=-1,yloop=-1,xwidth=1)    

        elif s_dict['direction'] == 'T':
            which_way = roll_dice(1,2)
            new_coord_left = passage_make(coord,xmod=-1,xloop=-1,ywidth=1)    
            new_coord_right = passage_make(coord,xmod=1,xloop=1,ywidth=1)    

            if which_way == 1:
                new_coord = new_coord_left
            else:
                new_coord = new_coord_right

        elif s_dict['direction'] == 'Y':
            which_way = roll_dice(1,2)  #got to move this up
            new_coord_left = passage_make(coord,xmod=-1,xloop=-1,ymod=1,yloop=1,xwidth=1)    
            new_coord_right = passage_make(coord,xmod=1,xloop=1,ymod=1,yloop=1,xwidth=1)    
            if which_way == 1:
                new_coord = new_coord_left
            else:
                new_coord = new_coord_right

        elif s_dict['direction'] == 'P': #plus
            which_way = roll_dice(1,3)
            new_coord_left = passage_make(coord,xmod=-1,xloop=-1,ywidth=1)    
            new_coord_right = passage_make(coord,xmod=1,xloop=1,ywidth=1)    
            new_coord_ahead = passage_make(coord,ymod=1,yloop=1,xwidth=1)    

            if which_way == 1:
                new_coord = new_coord_left
            elif which_way == 2:
                new_coord = new_coord_right
            else:
                new_coord = new_coord_ahead

        else:
        #s_dict['direction'] == 'X': 45 and 135
            which_way = roll_dice(1,4) ##got to move this up
            new_coord_left = passage_make(coord,xmod=-1,xloop=-1,ymod=1,yloop=1,xwidth=1)    
            new_coord_right = passage_make(coord,xmod=1,xloop=1,ymod=1,yloop=1,xwidth=1) 
            
            new_coord_left_back = passage_make(coord,xmod=-1,xloop=-1,ymod=-1,yloop=-1,xwidth=1)    
            new_coord_right_back = passage_make(coord,xmod=1,xloop=1,ymod=-1,yloop=-1,xwidth=1)                   

            if which_way == 1:
                new_coord = new_coord_left
            elif which_way == 2:
                new_coord = new_coord_right
            elif which_way == 3:
                new_coord = new_coord_left_back
            else:
                new_coord = new_coord_right_back

					

    elif pc_dict['direction'] == 'turn':
        new_coord = coord
        t_dict = turn(coord)
        print("T_DICT:",t_dict)

        t = roll_dice(1,20)

        if t_dict['direction'] == 'L90':
            new_coord = passage_make(coord,xmod=-1,xloop=-1,ywidth=1)    

        elif t_dict['direction'] == 'R90':
            new_coord = passage_make(coord,xmod=1,xloop=1,ywidth=1)    

        elif t_dict['direction'] == 'L45':
            new_coord = passage_make(coord,xmod=-1,xloop=-1,ymod=1,yloop=1,xwidth=1)    

        elif t_dict['direction'] == 'R45':
            new_coord = passage_make(coord,xmod=1,xloop=1,ymod=1,yloop=1,xwidth=1)    

        elif t_dict['direction'] == 'L135':
            new_coord = passage_make(coord,xmod=-1,xloop=-1,ymod=-1,yloop=-1,xwidth=1)    

        else:  #t_dict['direction'] == 'R135'
            new_coord = passage_make(coord,xmod=1,xloop=1,ymod=-1,yloop=-1,xwidth=1)    

        
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
        shape_dict = room(coord, room_stack) #if another room pass not C="R"  
        #room_stack = shape_dict['room_stack']      
        #each room part check for inside

        print("ROOM SHAPE:",shape_dict)
        rm = room_make(shape_dict, coord)
        if rm == "GOOD":
            secret_doors(shape_dict)                    

    elif pc_dict['direction'] == 'level':
        new_coord = coord
        level_dict = level(coord)
        new_coord = level_dict['new_coord']
        level_stack[new_coord] = level_dict

        print("LEVEL:",level_dict)
        
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
            shape_dict = room(coord, room_stack) #if another room pass not C="R"        

            print("ROOM SHAPE:",shape_dict)
            rm = room_make(shape_dict, coord)
            if rm == "GOOD":
                secret_doors(shape_dict)                    


        return new_coord

    elif pc_dict['direction'] == 'stop':
        new_coord = coord
        check_coord_L = (new_coord[0]-1,new_coord[1],new_coord[2])
        check_coord_R = (new_coord[0]+1,new_coord[1],new_coord[2])
        check_coord_A = (new_coord[0],new_coord[1]+1,new_coord[2])

        dead_end = True
        dead_end_count = 0

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
            ## need to check if in dungeons where putting Ds and handle can't go through dead ends
            e_dict_f = fancy_exit(coord)
            if 'S' in e_dict_f:
                e_dict = {}
                e_dict['direction'] = 'R'
                e_dict['coord'] = (coord[0],coord[1]+1,coord[2])
                e_dict['type'] = e_dict_f['type']
                exit_stack[coord] = e_dict
                dead_end = False

        #this will also need checking for facing etc.
        if dead_end == True:
            #need to check for secret doors here
            #only in left, right and ahead
            #put SD dict in to handle the directions, or a dict that can be read out?  
            #or make a dead end dict as no rooms here
            will_fit = in_dungeon((new_coord[0],new_coord[1]+1,new_coord[2]))
            if not will_fit:
                dungeon[(new_coord[0],new_coord[1]+1,new_coord[2])] = {}
                dungeon[(new_coord[0],new_coord[1]+1,new_coord[2])]['fill'] = 'D'
                dead_end_dict[(new_coord[0],new_coord[1]+1,new_coord[2])] = 'ymax'
                #dead_end_dict[(new_coord[0],new_coord[1]+1,new_coord[2])] = {}
                s = roll_dice(1,20)
                if s <= 5:
                    dungeon[(new_coord[0],new_coord[1]+1,new_coord[2])]['fill'] = 'Dsd'
                    e_dict = exit((new_coord[0],new_coord[1]+1,new_coord[2]))
                    exit_direction_full((new_coord[0],new_coord[1]+1,new_coord[2]), e_dict)

            will_fit = in_dungeon((new_coord[0]-1,new_coord[1],new_coord[2]))
            if not will_fit:
                dungeon[(new_coord[0]-1,new_coord[1],new_coord[2])] = {}
                dungeon[(new_coord[0]-1,new_coord[1],new_coord[2])]['fill'] = 'D'
                dead_end_dict[(new_coord[0]-1,new_coord[1],new_coord[2])] = 'xmin'
                s = roll_dice(1,20)
                if s <= 5:
                    dungeon[(new_coord[0]-1,new_coord[1],new_coord[2])]['fill'] = 'Dsd'
                    e_dict = exit((new_coord[0]-1,new_coord[1],new_coord[2]))
                    exit_direction_full((new_coord[0]-1,new_coord[1],new_coord[2]), e_dict)

            will_fit = in_dungeon((new_coord[0]+1,new_coord[1],new_coord[2]))
            if not will_fit:
                dungeon[(new_coord[0]+1,new_coord[1],new_coord[2])] = {}
                dungeon[(new_coord[0]+1,new_coord[1],new_coord[2])]['fill'] = 'D'
                dead_end_dict[(new_coord[0]+1,new_coord[1],new_coord[2])] = 'xmax'
                s = roll_dice(1,20)
                if s <= 5:
                    dungeon[(new_coord[0]-1,new_coord[1],new_coord[2])]['fill'] = 'Dsd'
                    e_dict = exit((new_coord[0]+1,new_coord[1],new_coord[2]))
                    exit_direction_full((new_coord[0]+1,new_coord[1],new_coord[2]), e_dict)

            ## add angle parts
            will_fit = in_dungeon((new_coord[0]-1,new_coord[1]+1,new_coord[2]))
            if not will_fit:
                dungeon[(new_coord[0]-1,new_coord[1]+1,new_coord[2])] = {}
                dungeon[(new_coord[0]-1,new_coord[1]+1,new_coord[2])]['fill'] = 'D'
            will_fit = in_dungeon((new_coord[0]+1,new_coord[1]+1,new_coord[2]))
            if not will_fit:
                dungeon[(new_coord[0]+1,new_coord[1]+1,new_coord[2])] = {}
                dungeon[(new_coord[0]+1,new_coord[1]+1,new_coord[2])]['fill'] = 'D'

            #need to retrace to last on exit stack?
            print("DEAD END")
            for key in exit_stack:
                ## this needs to be checked for level
                new_coord = key

            return new_coord



    elif pc_dict['direction'] == 'bad_things':
        new_coord = coord
        t_dict = bad_things(coord, room_stack)
        print("TRAP:",t_dict)
        
        if 'chute' in t_dict['trap']['type'] or 'elevator' in t_dict['trap']['type']:
            level_stack[new_coord] = t_dict

        new_coord = t_dict['new_coord']
        for x in range(3): #checking again in 3
            will_fit = in_dungeon((coord[0],coord[1]+x+1,coord[2]))
            if not will_fit:
                dungeon[(coord[0],coord[1]+x+1,coord[2])] = {}
                dungeon[(coord[0],coord[1]+x+1,coord[2])]['fill'] = 'C'
                new_coord = (coord[0],coord[1]+x+1,coord[2])
            else:
                break
        
    elif pc_dict['direction'] == 'random_encounter':
        print("WANDERING MONSTER")
        new_coord = coord
        roll_first = random_check()
        #"+1 like trap - wm"
        result_coord = check_action(roll_first, new_coord, room_stack)
        new_coord = result_coord

        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2])) #square for monster
        if not will_fit:                                                
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'wm'
        else:
            print('wm filled up check:',dungeon[(coord[0],coord[1]+1,coord[2])])
            dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'wm' #get this to work
            #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'wm'
            print('wm key check',dungeon[(coord[0],coord[1]+1,coord[2])])

        wm_coord = (coord[0],coord[1]+1,coord[2])
        wandering_monster_stack['key_count'] +=1
        wandering_monster_stack[wandering_monster_stack['key_count']] = {}
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord] = {}
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['level'] = level_matrix(abs(coord[2]))
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['type'] = 'NA'
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['No'] = 0
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['XP'] = 0

    return new_coord

#basic above options seem good, now to go through specifics and see what needs adding and finessing

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
    elif b>=5 and b <= 8:
        e_dict['beyond'] = 'A'
    elif b==9:
        e_dict['beyond'] = '4AB'
    elif b==10:
        e_dict['beyond'] = '4BA'
    else:
        e_dict['beyond'] = 'Room'

    exit_stack[coord] = e_dict

    return e_dict

def exit_beyond():   
    e_dict = {}
    b = roll_dice(1,20)
    if b <= 4:
        e_dict['beyond'] = 'P'
    elif b>=5 and b <= 8:
        e_dict['beyond'] = 'A'
    elif b==9:
        e_dict['beyond'] = '45AB'
    elif b==10:
        e_dict['beyond'] = '45BA'
    else:
        e_dict['beyond'] = 'Room'
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


def room(coord, room_stack, size="C", content=None ):
    '''
    can pass anything in that is not C for size and will work, just using R for room not Chamber
    just rectangular results for now
    pass 'MT' in content to mandate monster and treasure in room - for Illusionary Wall trap
    10 is fof 1 size room ahead of door
    '''
    #print("ROOM STACK ON ENTRY:",room_stack)

    room_stack['key_count'] += 1

    r = roll_dice(1,20)
    print("ROOM ROLL:",r)
    room_size = [0,0]
    shape_dict = {}
    shape_dict['shape'] = 'R'
    shape_dict['size'] = [0,0]

    ## pass a 10x10 signifier for set room size
    if size == "10":
        r = 1
    
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
        shape_dict = fancy_shape(shape_dict)
        ##MAKE ALL ROOMS RECTANGULAR TO START
        #shape_dict['size'] = [4,6]

    #shape, size, exits, contents, treasure, in  
    if size == 'Rd':
        shape_dict['fromdoor'] = 'Y'

    room_contents(shape_dict, coord, content)

    shape_dict = exit_no(shape_dict)
    shape_dict = exit_loc(shape_dict)
    shape_dict = exit_dir(shape_dict)

    ## check the room stack and exit functions here
    
    print("ROOM KEY COUNT:",room_stack['key_count'])
    print("ROOM STACK CHECK in room function:", room_stack)

        
    return shape_dict


def width():
    '''
        not implemented yet
        to do 5 foot wide passage, need to redo and the 'default' is then to do 2 squares for everything
        get a basic version going first, then this slower version later
        maybe for 5 foot corridor do it in html where it works? half the width
        could have cosmetic width markers as html CCC, CC to start then grid squares later
    '''
    w = roll_dice(1,20)
    #w = 20 #test
    print("WIDTH ROLL:",w)
    p_dict = {}
    p_dict['width'] = 1
    p_dict['type'] = 'N'
    p_dict['fill'] = ''

    #hack width for test here
    if w <= 12:
        p_dict['width'] = 1    
    elif w >=13 and w <=16:
        p_dict['width'] = 2
    elif w ==17:
        p_dict['width'] = 3
    elif w ==18:
        p_dict['width'] = 0.5
    else:
        p_dict = fancy_width()
    return p_dict

def fancy_width():
    '''
    CL = columns
    CLCR = double columns
    GA = galley
    ST = stream
    RI = river
    CH = chasm
    BR = bridge
    BN = boat same side
    BO = boat opp side
    '''
    p_dict = {}
    p_dict['width'] = 0
    p_dict['type'] = ''
    p_dict['fill'] = ''

    w = roll_dice(1,20)
    if w <=4:
        p_dict['width'] = 4
        p_dict['type'] = 'CL'
        p_dict['fill'] = 'I'
    elif w >=5 and w <=7:
        p_dict['width'] = 4
        p_dict['type'] = 'CLCR'
        p_dict['fill'] = 'I'
    elif w >=8 and w <=10:
        p_dict['width'] = 5
        p_dict['type'] = 'CLCR'
        p_dict['fill'] = 'I'
    if w >=11 and w <=12:
        p_dict['width'] = 5
        p_dict['type'] = 'CLCRGA'
        p_dict['fill'] = 'I'
    if w >=13 and w <=15:
        p_dict['width'] = 1
        p_dict['type'] = 'STBR'
        p_dict['fill'] = 'br'
        st = roll_dice(1,20)
        if st >=16:
            p_dict['type'] = 'ST'
            p_dict['fill'] = 'ri'
    if w >=16 and w <=17:
        p_dict['width'] = 2
        p_dict['type'] = 'RIBR'
    elif w ==18:
        p_dict['width'] = 4
        p_dict['type'] = 'RIBR'       
    elif w ==19:
        p_dict['width'] = 6
        p_dict['type'] = 'RIBR'       
    else:
        p_dict['width'] = 2
        p_dict['type'] = 'HBR'
        p_dict['fill'] = 'Hbr'       
        st = roll_dice(1,20)
        if st <= 10:
            pass #as above
        elif st >=11 and st <= 15:
            p_dict['fill'] = 'HA'  #can leap across
        else:
            p_dict['fill'] = 'Hl'

    if p_dict['type'] == 'RIBR':
        p_dict['fill'] = 'br'
        st = roll_dice(1,20)
        if st <=10:
            pass
        elif st >=11 and st <= 15:
            p_dict['type'] = 'RIBN'
            p_dict['fill'] = 'bn'
            opp = roll_dice(1,2)
            if opp == 2:
                p_dict['type'] = 'RIBO'
                p_dict['fill'] = 'bo'
        else:
            p_dict['type'] == 'RI'
            p_dict['fill'] = 'ri'

    return p_dict

def fancy_shape(shape_dict):
    s = roll_dice(1,20)
    #shape_dict = {}    
    shape_dict['water'] = 'N'
    shape_dict['size'] = 0

    ## get size for later use
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
        while rollflag == True:
            zr = roll_dice(1,20)
            shape_dict['size'] = shape_dict['size'] + 20 + zr
            if zr <= 15:
                rollflag = False

    if s <= 5:
        shape_dict['shape'] = 'C'  #circle
        shape_dict['fancy_shape'] = 'C'
        p = roll_dice(1,20)

        if p <= 5:
            shape_dict['water'] = 'P'
            shape_dict = wet_small(shape_dict, coord)
        if p >=6 and p <= 7:
            shape_dict['water'] = 'W' #well #make this descend
        if p >=8 and p <= 10:
            shape_dict['water'] = 'S' #shaft #make this descend
            
        usesize = shape_dict['size'] / PI
        radius = int(math.sqrt(usesize))
        shape_dict['size'] = [radius, radius]

    if s >= 6 and s <=8:
        shape_dict['shape'] = 'T'
        shape_dict['fancy_shape'] = 'T'
        width = math.sqrt(shape_dict['size'] * 4/math.sqrt(3))
        height = width * math.sqrt(3)/2
        shape_dict['size'] = [width, height]
    if s >= 9 and s <=11:
        shape_dict['shape'] = 'Z'
        shape_dict['fancy_shape'] = 'Z'
        #trapezoid make height 2 and top = bottom-2 and area +2 = 2* base
        b = int((shape_dict['size'] + 2)/2)
        shape_dict['size'] = [b,2]
    if s >= 12 and s <=13:
        shape_dict['shape'] = 'S'
    if s >= 14 and s <=15:
        #hack a circle
        shape_dict['shape'] = 'V'
        shape_dict['fancy_shape'] = 'V'
        usesize = shape_dict['size'] / PI
        radius = int(math.sqrt(usesize))
        shape_dict['size'] = [max(1,radius-2), radius+2]
    if s >= 16 and s <=17:
        shape_dict['shape'] = 'H'
        shape_dict['fancy_shape'] = 'H'
        usesize = math.sqrt(shape_dict['size'] * 2.0/3.0*math.sqrt(3))
        shape_dict['size'] = [int(usesize),int(usesize)]
    if s >= 18 and s <=19:
        shape_dict['shape'] = 'O'
        shape_dict['fancy_shape'] = 'H'
        #A=2(1+2)*a^2
        usesize = math.sqrt(shape_dict['size'] / 2*(1+math.sqrt(2)) )
        #side - now get radius
        radius = usesize * math.sqrt(1 + 1/math.sqrt(2))
        shape_dict['size'] = [int(radius),int(radius)]
    else:
        shape_dict['shape'] = 'CV'
        shape_dict['fancy_shape'] = 'H'
        c = roll_dice(1,20)
        if c <= 5:
            shape_dict['size'] = [4,6]
        elif c>= 6 and c<=7:
            shape_dict['size'] = [5,roll_dice(1,2)+6]
        elif c>= 8 and c<=9:            
            #to implement double cave
            shape_dict['size'] = [6,6]
            #Double Cave: 2 × 3, 6 × 6
        elif c>= 10 and c<=11:            
            #Double Cave: 35’ × 50’, 80’ × 90’
            shape_dict['size'] = [8,9]
        elif c>= 12 and c<=14:            
            shape_dict['size'] = [roll_dice(1,2)+8,roll_dice(1,2)+11]
        elif c>= 15 and c<=16:            
            shape_dict['size'] = [12,15]
        elif c>= 17 and c<=18:            
            shape_dict['size'] = [15,20]
            shape_dict = wet_small(shape_dict, coord)
        else:
            shape_dict['size'] = [roll_dice(1,6)+24,roll_dice(1,6)+34]
            shape_dict = wet_large(shape_dict, coord)
            #if shape_dict['lake'] needs check in room?? for after room coords done
        #wet check
      
        shape_dict['shape'] = 'R' ## for now
    return shape_dict

    
def exit_no(shape_dict):
    area = shape_dict['size'][0]*shape_dict['size'][1]
    e = roll_dice(1,20)
    if e <=3:
        if area <= 6:
            shape_dict['exits'] = 1
        else:
            shape_dict['exits'] = 2
    elif e>=4 and e<=6:
        if area <= 6:
            shape_dict['exits'] = 2
        else:
            shape_dict['exits'] = 3
    elif e>=7 and e<=9:
        if area <= 6:
            shape_dict['exits'] = 3
        else:
            shape_dict['exits'] = 4
    elif e>=10 and e<=12:
        if area <= 1200:
            shape_dict['exits'] = 0
            shape_dict['secretdoors'] = 'check'
        else:
            shape_dict['exits'] = 1
    elif e>=13 and e<=15:
        shape_dict['exits'] = roll_dice(1,4)
    elif e>=16 and e<=18:
        if area <= 1600:
            shape_dict['exits'] = 0
            shape_dict['secretdoors'] = 'check'
        else:
            shape_dict['exits'] = 1
    else:
        shape_dict['exits'] = 1
        # if differentiate chambers and rooms this becomes passage
        shape_dict['exitstype'] = 'door'

    return shape_dict   

def exit_loc(shape_dict):
    shape_dict['exitlocations'] = {}
    for i in range(shape_dict['exits']):
        e = roll_dice(1,20)
        if e <= 7:
            shape_dict['exitlocations'][i+1] = 'O'
        elif e>= 8 and e <=12:
            shape_dict['exitlocations'][i+1] = 'L'
        elif e>= 13 and e <=17:
            shape_dict['exitlocations'][i+1] = 'R'
        else:
            shape_dict['exitlocations'][i+1] = 'S'

    return shape_dict               

def exit_dir(shape_dict):
    #not needed until get chamber/room differentiation
    #not implemented
    shape_dict['exitdirections'] = {}
    for i in range(shape_dict['exits']):
        e = roll_dice(1,20)
        if e<=16:
            shape_dict['exitdirections'][i+1] = 'A'
        elif e >=17 and e<=18:
            shape_dict['exitdirections'][i+1] = '45AB'
        else:
            shape_dict['exitdirections'][i+1] = '45BA'

    return shape_dict            

def room_contents(shape_dict, coord, content):
    shape_dict['contents'] = {}
    r = roll_dice(1,20)
    print("ROOM CONTENTS ROLL:", r)
    if content == "MT":
        r = 15 #make monster and treasure

    if r <= 12:
        shape_dict['contents']['empty'] = 'Y'
    elif r >13 and r <=14:
        shape_dict['contents']['monster'] = {}
        shape_dict['contents']['monster']['level'] = level_matrix(abs(coord[2]))
        shape_dict['contents']['monster']['type'] = 'NA'
        shape_dict['contents']['monster']['No'] = 0
        shape_dict['contents']['monster']['XP'] = 0
    elif r >15 and r <=17:
        shape_dict['contents']['monster'] = {}
        shape_dict['contents']['treasure'] = {}
        shape_dict['contents']['monster']['level'] = level_matrix(abs(coord[2]))
        shape_dict['contents']['monster']['type'] = 'NA'
        shape_dict['contents']['monster']['No'] = 0
        shape_dict['contents']['monster']['XP'] = 0

        shape_dict = loot(shape_dict,coord,monster="Y")
        shape_dict = loot_store(shape_dict)
        
        if shape_dict['contents']['treasure']['protection'] == 'guard':
            shape_dict = loot_guard(shape_dict)
        else:
            shape_dict = loot_hide(shape_dict)

    elif r == 18:
        shape_dict['contents']['level'] = {}
    elif r == 19:        
        shape_dict['contents']['trap'] = {}
        shape_dict['contents']['trap'] = bad_things(coord, room_stack, size="R") #or should all traps be on room entry and this is ok?
        #trying this again
    else:
        shape_dict['contents']['treasure'] = {}
        shape_dict = loot(shape_dict,coord,monster="N")
        shape_dict = loot_store(shape_dict)
        
        if shape_dict['contents']['treasure']['protection'] == 'guard':
            shape_dict = loot_guard(shape_dict)
        else:
            shape_dict = loot_hide(shape_dict)

def room_make(shape_dict, coord, size="C"):
    newcoord = coord

    if shape_dict['shape'] == 'R':
        print("rectangular", room_stack['key_count'])
        room_stack[room_stack['key_count']] = {}
        #H x W
        #position based on size
        adjust = 0
        if size == "C":
            if shape_dict['size'][1] % 2 == 0:
                lr = roll_dice(1,2)
                if lr == 1:
                    adjust = -1
                else:
                    adjust = 1
                #don't adjust back rooms into not fitting for secret doors

            #if shape_dict['size'][1] == 2:
            for j in range(shape_dict['size'][1]):
                for i in range(shape_dict['size'][0]):
                    will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]))
                    if not will_fit:                
                        dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])] = {}
                        dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2])]['fill'] = 'R' +  str(room_stack['key_count'])
                        #add to room stack dictionary for key printing
                        room_stack[room_stack['key_count']][(coord[0] + i + adjust,coord[1]+j+1,coord[2])] = {}
                        if i == 0 and j == 0 and 'fromdoor' in shape_dict:
                            room_stack[room_stack['key_count']][(coord[0] + i + adjust,coord[1]+j+1,coord[2])]['fill'] = 'Rd' + str(room_stack['key_count'])
                        else:
                            room_stack[room_stack['key_count']][(coord[0] + i + adjust,coord[1]+j+1,coord[2])]['fill'] = 'R' + str(room_stack['key_count'])

                    else:
                        break
        else:  ## branch for from inside rooms and secret doors
            for j in range(shape_dict['size'][1]):
                for i in range(shape_dict['size'][0]):
                    will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j,coord[2]))
                    if not will_fit:                
                        dungeon[(coord[0] + i + adjust,coord[1]+j,coord[2])] = {}
                        dungeon[(coord[0] + i + adjust,coord[1]+j,coord[2])]['fill'] = 'R' +  str(room_stack['key_count'])
                        #add to room stack dictionary for key printing
                        room_stack[room_stack['key_count']][(coord[0] + i + adjust,coord[1]+j,coord[2])] = {}
                        if i == 0 and j == 0 and 'fromdoor' in shape_dict:
                            room_stack[room_stack['key_count']][(coord[0] + i + adjust,coord[1]+j,coord[2])]['fill'] = 'Rd' + str(room_stack['key_count'])
                        else:
                            room_stack[room_stack['key_count']][(coord[0] + i + adjust,coord[1]+j,coord[2])]['fill'] = 'R' + str(room_stack['key_count'])

                    else:
                        break


        #loop the shape_dict contents for exists etc
        print("ROOM SHAPE DICT CONTENTS")
        
        print("ROOM STACK CHECK",room_stack[room_stack['key_count']])
        troom_lim = coord_limits(room_stack[room_stack['key_count']])
        trxmin = troom_lim[0][0]
        trymin = troom_lim[0][1]
        trzmin = troom_lim[0][2]
        trxmax = troom_lim[1][0]
        trymax = troom_lim[1][1]
        trzmax = troom_lim[1][2]
        print("RMIN-CHECK:",trxmin,trymin,trzmin)
        print("RMAX-CHECK:",trxmax,trymax,trzmax)

        if trxmin > 9000 or trymin > 9000 or trzmin > 9000:
            #NULL room #should handle below exception problem
            #no coords above to reduce these numbers to room limits
            #must make sure everything else in contents comes out here
            print("NULL ROOM: no need to progress further with this one")
            #delete from room dictionary the stub?
            del room_stack[room_stack['key_count']]
            room_stack['key_count'] -= 1
            return "BAD"

        #check for water to put a pool or lake in
        
        for key in shape_dict:
            #print(key, shape_dict[key])
            #test to implement other things - need fills for these
            if key == 'water':
                print("HAS WATER",shape_dict[key])
                #mid_room = [int(trxmax-trxmin)/2+1,int(trymax-trymin)/2+1]  ## got to get from coords actually found
                #for pool, shaft, well
                #mid_coord = (trxmin + mid_room[0],trymin + mid_room[1], trzmin)
                #now picking a random coord from list that exists to do this
                mid_coord = coord_random(room_stack[room_stack['key_count']])
                #print(mid_room, mid_coord)
                print(mid_coord)

                #for lake - remove any edge coords

                ##need to put in dict - maybe replace R with P in the fill
                #this is where a pool goes
                if shape_dict[key] == 'P':
                    print("has Pool")
                    #check for wet_magic
                    if mid_coord in dungeon:
                        print("fitting mid_coord", mid_coord)
                        dungeon[mid_coord]['fill'] = dungeon[mid_coord]['fill'] + 'P'
                        if 'wet_magic' in shape_dict['pool']:
                            dungeon[mid_coord]['fill'] = dungeon[mid_coord]['fill'] + 'M'
                    else:
                        print("fit fail",room_stack[room_stack['key_count']])
                elif shape_dict[key] == 'L':
                    print("has Lake")
                    ##double LL could be location of treasure and monster?
                    ## make sure at least tiny one pixel lake
                    if mid_coord in dungeon:
                        print("fitting mid_coord", mid_coord)
                        dungeon[mid_coord]['fill'] = dungeon[mid_coord]['fill'] + 'L'
                        if 'wet_magic' in shape_dict['lake']:
                            dungeon[mid_coord]['fill'] = dungeon[mid_coord]['fill'] + 'M'

                        non_edge = coord_edge(room_stack[room_stack['key_count']])
                        for c in non_edge:
                            dungeon[c]['fill'] = dungeon[c]['fill'] + 'L'
                            if 'wet_magic' in shape_dict['lake']:
                                dungeon[c]['fill'] = dungeon[c]['fill'] + 'M'
                    else:
                        print("fit fail",room_stack[room_stack['key_count']])

                elif shape_dict[key] == 'W':
                    print("has Well")
                    if mid_coord in dungeon:
                        print("fitting mid_coord", mid_coord)
                        dungeon[mid_coord]['fill'] = dungeon[mid_coord]['fill'] + 'W'
                    else:
                        print("fit fail",room_stack[room_stack['key_count']])

                elif shape_dict[key] == 'S':
                    print("has Shaft")
                    if mid_coord in dungeon:
                        print("fitting mid_coord", mid_coord)
                        dungeon[mid_coord]['fill'] = dungeon[mid_coord]['fill'] + 'S'
                    else:
                        print("fit fail",room_stack[room_stack['key_count']])

                else:
                    pass #not wet

                #what about lake
            if key == 'wet_magic':
                print("HAS WATER AND MAGIC",shape_dict[key])
                wet_magic_str = 'M'  #in building pools and lakes check for this


            if key == 'contents':
                for c in shape_dict['contents']:
                    if c == 'monster':   
                        monster_string = ''  #could be some lookup indicator number maybe or just monster as many long list legend to do otherwise
                        monster_string = 'm' #dummy default
                        #or the ref to the table rolled on is maybe good
                        #monsters has bug
                        print("MONSTER ROOM STACK CHECK:",room_stack[room_stack['key_count']].keys())
                        print("MONSTER ROOM LEN CHECK:",len(list(room_stack[room_stack['key_count']].keys())))
                        rand_length = len(list(room_stack[room_stack['key_count']].keys()))
                        w = roll_dice(1,rand_length)
                        print("MONSTER ROOM ROLL CHECK:",w)
                        for index, r in enumerate(room_stack[room_stack['key_count']].keys()):
                            #print("treasureindex",r)print("monsterindex",r)
                            if index + 1 == w:
                                room_stack[room_stack['key_count']][r]['fill'] = room_stack[room_stack['key_count']][r]['fill'] + monster_string
                                print("newmonsterfill",room_stack[room_stack['key_count']][r]['fill']) 
                                dungeon[r]['fill'] = dungeon[r]['fill'] + monster_string


                    if c == 'treasure':
                        treasure_string = ''
                        #get what it is
                        for tt in shape_dict['contents']['treasure']['type']:
                            if shape_dict['contents']['treasure']['type'][tt] > 0:
                                treasure_string = tt[0]
                                if tt == 'gems':
                                    treasure_string = treasure_string.upper()
                                print("TREASURE STRING CHECK:",treasure_string)

                        rand_length = len(list(room_stack[room_stack['key_count']].keys()))
                        w = roll_dice(1,rand_length)
                        print("TREASURE ROOM ROLL CHECK:",w)
                        for index, r in enumerate(room_stack[room_stack['key_count']].keys()):
                            #print("treasureindex",r)
                            if index + 1 == w:
                                room_stack[room_stack['key_count']][r]['fill'] = room_stack[room_stack['key_count']][r]['fill'] + treasure_string
                                print("newtreasurefill",room_stack[room_stack['key_count']][r]['fill'])
                                dungeon[r]['fill'] = dungeon[r]['fill'] + treasure_string
                        #need to output guards and hidden in room_stack or put shape_dict in room_stack


                    if c == 'trap':
                        ##need to check for secret doors
                        ##need random location
                        for sh in shape_dict['contents']:
                            print("TRAP SHAPE DICT CONTENTS:",shape_dict['contents'][sh])
                        for tr in shape_dict['contents']['trap']:
                            #for trtype in shape_dict['contents']['trap'][tr]:
                            #print( "CONTENTS TRAP TYPE:", trtype)
                            print( "CONTENTS TRAP TYPE:", shape_dict['contents']['trap'][tr])
                            if tr == 'secretdoor':
                                print("secretdoor info:",shape_dict['contents']['trap'][tr])
                                #for this need secret door procedure like exits
                                #secret room has treasure

                        rand_length = len(list(room_stack[room_stack['key_count']].keys()))
                        w = roll_dice(1,rand_length)
                        print("TRAP ROOM ROLL CHECK:",w)
                        trap_string = ''
                        for index, r in enumerate(room_stack[room_stack['key_count']].keys()):
                            #print("trapindex",r)
                            if 1 == 1:  #work out if shape_dict bad things initial doing what it needs - not putting in ranom place though?
                                #so this disabled for now
                                #if use this take it out of shape_dict['trap'] and just use this for indicator
                                if index + 1 == w:
                                    trap_string = shape_dict['contents']['trap']['trap']['abv']
                                    
                                    ##got to find from t_dict what to put in string
                                    room_stack[room_stack['key_count']][r]['fill'] = room_stack[room_stack['key_count']][r]['fill'] + trap_string
                                    print("newtrapfill",room_stack[room_stack['key_count']][r]['fill'] + trap_string)
                                    dungeon[r]['fill'] = dungeon[r]['fill'] + trap_string


                    #if c is wet or other things in contents need to go above exits probably but null rooms should not have

            if key == 'exits':
                '''
                can get errors for null rooms - so check if still default min/max and delete entry prior
                '''
                room_lim = coord_limits(room_stack[room_stack['key_count']])
                rxmin = room_lim[0][0]
                rymin = room_lim[0][1]
                rzmin = room_lim[0][2]
                rxmax = room_lim[1][0]
                rymax = room_lim[1][1]
                rzmax = room_lim[1][2]
                print("RMIN:",rxmin,rymin,rzmin)
                print("RMAX:",rxmax,rymax,rzmax)

                secret_door_count = 0
                secret_door_dict = {}

                if shape_dict['exits'] == 0:
                    #check for secret doors in all walls
                    #print("SECRET DOOR NOT IMPLEMENTED IN OUTPUT YET")
                    #loop through room coords and check edges for sdoors
                    #count the secret doors
                    #randomly choose one to follow 
                    #apply basics of this to other secret door check places
                    #exit stack for all secret doors
                    #go across xmin from ymin to ymax
                    #go across xmax from ymin to ymax
                    #go across ymin from xmin to xmax
                    #go across ymax from xmin to xmax

                    #edges are (xmax - xmin + 1) * 2
                    #edges are (ymax - ymin + 1) * 2

                    #ymin

                    ##gotta check the exit passageways out etc.
                    #if which_way == 1:
                        #new_coord = (el[0]-1-x,el[1]+1+x,rzmin)
                    #use exit_beyond function exit_beyond()
                    for y in range(rymin,rymax+1):
                        s = roll_dice(1,20)
                        if s <= 5:
                            secret_door_count +=1 
                            secret_door_dict[secret_door_count] = {}
                            secret_door_dict[secret_door_count][(rxmin,y,rzmin)] = 'xmin'
                            try:
                                dungeon[(rxmin,y,rzmin)]['fill'] = dungeon[(rxmin,y,rzmin)]['fill'] + 'sd'
                            except Exception as nosdfillE:
                                error_dict[error_dict['key_count']] = nosdfillE
                                error_dict['type']['key_count'] = "secret door fill 1667"
                                error_dict['key_count'] += 1
                                print(nosdfillE)
                                print("DUNGEONERRORCHECK:",dungeon, "xmin sd")
                                print("ROOMSTACKCHECK:",room_stack)
                                continue

                            #exit check is one left of above
                            #e_dict = exit((rxmin-1,y,rzmin))
                            #exit_result(e_dict,(rxmin-1,y,rzmin))
                            e_dict = exit_beyond()
                            e_dict['loc'] = 'xminloc'
                            secret_door_dict[secret_door_count][(rxmin-1,y,rzmin)] = e_dict


                    for y in range(rymin,rymax+1):
                        s = roll_dice(1,20)
                        if s <= 5:
                            secret_door_count +=1 
                            secret_door_dict[secret_door_count] = {}
                            secret_door_dict[secret_door_count][(rxmax,y,rzmin)] = 'xmax'
                            try:
                                dungeon[(rxmax,y,rzmin)]['fill'] = dungeon[(rxmax,y,rzmin)]['fill'] + 'sd'
                            except Exception as nosdfillE:
                                print(nosdfillE)
                                error_dict[error_dict['key_count']] = nosdfillE
                                error_dict['type']['key_count'] = "secret door fill 1693"
                                error_dict['key_count'] += 1
                                print("DUNGEONERRORCHECK:",dungeon, "xmax sd")
                                print("ROOMSTACKCHECK:",room_stack)
                                #raise("coordinate fail error")
                                continue

                            #exit check is one left of above
                            #e_dict = exit((rxmax+1,y,rzmin))
                            #exit_result(e_dict,(rxmax+1,y,rzmin))
                            e_dict = exit_beyond()
                            e_dict['loc'] = 'xmaxloc'
                            secret_door_dict[secret_door_count][(rxmax+1,y,rzmin)] = e_dict

                    for x in range(rxmin,rxmax+1):
                        s = roll_dice(1,20)
                        if s <= 5:
                            secret_door_count +=1 
                            secret_door_dict[secret_door_count] = {}
                            secret_door_dict[secret_door_count][(x,rymin,rzmin)] = 'ymin'
                            try:
                                dungeon[(x,rymin,rzmin)]['fill'] = dungeon[(x,rymin,rzmin)]['fill'] + 'sd'
                            except Exception as nosdfillE:
                                error_dict[error_dict['key_count']] = nosdfillE
                                error_dict['type']['key_count'] = "secret door fill 1717"
                                error_dict['key_count'] += 1
                                print(nosdfillE)
                                print("DUNGEONERRORCHECK:",dungeon, "ymin sd")
                                print("ROOMSTACKCHECK:",room_stack)
                                continue
                            #exit check is one up min from above
                            #e_dict = exit((x,rymin-1,rzmin))
                            #exit_result(e_dict,(x,rymin-1,rzmin))
                            e_dict = exit_beyond()
                            e_dict['loc'] = 'yminloc'
                            secret_door_dict[secret_door_count][(x,rymin-1,rzmin)] = e_dict

                    for x in range(rxmin,rxmax+1):
                        s = roll_dice(1,20)
                        if s <= 5:
                            secret_door_count +=1 
                            secret_door_dict[secret_door_count] = {}
                            secret_door_dict[secret_door_count][(x,rymax,rzmin)] = 'ymax'
                            try:
                                dungeon[(x,rymax,rzmin)]['fill'] = dungeon[(x,rymax,rzmin)]['fill'] + 'sd'
                            except Exception as nosdfillE:
                                error_dict[error_dict['key_count']] = nosdfillE
                                error_dict['type']['key_count'] = "secret door fill 1740"
                                error_dict['key_count'] += 1
                                print(nosdfillE)
                                print("DUNGEONERRORCHECK:",dungeon, "ymax sd")
                                print("ROOMSTACKCHECK:",room_stack)
                                continue

                                

                            #exit check is one down max from above
                            #e_dict = exit((x,rymax+1,rzmin))
                            #exit_result(e_dict,(x,rymax+1,rzmin))
                            e_dict = exit_beyond()
                            e_dict['loc'] = 'ymaxloc'
                            secret_door_dict[secret_door_count][(x,rymax+1,rzmin)] = e_dict


                    print("SECRET DOOR COUNT:",secret_door_count)
                    print("SECRET DOOR DICT:",secret_door_dict)


                    shape_dict['contents']['secret_door_dict'] = secret_door_dict
                    shape_dict['contents']['secret_door_count'] = secret_door_count


                else:
                    take_exit = roll_dice(1,shape_dict['exits'])

                    for e in range(shape_dict['exits']):
                        #echeck plus 1 for room
                        print("EXIT CHECK",e)
                        print("exit location:",shape_dict['exitlocations'][e+1])
                        print("exit direction:",shape_dict['exitdirections'][e+1])
                        
                        
                        #putting in place
                        #need the maximum L/R/B/A back and ahead coordinates - so max and min X/Y for the room to place things
                        #work out which exit to take - currently will take the most recent one
                        #also check which random exit to follow

                        #the below need checks to be secret doors if will fit fails
                        if shape_dict['exitlocations'][e+1] == 'O':
                            #check for possible positions at ymax range from xmin to xmax
                            #find random location in opp wall and add to door
                            es = roll_dice(1,rxmax-rxmin + 1)
                            el = [rxmin + es -1,rymax]

                            #30m passage that direction - ahead y+
                            if shape_dict['exitdirections'][e+1] == 'A': #AHEAD
                                for x in range(3):
                                    will_fit = in_dungeon((el[0],el[1]+1+x,rzmin))
                                    if not will_fit:
                                        dungeon[(el[0],el[1]+1+x,rzmin)] = {}
                                        dungeon[(el[0],el[1]+1+x,rzmin)]['fill'] = 'C'
                                        if take_exit == e+1: #dice 1, loop 0
                                            new_coord = (el[0],el[1]+1+x,rzmin)
                                    else:
                                        sd = roll_dice(1,20)
                                        if sd <= 5:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0],el[1]+1+x-1,rzmin)] = 'Y'
                                        elif sd >=6 and sd <=10:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0],el[1]+1+x-1,rzmin)] = 'OW'
                                        else:
                                            pass
                                        break

                            else: #shape_dict['exitdirections'][e+1]: #AB or BA if opp wall back 45 no good
                                which_way = roll_dice(1,2)           
                                if which_way == 1:  #corridor left
                                    for x in range(3):
                                        will_fit = in_dungeon((el[0]-1-x,el[1]+1+x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]-1-x,el[1]+1+x,rzmin)] = {}
                                            dungeon[(el[0]-1-x,el[1]+1+x,rzmin)]['fill'] = 'C'
                                            if which_way == 1 and take_exit == e+1:
                                                new_coord = (el[0]-1-x,el[1]+1+x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x+1,el[1]+1+x-1,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x+1,el[1]+1+x-1,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break
                                else:
                                    for x in range(3): #corridor right
                                        will_fit = in_dungeon((el[0]+1+x,el[1]+1+x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]+1+x,el[1]+1+x,rzmin)] = {}
                                            dungeon[(el[0]+1+x,el[1]+1+x,rzmin)]['fill'] = 'C'
                                            if which_way == 2 and take_exit == e+1:
                                                new_coord = (el[0]+1+x,el[1]+1+x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x-1,el[1]+1+x-1,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x-1,el[1]+1+x-1,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break

                        elif shape_dict['exitlocations'][e+1] == 'L': #LEFT
                            #check for possible positions at xmin range from ymin to ymax
                            try:
                                es = roll_dice(1,rymax-rymin + 1)
                                el = [rxmin,rymin + es -1]
                            except Exception as roomsizeE:
                                error_dict[error_dict['key_count']] = roomsizeE
                                error_dict['type']['key_count'] = "room size 1855"
                                error_dict['key_count'] += 1

                                #try and work out if null room - might go away if now has no coords
                                print("error is:",roomsizeE)
                                print(shape_dict)
                                print(room_stack)

                            if shape_dict['exitdirections'][e+1] == 'A':
                                for x in range(3):
                                    will_fit = in_dungeon((el[0]-1-x,el[1],rzmin))
                                    if not will_fit:
                                        dungeon[(el[0]-1-x,el[1],rzmin)] = {}
                                        dungeon[(el[0]-1-x,el[1],rzmin)]['fill'] = 'C'
                                        if take_exit == e+1: #dice 1, loop 0
                                            new_coord = (el[0]-1-x,el[1],rzmin)  

                                    else:
                                        sd = roll_dice(1,20)
                                        if sd <= 5:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0]-1-x+1,el[1],rzmin)  ] = 'Y'
                                        elif sd >=6 and sd <=10:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0]-1-x+1,el[1],rzmin)  ] = 'OW'
                                        else:
                                            pass
                                        break

                            else: #shape_dict['exitdirections'][e+1]: #AB or BA if opp wall back 45 no good
                                which_way = roll_dice(1,2)           
                                if which_way == 1:  #corridor opp
                                    for x in range(3):
                                        will_fit = in_dungeon((el[0]-1-x,el[1]+1+x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]-1-x,el[1]+1+x,rzmin)] = {}
                                            dungeon[(el[0]-1-x,el[1]+1+x,rzmin)]['fill'] = 'C'
                                            if which_way == 1 and take_exit == e+1:
                                                new_coord = (el[0]-1-x,el[1]+1+x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x+1,el[1]+1+x-1,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x-1,el[1]+1+x-1,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break
                                else:
                                    for x in range(3): #same
                                        will_fit = in_dungeon((el[0]-1-x,el[1]-1-x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]-1-x,el[1]-1-x,rzmin)] = {}
                                            dungeon[(el[0]-1-x,el[1]-1-x,rzmin)]['fill'] = 'C'
                                            if which_way == 2 and take_exit == e+1:
                                                new_coord = (el[0]-1-x,el[1]-1-x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x+1,el[1]-1-x+1,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x-1+1,el[1]+1+x-1,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break

                        elif shape_dict['exitlocations'][e+1] == 'R':                    
                            #check for possible positions at xmax range from ymin to ymax    
                            es = roll_dice(1,rymax-rymin + 1)
                            el = [rxmax,rymin + es -1]

                            if shape_dict['exitdirections'][e+1] == 'A':
                                for x in range(3):
                                    will_fit = in_dungeon((el[0]+1+x,el[1],rzmin))
                                    if not will_fit:
                                        dungeon[(el[0]+1+x,el[1],rzmin)] = {}
                                        dungeon[(el[0]+1+x,el[1],rzmin)]['fill'] = 'C'
                                        if take_exit == e+1: #dice 1, loop 0
                                            new_coord = (el[0]+1+x,el[1],rzmin)
                                    else:
                                        sd = roll_dice(1,20)
                                        if sd <= 5:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0]+1+x-1,el[1],rzmin)] = 'Y'
                                        elif sd >=6 and sd <=10:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0]+1+x-1,el[1],rzmin)] = 'OW'
                                        else:
                                            pass
                                        break


                            else: #shape_dict['exitdirections'][e+1]: #AB or BA if opp wall back 45 no good
                                which_way = roll_dice(1,2)           
                                if which_way == 1:  #corridor opp
                                    for x in range(3):
                                        will_fit = in_dungeon((el[0]+1+x,el[1]+1+x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]+1+x,el[1]+1+x,rzmin)] = {}
                                            dungeon[(el[0]+1+x,el[1]+1+x,rzmin)]['fill'] = 'C'
                                            if which_way == 1:
                                                new_coord = (el[0]+1+x,el[1]+1+x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x-1,el[1]+1+x-1,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x-1,el[1]+1+x-1,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break
                                else:
                                    for x in range(3): #same
                                        will_fit = in_dungeon((el[0]+1+x,el[1]-1-x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]+1+x,el[1]-1-x,rzmin)] = {}
                                            dungeon[(el[0]+1+x,el[1]-1-x,rzmin)]['fill'] = 'C'
                                            if which_way == 2:
                                                new_coord = (el[0]+1+x,el[1]-1-x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x,el[1]-1-x,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x,el[1]-1-x,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break


                        else: #S wall
                            #check for possible positions at ymin range from xmin to xmax
                            es = roll_dice(1,rxmax-rxmin + 1)
                            el = [rxmin + es -1,rymin]

                            if shape_dict['exitdirections'][e+1] == 'A':
                                for x in range(3):
                                    will_fit = in_dungeon((el[0],el[1]-1-x,rzmin))
                                    if not will_fit:
                                        dungeon[(el[0],el[1]-1-x,rzmin)] = {}
                                        dungeon[(el[0],el[1]-1-x,rzmin)]['fill'] = 'C'
                                        if take_exit == e+1: #dice 1, loop 0
                                            new_coord = ((el[0],el[1]-1-x,rzmin))       
                                    else:
                                        sd = roll_dice(1,20)
                                        if sd <= 5:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0],el[1]-1-x+1,rzmin)] = 'Y'
                                        elif sd >=6 and sd <=10:
                                            secret_door_count +=1 
                                            secret_door_dict[(el[0],el[1]-1-x+1,rzmin)] = 'OW'
                                        else:
                                            pass
                                        break


                            else: #shape_dict['exitdirections'][e+1]: #angled either way
                                which_way = roll_dice(1,2)           
                                if which_way == 1:  #corridor left
                                    for x in range(3):
                                        will_fit = in_dungeon((el[0]-1-x,el[1]-1-x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]-1-x,el[1]-1-x,rzmin)] = {}
                                            dungeon[(el[0]-1-x,el[1]-1-x,rzmin)]['fill'] = 'C'
                                            if which_way == 1:
                                                new_coord = (el[0]-1-x,el[1]+1+x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x+1,el[1]+1+x-1,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]-1-x+1,el[1]+1+x-1,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break
                                else:
                                    #secret doors here need to use the other sd procedures eventually
                                    for x in range(3): #corridor right
                                        will_fit = in_dungeon((el[0]+1+x,el[1]-1-x,rzmin))
                                        if not will_fit:                
                                            dungeon[(el[0]+1+x,el[1]-1-x,rzmin)] = {}
                                            dungeon[(el[0]+1+x,el[1]-1-x,rzmin)]['fill'] = 'C'
                                            if which_way == 2:
                                                new_coord = (el[0]+1+x,el[1]-1-x,rzmin)
                                        else:
                                            sd = roll_dice(1,20)
                                            if sd <= 5:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x-1,el[1]-1-x+1,rzmin)] = 'Y'
                                            elif sd >=6 and sd <=10:
                                                secret_door_count +=1 
                                                secret_door_dict[(el[0]+1+x-1,el[1]-1-x+1,rzmin)] = 'OW'
                                            else:
                                                pass
                                            break



                    #pass

            #check treasure, monsters, exits and place these
        #shape_dict['contents']['secret_door_dict'] = secret_door_dict if want to implement
        #shape_dict['contents']['secret_door_count'] = secret_door_count  #to place won't fit exits

            #exists need coloring for output so door/exit stack
        print("adding ROOM:",room_stack['key_count'],"to stack")
        room_stack['shape_dict'][room_stack['key_count']] = copy.deepcopy(shape_dict)
        return "GOOD"
    else:
        pass   #do we want a return

def loot(shape_dict,coord,monster="N"):
    #when coming from wet small or others with no initialisation
    if 'contents' not in shape_dict:
        shape_dict['contents'] = {}

    if 'treasure' not in shape_dict['contents']:
        shape_dict['contents']['treasure'] = {}

    shape_dict['contents']['treasure']['type'] = {}
    shape_dict['contents']['treasure']['type']['copper'] = 0
    shape_dict['contents']['treasure']['type']['silver'] = 0
    shape_dict['contents']['treasure']['type']['electrum'] = 0
    shape_dict['contents']['treasure']['type']['gold'] = 0
    shape_dict['contents']['treasure']['type']['platinum'] = 0
    shape_dict['contents']['treasure']['type']['gems'] = 0
    shape_dict['contents']['treasure']['type']['jewellery'] = 0
    shape_dict['contents']['treasure']['type']['magic'] = 0

    if monster == 'N':
        multi = 1
        rolls = 1
    else:
        multi = 1.1
        rolls = 2
    for t in range(rolls):        
        l = roll_dice(1,100)
        if l<=25:
            shape_dict['contents']['treasure']['type']['copper'] = shape_dict['contents']['treasure']['type']['copper'] + int(abs(coord[2]) * 1000* multi ) 
        elif l >= 26 and l <= 50:
            shape_dict['contents']['treasure']['type']['silver'] = shape_dict['contents']['treasure']['type']['silver'] + int(abs(coord[2]) * 1000* multi ) 
        elif l >= 51 and l <= 65:
            shape_dict['contents']['treasure']['type']['electrum'] = shape_dict['contents']['treasure']['type']['electrum'] + int(abs(coord[2]) * 750* multi ) 
        elif l >= 66 and l <= 80:
            shape_dict['contents']['treasure']['type']['gold'] = shape_dict['contents']['treasure']['type']['gold'] + int(abs(coord[2]) * 250* multi ) 
        elif l >= 81 and l <= 90:
            shape_dict['contents']['treasure']['type']['platinum'] = shape_dict['contents']['treasure']['type']['silver'] + int(abs(coord[2]) * 100* multi ) 
        elif l >= 91 and l <= 94:
            shape_dict['contents']['treasure']['type']['gems'] = shape_dict['contents']['treasure']['type']['gems'] + int(abs(coord[2]) * roll_dice(1,4)* multi ) 
        elif l >= 95 and l <= 97:
            shape_dict['contents']['treasure']['type']['jewellery'] = shape_dict['contents']['treasure']['type']['jewellery'] + int(abs(coord[2])* multi ) 
        else:
            shape_dict['contents']['treasure']['type']['magic']  += 1

        return shape_dict

def loot_store(shape_dict):
    l = roll_dice(1,20)
    if l <=2:
        shape_dict['contents']['treasure']['store'] = 'Bags'
    elif l >=3 and l<=4:
        shape_dict['contents']['treasure']['store'] = 'Sacks'
    elif l >=5 and l<=6:
        shape_dict['contents']['treasure']['store'] = 'Coffers'
    elif l >=7 and l<=8:
        shape_dict['contents']['treasure']['store'] = 'Chests'
    elif l >=9 and l<=10:
        shape_dict['contents']['treasure']['store'] = 'Bloody Great Chests'
    elif l >=11 and l<=12:
        shape_dict['contents']['treasure']['store'] = 'Clay Jars'
    elif l >=13 and l<=14:
        shape_dict['contents']['treasure']['store'] = 'Metal Urns'
    elif l >=15 and l<=16:
        shape_dict['contents']['treasure']['store'] = 'Stone Jars'
    elif l >=17 and l<=18:
        shape_dict['contents']['treasure']['store'] = 'Metal Trunks'
    else:
        shape_dict['contents']['treasure']['store'] = 'Loose'

    g = roll_dice(1,20)
    if g <=8:
        shape_dict['contents']['treasure']['protection'] = 'guard'
    else:
        shape_dict['contents']['treasure']['protection'] = 'hide'

    return shape_dict

def loot_guard(shape_dict):
    l = roll_dice(1,20)    
    if l<=2:
        shape_dict['contents']['treasure']['guard'] = 'Contact poison: container'
    elif l>=3 and l<=4:
        shape_dict['contents']['treasure']['guard'] = 'Contact poison: loot'
    elif l>=5 and l<=6:
        shape_dict['contents']['treasure']['guard'] = 'Poison needles: lock'
    elif l==7:
        shape_dict['contents']['treasure']['guard'] = 'Poison needles: handle'
    elif l==8:        
        shape_dict['contents']['treasure']['guard'] = 'Darts: front'
    elif l==9:                
        shape_dict['contents']['treasure']['guard'] = 'Darts: top'
    elif l==10:                
        shape_dict['contents']['treasure']['guard'] = 'Darts: inside bottom up'
    elif l>=11 and l<=12:
        shape_dict['contents']['treasure']['guard'] = 'Blade: across inside'
    elif l==13:                        
        p = roll_dice(1,4)
        if p == 1:
            shape_dict['contents']['treasure']['guard'] = 'Snakes: poison'
        elif p == 2:
            shape_dict['contents']['treasure']['guard'] = 'Lizards: poison'
        elif p == 3:
            shape_dict['contents']['treasure']['guard'] = 'Spiders: poison'
        else:
            shape_dict['contents']['treasure']['guard'] = 'Scorpions: poison'
    elif l==14:                                
        shape_dict['contents']['treasure']['guard'] = 'Gas'
    elif l==15:                                        
        shape_dict['contents']['treasure']['guard'] = 'Trapdoor: front'
    elif l==16:                                                
        shape_dict['contents']['treasure']['guard'] = 'Trapdoor: one square back'
    elif l==17:                                                        
        shape_dict['contents']['treasure']['guard'] = 'Stone Falls: Front'
    elif l==18:                                                                
        shape_dict['contents']['treasure']['guard'] = 'Spear trap: Walls'
    elif l==19:                                                                        
        shape_dict['contents']['treasure']['guard'] = 'Magic: Rune Boom'
    elif l==20:                                                                                
        shape_dict['contents']['treasure']['guard'] = 'Magic: Symbol'

    return shape_dict

def loot_hide(shape_dict):
    l = roll_dice(1,20)
    if l<=3:
        shape_dict['contents']['treasure']['hide'] = 'Magic: Invisibility'
    elif l>=4 and l<=5:
        shape_dict['contents']['treasure']['hide'] = 'Magic: Ilusion'
    elif l==6:                                                        
        shape_dict['contents']['treasure']['hide'] = 'Secret: Compartment under container'
    elif l>=7 and l<=8:
        shape_dict['contents']['treasure']['hide'] = 'Secret: Compartment'
    elif l==9:                                                        
        shape_dict['contents']['treasure']['hide'] = 'Secret: Inside non-storage item'
    elif l==10:                                                        
        shape_dict['contents']['treasure']['hide'] = 'Secret: Disguised as other'
    elif l==11:                                                        
        r = roll_dice(1,2)
        if r == 1:
            shape_dict['contents']['treasure']['hide'] = 'Secret: In rubbish'
        else:
            shape_dict['contents']['treasure']['hide'] = 'Secret: In poo'
    elif l>=12 and l<=13:
        shape_dict['contents']['treasure']['hide'] = 'Secret: Loose stone - under'
    elif l>=14 and l<=15:
        shape_dict['contents']['treasure']['hide'] = 'Secret: Loose stone - in wall'
    else:
        shape_dict['contents']['treasure']['hide'] = 'Secret room nearby'
        #make 10x10 thing?

    return shape_dict

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
            dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'st'

            dungeon[(coord[0],coord[1]+1,coord[2]-2)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-2)]['fill'] = 'st'
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
            dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'st'

            dungeon[(coord[0],coord[1]+1,coord[2]-2)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-2)]['fill'] = 'st'

            dungeon[(coord[0],coord[1]+1,coord[2]-3)] = {}
            dungeon[(coord[0],coord[1]+1,coord[2]-3)]['fill'] = 'st'
            new_coord = (coord[0],coord[1]+1,coord[2]-3)  ##1 in 20 closes
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

                dungeon[(coord[0],coord[1]+1,coord[2]+0)] = {}  ##this is the level down chute part
                dungeon[(coord[0],coord[1]+1,coord[2]+0)]['fill'] = 'ch'

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
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]-1))  #down 1#facing #need all the level will fits eventually
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

def bad_things(coord, room_stack, size="C"):
    '''
    option to have it concatenate to fill by passing other than size="C"
    still need to work out bad things for rooms in random spot
    '''

    #have to fill, need if coming from corridor or room
    new_coord = coord    
    #all traps located ahead plus 1?
    t_dict = {}
    t_dict['new_coord'] = new_coord
    t_dict['trap'] = {}
    t_dict['secretdoor'] = 'N'
    t_dict['trap']['type'] = 'secretdoor'
    t_dict['trap']['chance'] = 1.0
    t_dict['trap']['fits'] = 'N'
    t_dict['trap']['abv'] = ''  #default not fill with #will fit is for bad things

    if size == "C":
        will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))  #down 1#facing
        if not will_fit:                                                
            dungeon[(coord[0],coord[1]+1,coord[2])] = {}

            t = roll_dice(1,20)
            if t <= 5:
                t_dict['secretdoor'] == 'Y'
                s = roll_dice(1,20)
                t_dict['trap']['chance'] = 0.15
                t_dict['trap']['chance_elf'] = 0.25
                t_dict['trap']['damage'] = roll_dice(1,6)
                t_dict['trap']['type'] = 'secret door pit'
                t_dict['trap']['abv'] = 'pt'
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pt'
                else:
                    ## maybe below is not necessary?
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pt'
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'pt'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord
                ## do stuff for exits!!
            if t >= 6 and t <= 7:
                t_dict['trap']['type'] = 'pit'
                t_dict['trap']['abv'] = 'pi'
                t_dict['trap']['chance'] = 3.0/6.0
                t_dict['trap']['damage'] = roll_dice(1,6)
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'pi'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'pi'
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'pi' #get this to work later
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord            
            if t == 8:
                t_dict['trap']['type'] = 'pit'
                t_dict['trap']['abv'] = 'ps'
                t_dict['trap']['chance'] = 3.0/6.0
                t_dict['trap']['effect'] = 'spikes'
                t_dict['trap']['damage'] = roll_dice(2,6)
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ps'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'ps'
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
                    t_dict['trap']['abv'] = 'el'
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
                ##needs the top level to work as well, not at -1
                #for k in range(d):
                for k in range(d+1): #loop current level to end d0 is current               
                    for j in range(2):
                        for i in range(2):
                            #will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1))
                            will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]-k))
                            if not will_fit:                
                                #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)] = {}
                                dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k)] = {}
                                #no prefil here as a trap same as others
                                if size == "C":
                                    #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] = 'el'
                                    dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k)]['fill'] = 'el'
                                else:
                                    #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] = 'el'  #get to work later
                                    dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k)]['fill'] = 'el'  #get to work later
                                    #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] = dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] + 'el'
                                new_coord = (coord[0],coord[1]+3,coord[2]-k-1) #past elevator 2 and down
                            else:
                                break
            if t == 12:
                #12 Wall 10’ behind slides across passage blocking it for from 40-60 turns.
                t_dict['trap']['type'] = 'slidingwall'
                t_dict['trap']['abv'] = 'bw'
                t_dict['trap']['chance'] = roll_dice(1,20) + 40
                t_dict['trap']['effect'] = 'blocked'
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'bw'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'bw' #fill only bw fix later
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'bw'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord            
            if t == 13:
                t_dict['trap']['type'] = 'oil'
                t_dict['trap']['abv'] = 'ol'
                t_dict['trap']['chance'] = roll_dice(1,20) + 40
                t_dict['trap']['effect'] = 'random person'
                t_dict['trap']['damage'] = roll_dice(2,6)
                t_dict['trap']['save'] = 'magic'
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ol'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ol' #fill only ol fix later
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'ol'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord            
            if t == 14:
                t_dict['trap']['type'] = 'pit'
                t_dict['trap']['abv'] = 'pc'
                t_dict['trap']['chance'] = 3.0/6.0
                t_dict['trap']['effect'] = 'crush death'
                t_dict['trap']['damage'] = roll_dice(2,6)
                t_dict['trap']['duration'] = roll_dice(1,4) + 1
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'pc'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'pc' #get this to work for rooms
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'pc'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord            
            if t == 15:
                t_dict['trap']['type'] = 'arrow'
                t_dict['trap']['abv'] = 'ar'
                t_dict['trap']['chance'] = 0.05
                t_dict['trap']['damage'] = roll_dice(1,3)  * roll_dice(1,6)
                t_dict['trap']['save'] = 'poison'
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ar'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ar' #fill only ar fix later
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'ar'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord            
            if t == 16:
                t_dict['trap']['type'] = 'spear'
                t_dict['trap']['abv'] = 'sp'
                t_dict['trap']['chance'] = 0.05
                t_dict['trap']['damage'] = roll_dice(1,3)  * roll_dice(1,8)
                t_dict['trap']['save'] = 'poison'
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'sp'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] =  'sp'  #### got to make these more useful later
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'sp'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord            
            if t == 17:
                t_dict['trap']['type'] = 'gas'
                t_dict['trap']['abv'] = 'gs'
                t_dict['trap']['details'] = stinky()
                for key in t_dict['trap']['details']:
                    t_dict[key] = t_dict['trap']['details'][key]
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'gs'
                else:
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'gs'  #fill only gs
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'gs'
                new_coord = (coord[0],coord[1]+1,coord[2])
                t_dict['new_coord'] = new_coord            
            if t == 18:
                what_fall = roll_dice(1,2)
                if what_fall == 1:
                    t_dict['trap']['type'] = 'doorfalls'
                    t_dict['trap']['abv'] = 'df'
                    t_dict['trap']['chance'] = 0.05
                    t_dict['trap']['damage'] = roll_dice(1,10)
                    t_dict['trap']['save'] = 'petrification'
                    if size == "C":
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'df'
                    else:
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'df' #fill only df fix later
                        #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'df'
                    new_coord = (coord[0],coord[1]+1,coord[2])
                    t_dict['new_coord'] = new_coord                            
                else:
                    t_dict['trap']['type'] = 'stonefalls'
                    t_dict['trap']['abv'] = 'sf'
                    t_dict['trap']['chance'] = 0.05
                    t_dict['trap']['damage'] = roll_dice(2,10)
                    t_dict['trap']['save'] = 'petrification'
                    if size == "C":
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'sf'
                    else:
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'sf' #fill only sf fix later
                        #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'sf'
                    new_coord = (coord[0],coord[1]+1,coord[2])
                    t_dict['new_coord'] = new_coord                            
            if t == 19:
                t_dict['trap']['type'] = 'illusionarywall'
                w = roll_dice(1,20)
                if w <= 6:
                    t_dict['trap']['type'] = t_dict['trap']['type'] + 'pit'
                    t_dict['trap']['abv'] = 'pi'
                    t_dict['trap']['chance'] = 3.0/6.0
                    t_dict['trap']['damage'] = roll_dice(1,6)
                    if size == "C":
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pi'
                    else:
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'pi' #fill only pi fix later
                        #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'pi'
                    new_coord = (coord[0],coord[1]+1,coord[2])
                    t_dict['new_coord'] = new_coord
                elif w>=7 and w<=10:
                    t_dict['trap']['type'] = t_dict['trap']['type'] + 'chute'
                    t_dict['trap']['abv'] = 'ch'
                    t_dict['trap']['effect'] = 'one way'
                    dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
                    if size == "C":
                        dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'ch'  ##add chute down fill
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ch'
                    else:
                        dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] + 'ch'  ##add chute down fill
                        dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'ch'

                    new_coord = (coord[0],coord[1]+1,coord[2]-1)
                    t_dict['new_coord'] = new_coord
                else:
                    #pass put room here
                    shape_dict = room(coord, room_stack, content="MT") #if another room pass not C="R"  
                    #room_stack = shape_dict['room_stack']     
                    
                    #pass MT for monster and treasure
                    #each room part check for inside

                    print("ROOM SHAPE:",shape_dict)
                    rm = room_make(shape_dict, coord)
                    if rm == "GOOD":
                        secret_doors(shape_dict)                    


            if t == 20:        
                dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
                if size == "C":
                    dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'ch'  #fill down for chute
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ch'
                else:
                    #dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] + 'ch'  #fill down for chute
                    #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'ch'
                    dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'Rch'  #fill down for chute
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'Rch'

                new_coord = (coord[0],coord[1]+1,coord[2]-1)
                t_dict['trap']['type'] = 'chute'
                t_dict['trap']['effect'] = 'one way'
                t_dict['trap']['duration'] = 'permanent'
                t_dict['new_coord'] = new_coord

            t_dict['trap']['fits'] = 'Y'
    else:  #inside a room, things already created
        t = roll_dice(1,20)
        if t <= 5:
            t_dict['secretdoor'] == 'Y'
            s = roll_dice(1,20)
            t_dict['trap']['chance'] = 0.15
            t_dict['trap']['chance_elf'] = 0.25
            t_dict['trap']['damage'] = roll_dice(1,6)
            t_dict['trap']['type'] = 'secret door pit'
            t_dict['trap']['abv'] = 'pt'
        if t >= 6 and t <= 7:
            t_dict['trap']['type'] = 'pit'
            t_dict['trap']['abv'] = 'pi'
            t_dict['trap']['chance'] = 3.0/6.0
            t_dict['trap']['damage'] = roll_dice(1,6)
        if t == 8:
            t_dict['trap']['type'] = 'pit'
            t_dict['trap']['abv'] = 'ps'
            t_dict['trap']['chance'] = 3.0/6.0
            t_dict['trap']['effect'] = 'spikes'
            t_dict['trap']['damage'] = roll_dice(2,6)
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
                t_dict['trap']['abv'] = 'el'
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
            ##needs the top level to work as well, not at -1
            #for k in range(d):
            for k in range(d+1): #loop current level to end d0 is current               
                for j in range(2):
                    for i in range(2):
                        #will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1))
                        will_fit = in_dungeon((coord[0] + i + adjust,coord[1]+j+1,coord[2]-k))
                        if not will_fit:                
                            #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)] = {}
                            dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k)] = {}
                            #no prefil here as a trap same as others
                            if size == "C":
                                #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] = 'el'
                                dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k)]['fill'] = 'el'
                            else:
                                #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] = 'el'  #get to work later
                                dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k)]['fill'] = 'el'  #get to work later
                                #dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] = dungeon[(coord[0] + i + adjust,coord[1]+j+1,coord[2]-k-1)]['fill'] + 'el'
                            new_coord = (coord[0],coord[1]+3,coord[2]-k-1) #past elevator 2 and down
                        else:
                            break
        if t == 12:
            #12 Wall 10’ behind slides across passage blocking it for from 40-60 turns.
            t_dict['trap']['type'] = 'slidingwall'
            t_dict['trap']['chance'] = roll_dice(1,20) + 40
            t_dict['trap']['effect'] = 'blocked'
            t_dict['trap']['abv'] = 'bw'
        if t == 13:
            t_dict['trap']['type'] = 'oil'
            t_dict['trap']['abv'] = 'ol'
            t_dict['trap']['chance'] = roll_dice(1,20) + 40
            t_dict['trap']['effect'] = 'random person'
            t_dict['trap']['damage'] = roll_dice(2,6)
            t_dict['trap']['save'] = 'magic'
        if t == 14:
            t_dict['trap']['type'] = 'pit'
            t_dict['trap']['abv'] = 'pc'
            t_dict['trap']['chance'] = 3.0/6.0
            t_dict['trap']['effect'] = 'crush death'
            t_dict['trap']['damage'] = roll_dice(2,6)
            t_dict['trap']['duration'] = roll_dice(1,4) + 1
        if t == 15:
            t_dict['trap']['type'] = 'arrow'
            t_dict['trap']['abv'] = 'ar'
            t_dict['trap']['chance'] = 0.05
            t_dict['trap']['damage'] = roll_dice(1,3)  * roll_dice(1,6)
            t_dict['trap']['save'] = 'poison'
        if t == 16:
            t_dict['trap']['type'] = 'spear'
            t_dict['trap']['abv'] = 'sp'
            t_dict['trap']['chance'] = 0.05
            t_dict['trap']['damage'] = roll_dice(1,3)  * roll_dice(1,8)
            t_dict['trap']['save'] = 'poison'
        if t == 17:
            t_dict['trap']['type'] = 'gas'
            t_dict['trap']['abv'] = 'gs'
            t_dict['trap']['details'] = stinky()
            for key in t_dict['trap']['details']:
                t_dict[key] = t_dict['trap']['details'][key]
        if t == 18:
            what_fall = roll_dice(1,2)
            if what_fall == 1:
                t_dict['trap']['type'] = 'doorfalls'
                t_dict['trap']['abv'] = 'df'
                t_dict['trap']['chance'] = 0.05
                t_dict['trap']['damage'] = roll_dice(1,10)
                t_dict['trap']['save'] = 'petrification'
            else:
                t_dict['trap']['type'] = 'stonefalls'
                t_dict['trap']['abv'] = 'sf'
                t_dict['trap']['chance'] = 0.05
                t_dict['trap']['damage'] = roll_dice(2,10)
                t_dict['trap']['save'] = 'petrification'
        if t == 19:
            t_dict['trap']['type'] = 'illusionarywall'
            w = roll_dice(1,20)
            if w <= 6:
                t_dict['trap']['type'] = t_dict['trap']['type'] + 'pit'
                t_dict['trap']['abv'] = 'pi'
                t_dict['trap']['chance'] = 3.0/6.0
                t_dict['trap']['damage'] = roll_dice(1,6)
            elif w>=7 and w<=10:
                t_dict['trap']['type'] = t_dict['trap']['type'] + 'chute'
                t_dict['trap']['abv'] = 'ch'
                t_dict['trap']['effect'] = 'one way'
                dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
            else:
                #pass put room here
                shape_dict = room(coord, room_stack, content="MT") #if another room pass not C="R"  
                #room_stack = shape_dict['room_stack']     
                
                #pass MT for monster and treasure
                #each room part check for inside

                print("ROOM SHAPE:",shape_dict)
                rm = room_make(shape_dict, coord)
                if rm == "GOOD":
                    secret_doors(shape_dict)                    


        if t == 20:        
            dungeon[(coord[0],coord[1]+1,coord[2]-1)] = {}
            if size == "C":
                dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'ch'  #fill down for chute
                dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'ch'
            else:
                #dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] + 'ch'  #fill down for chute
                #dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] + 'ch'
                dungeon[(coord[0],coord[1]+1,coord[2]-1)]['fill'] = 'Rch'  #fill down for chute
                dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'Rch'

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

def fancy_cave(coord):
    '''
    maybe combine in room? pass 'CAVE
    '''
    c = roll_dice(1,20)

def wet_small(shape_dict, coord):
    #not implemented yet
    w = roll_dice(1,20)
    print("WET SMALL ROLL:",w)
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
        wet_dict['monster_details'] = {}
        wet_dict['monster_details']['level'] = level_matrix(abs(coord[2]))
        wet_dict['monster_details']['type'] = 'NA'
        wet_dict['monster_details']['No'] = 0
        wet_dict['monster_details'] = 0

    elif w >= 13 and w <=18:
        wet_dict['wet'] = 'Y'
        wet_dict['monster'] = 'Y'
        wet_dict['monster_details'] = {}
        wet_dict['monster_details']['level'] = level_matrix(abs(coord[2]))
        wet_dict['monster_details']['type'] = 'NA'
        wet_dict['monster_details']['No'] = 0
        wet_dict['monster_details'] = 0

        wet_dict['treasure'] = 'Y'

        shape_dict = loot(shape_dict,coord,monster="Y")
        shape_dict = loot_store(shape_dict)
        
        if shape_dict['contents']['treasure']['protection'] == 'guard':
            shape_dict = loot_guard(shape_dict)
        else:
            shape_dict = loot_hide(shape_dict)

    else:
        wet_dict['magic'] = 'Y'
        shape_dict = wet_magic(shape_dict)

    if 'pool' not in shape_dict:
        shape_dict['pool'] = ''
        shape_dict['pool'] = wet_dict

    return shape_dict


def wet_large(shape_dict, coord):
    #not implemented yet
    w = roll_dice(1,20)
    print("WET LARGE ROLL:",w)
    wet_dict = {}
    wet_dict['wet'] = 'N'
    wet_dict['monster'] = 'N'
    wet_dict['treasure'] = 'N'
    wet_dict['magic'] = 'N'

    if w <= 10:
        pass
    elif w >= 11 and w <=15:
        shape_dict['water'] = 'L' #lake
        wet_dict['wet'] = 'Y'
        shape_dict['lake'] = wet_dict
    elif w >= 16 and w <=18:
        shape_dict['water'] = 'L'
        wet_dict['wet'] = 'Y'
        wet_dict['monster'] = 'Y' #as per encounter
        wet_dict['monster_details'] = {}
        wet_dict['monster_details']['level'] = level_matrix(abs(coord[2]))
        wet_dict['monster_details']['type'] = 'NA'
        wet_dict['monster_details']['No'] = 0
        wet_dict['monster_details'] = 0

        shape_dict['lake'] = wet_dict
    else:
        shape_dict['water'] = 'L'
        wet_dict['magic'] = 'Y'  #portal to another realm/world/dungeon23
        shape_dict['wet_magic'] = wet_dict
        shape_dict['lake'] = wet_dict
        m = roll_dice(1,20)
        if m <= 18:
            wet_dict['monster'] = 'Y'
            wet_dict['monster_details'] = {}
            wet_dict['monster_details']['level'] = level_matrix(abs(coord[2]))
            wet_dict['monster_details']['type'] = 'NA'
            wet_dict['monster_details']['No'] = 0
            wet_dict['monster_details'] = 0

            ##need to monster generate

            shape_dict = loot(shape_dict,coord,monster="Y")
            shape_dict = loot_store(shape_dict)
            
            if shape_dict['contents']['treasure']['protection'] == 'guard':
                shape_dict = loot_guard(shape_dict)
            else:
                shape_dict = loot_hide(shape_dict)

            wet_dict['portal'] = 'another world/dungeon23/other place'
            #otherwise can be monster, but above is more fun unless solo or could random

        shape_dict['lake'] = wet_dict

    return shape_dict


def wet_magic(shape_dict):
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
        s = roll_dice(1,3)
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
            #100 miles away or effectively could be exit program
            new_coord = (0,0,0)
    
    shape_dict['wet_magic'] = wet_magic_dict
    return shape_dict

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


def secret_doors(shape_dict):

    if 'secret_door_count' in room_stack['shape_dict'][room_stack['key_count']]['contents']:
        secret_door_count = room_stack['shape_dict'][room_stack['key_count']]['contents']['secret_door_count']
        secret_door_dict = room_stack['shape_dict'][room_stack['key_count']]['contents']['secret_door_dict']

        print("\ncalling SD", room_stack, "\n")
    
        #loop through the secret doors  #just rest rooms first
        #somewhere in this loop is a problem
        for s in range(secret_door_count):
            print("\nSECRET DOOR CHECK", s)
            for key in secret_door_dict[s + 1]: #room integers 1 onwards
                print("key for secret_door_dict[s + 1]", key, "value:", secret_door_dict[s + 1][key])

                if 'loc' in secret_door_dict[s + 1][key]:
                    usedir = secret_door_dict[s + 1][key]['loc']
                    #key is the location
                    #want a reduced exit_result
                    #exit dir full won't work here as does not have a facing as for dead end corridor
                    if secret_door_dict[s + 1][key]['beyond'] == 'Room':
                        print("in secret door room and rolling")
                        new_coord = secret_door_dict[s + 1][key]
                        #shape_dict = room(secret_door_dict[s + 1][key], room_stack, size='R' )  ## different type to get slightly different table
                        print("room stack before", room_stack)
                        shape_dict = room(key, room_stack, size='R' )  ## different type to get slightly different table
                        print("room stack after", room_stack)

                        print("SECRETDOORDICT",secret_door_dict)
                        print("NEW_COORD",new_coord, "KEY:",key)
                        print("SHAPEDICTSD",shape_dict)

                        print("ROOM SHAPE ROOM SD:",shape_dict)
                        ## do simple version first of x directions and y directions of rectangular
                        print("params for room_make call", shape_dict, key)
                        ##room_make(shape_dict, key)
                        
                        rm = room_make(shape_dict, key, size="R")  ##right value here - pass R for room to get it to not adjust y plot
                        if rm == "GOOD":
                            secret_doors(shape_dict)                    

                    elif secret_door_dict[s + 1][key]['beyond'] == '45AB' or secret_door_dict[s + 1][key]['beyond'] == '45BA':
                        print("in secret door passage 45 ahead - only want to go one direction")

                        if usedir == 'xminloc':
                            which_way = roll_dice(1,2)           
                            if which_way == 1:  #corridor left
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]-x,key[1]+x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]-x,key[1]+x,key[2])] = {}
                                        dungeon[(key[0]-x,key[1]+x,key[2])]['fill'] = 'C'
                                    else:
                                        break
                            else:
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]-x,key[1]-x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]-x,key[1]-x,key[2])] = {}
                                        dungeon[(key[0]-x,key[1]-x,key[2])]['fill'] = 'C'
                                    else:
                                        break

                        elif usedir == 'xmaxloc': 
                            which_way = roll_dice(1,2)           
                            if which_way == 1:  #corridor right
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]+x,key[1]+x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]+x,key[1]+x,key[2])] = {}
                                        dungeon[(key[0]+x,key[1]+x,key[2])]['fill'] = 'C'
                                    else:
                                        break
                            else: #corridor left
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]+x,key[1]-x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]+x,key[1]-x,key[2])] = {}
                                        dungeon[(key[0]+x,key[1]-x,key[2])]['fill'] = 'C'
                                    else:
                                        break

                        elif usedir == 'yminloc':                             
                            which_way = roll_dice(1,2)           
                            if which_way == 1:  #corridor left
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]-x,key[1]-x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]-x,key[1]-x,key[2])] = {}
                                        dungeon[(key[0]-x,key[1]-x,key[2])]['fill'] = 'C'
                                    else:
                                        break
                            else: #corridor right
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]+x,key[1]-x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]+x,key[1]-x,key[2])] = {}
                                        dungeon[(key[0]+x,key[1]-x,key[2])]['fill'] = 'C'
                                    else:
                                        break

                        else: #ymaxloc
                            which_way = roll_dice(1,2)           
                            if which_way == 1:  #corridor right
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]-x,key[1]+x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]-x,key[1]+x,key[2])] = {}
                                        dungeon[(key[0]-x,key[1]+x,key[2])]['fill'] = 'C'
                                    else:
                                        break
                            else: #corridor left
                                for x in range(3):
                                    will_fit = in_dungeon((key[0]+x,key[1]+x,key[2]))
                                    if not will_fit:                
                                        dungeon[(key[0]+x,key[1]+x,key[2])] = {}
                                        dungeon[(key[0]+x,key[1]+x,key[2])]['fill'] = 'C'
                                    else:
                                        break

                    elif secret_door_dict[s + 1][key]['beyond'] == 'A':                    
                        print("in secret door passage ahead")
                        if usedir == 'xminloc':
                            for x in range(3): #here 0 is already 1 past
                                will_fit = in_dungeon((key[0]-x,key[1],key[2]))
                                if not will_fit:                
                                    dungeon[(key[0]-x,key[1],key[2])] = {}
                                    dungeon[(key[0]-x,key[1],key[2])]['fill'] = 'C'
                                else:
                                    break
                        elif usedir == 'xmaxloc':                             
                            for x in range(3):
                                will_fit = in_dungeon((key[0]+x,key[1],key[2]))
                                if not will_fit:                
                                    dungeon[(key[0]+x,key[1],key[2])] = {}
                                    dungeon[(key[0]+x,key[1],key[2])]['fill'] = 'C'
                                else:
                                    break
                        elif usedir == 'yminloc':                             
                            for x in range(3):
                                will_fit = in_dungeon((key[0],key[1]-x,key[2]))
                                if not will_fit:                
                                    dungeon[(key[0],key[1]-x,key[2])] = {}
                                    dungeon[(key[0],key[1]-x,key[2])]['fill'] = 'C'
                                else:
                                    break
                        else: #ymaxloc
                            for x in range(3):
                                will_fit = in_dungeon((key[0],key[1]+x,key[2]))
                                if not will_fit:                
                                    dungeon[(key[0],key[1]+x,key[2])] = {}
                                    dungeon[(key[0],key[1]+x,key[2])]['fill'] = 'C'
                                else:
                                    break

                    else: #'P'                                        
                        print("in secret door parallel passage")

                        ##need to make square straight in front as well
                        if usedir == 'xminloc' or usedir == 'xmaxloc':
                            will_fit = in_dungeon(key)  #original located
                            if not will_fit:
                                dungeon[key] = {}
                                dungeon[key]['fill'] = 'C'

                            for x in range(3):
                                will_fit = in_dungeon((key[0],key[1]-x-1,key[2]))
                                if not will_fit:
                                    dungeon[(key[0],key[1]-x-1,key[2])] = {}
                                    dungeon[(key[0],key[1]-x-1,key[2])]['fill'] = 'C'
                            for x in range(3):
                                will_fit = in_dungeon((key[0],key[1]+x+1,key[2]))
                                if not will_fit:
                                    dungeon[(key[0],key[1]+x+1,key[2])] = {}
                                    dungeon[(key[0],key[1]+x+1,key[2])]['fill'] = 'C'

                        else: #y
                            will_fit = in_dungeon(key)  #original located
                            if not will_fit:
                                dungeon[key] = {}
                                dungeon[key]['fill'] = 'C'

                            for x in range(3):
                                will_fit = in_dungeon((key[0]-x-1,key[1],key[2]))
                                if not will_fit:
                                    dungeon[(key[0]-x-1,key[1],key[2])] = {}
                                    dungeon[(key[0]-x-1,key[1],key[2])]['fill'] = 'C'
                            for x in range(3):
                                will_fit = in_dungeon((key[0]+x+1,key[1],key[2]))
                                if not will_fit:
                                    dungeon[(key[0]+x+1,key[1],key[2])] = {}
                                    dungeon[(key[0]+x+1,key[1],key[2])]['fill'] = 'C'


def exit_direction_full(coord, e_dict):
    print("EDF EDICT:",e_dict)
    if e_dict['direction'] == 'L':
        if e_dict['type'] == 'N':
            exit_stack[(coord[0]-1,coord[1],coord[2])] = {}
            if e_dict['beyond'] == 'P':
                for x in range(3):
                    will_fit = in_dungeon((coord[0]-1,coord[1]+x-1,coord[2]))
                    if not will_fit:
                        dungeon[(coord[0]-1,coord[1]+x-1,coord[2])] = {}
                        if x != 0:
                            dungeon[(coord[0]-1,coord[1]+x-1,coord[2])]['fill'] = 'C'
                        else:
                            dungeon[(coord[0]-1,coord[1]+x-1,coord[2])]['fill'] = 'Cd'
                        new_coord = (coord[0]-1,coord[1]+x-1,coord[2])
                for x in range(3):
                    will_fit = in_dungeon((coord[0]-1,coord[1]+x+1,coord[2]))
                    if not will_fit:
                        dungeon[(coord[0]-1,coord[1]+x+1,coord[2])] = {}
                        if x != 0:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'C'
                        else:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'Cd'
                        new_coord = (coord[0]-1,coord[1]+x+1,coord[2])

            if e_dict['beyond'] == 'A':              
                d = roll_dice(1,20)              
                if d >=3 and d <= 5:
                    will_fit = in_dungeon((coord[0]-1,coord[1],coord[2]))
                    if not will_fit:
                        exit_stack[(coord[0]-1,coord[1],coord[2])] = {}
                else:
                    #30m passage that direction
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-x-1,coord[1],coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]-x-1,coord[1],coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]-x-1,coord[1],coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-x-1,coord[1],coord[2])]['fill'] = 'Cd'
                            new_coord = ((coord[0]-x-1,coord[1],coord[2]))                        


            if e_dict['beyond'] == '4AB':   ##45 A
                which_way = roll_dice(1,2)           
                if which_way == 1:  #corridor left
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                            if which_way == 1:
                                new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                        else:
                            break
                else:
                    for x in range(3): #corridor right
                        will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                            if which_way == 2:
                                new_coord = (coord[0]+1+x,coord[1]+1+x,coord[2])
                        else:
                            break

            if e_dict['beyond'] == '4BA':   ##45 A
                which_way = roll_dice(1,2)  #work out random direction         
                if which_way == 1:  #corridor left
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1-x,coord[1]-1-x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                            if which_way == 1:
                                new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                        else:
                            break
                else:
                    for x in range(3): #corridor right
                        will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                            if which_way == 2:
                                new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                        else:
                            break

            if e_dict['beyond'] == 'Room':
                #want those we randomly position lr
                new_coord = coord
                #new part!
                #if coming from here pass door to room function?
                #dungeon[coord]['fill'] = dungeon[coord]['fill'] + 'd'  #add door indicator

                shape_dict = room(coord, room_stack, size='Rd' )  ## different type to get slightly different table pass Rd to indicate from door
                #room_stack = shape_dict['room_stack']
                #each room part check for inside

                print("ROOM SHAPE:",shape_dict)
                ## do simple version first of x directions and y directions of rectangular
                rm = room_make(shape_dict, coord)
                if rm == "GOOD":
                    secret_doors(shape_dict)                    


    elif e_dict['direction'] == 'R':
        if e_dict['type'] == 'N':
            exit_stack[(coord[0]+1,coord[1],coord[2])] = {}
            if e_dict['beyond'] == 'P':
                for x in range(3):
                    will_fit = in_dungeon((coord[0]+x-1,coord[1],coord[2]))
                    if not will_fit:
                        dungeon[(coord[0]+1,coord[1]+x-1,coord[2])] = {}
                        if x != 0:
                            dungeon[(coord[0]+1,coord[1]+x-1,coord[2])]['fill'] = 'C'
                        else:
                            dungeon[(coord[0]+1,coord[1]+x-1,coord[2])]['fill'] = 'Cd'
                        new_coord = (coord[0]+1,coord[1]+x-1,coord[2])
                for x in range(3):
                    will_fit = in_dungeon((coord[0]-1,coord[1]+x+1,coord[2]))
                    if not will_fit:
                        dungeon[(coord[0]-1,coord[1]+x+1,coord[2])] = {}
                        if x != 0:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'C'
                        else:
                            dungeon[(coord[0]-1,coord[1]+x+1,coord[2])]['fill'] = 'Cd'
                        new_coord = (coord[0]-1,coord[1]+x+1,coord[2])

            if e_dict['beyond'] == 'A':              
                d = roll_dice(1,20)              
                if d >=3 and d <= 5:
                    will_fit = in_dungeon((coord[0]+1,coord[1],coord[2]))
                    if not will_fit:
                        exit_stack[(coord[0]+1,coord[1],coord[2])] = {}
                else:
                    #30m passage that direction
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-x-1,coord[1],coord[2]))
                        if not will_fit:
                            dungeon[(coord[0]+x+1,coord[1],coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]+x+1,coord[1],coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+x+1,coord[1],coord[2])]['fill'] = 'Cd'
                            new_coord = ((coord[0]+x+1,coord[1],coord[2]))      

            if e_dict['beyond'] == '4AB':   ##45 A - need to make facing for R different eventually
                which_way = roll_dice(1,2)           
                if which_way == 1:  #corridor left
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                            if which_way == 1:
                                new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                        else:
                            break
                else:
                    for x in range(3): #corridor right
                        will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                            if x!= 0:
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
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
                            if x!= 0:
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                            if which_way == 1:
                                new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                        else:
                            break
                else:
                    for x in range(3): #corridor right
                        will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                            if x!= 0:
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                            if which_way == 2:
                                new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                        else:
                            break

            if e_dict['beyond'] == 'Room':
                #want those we randomly position lr
                new_coord = coord
                #dungeon[coord]['fill'] = dungeon[coord]['fill'] + 'd'  #add door indicator
                ## check for room or chamber
                rt = roll_dice(1,10)
                if rt <=8:
                    #room
                    shape_dict = room(coord, room_stack,size='Rd')  ## different type to get slightly different table indicate room from door
                else:
                    #chamber
                    shape_dict = room(coord, room_stack)
                #each room part check for inside

                print("ROOM SHAPE:",shape_dict)
                rm = room_make(shape_dict, coord)
                if rm == "GOOD":
                    secret_doors(shape_dict)                    

            
    else:  #final branch ahead
        if e_dict['type'] == 'N':
            exit_stack[(coord[0],coord[1]+1,coord[2])] = {}
            if e_dict['beyond'] == 'P':
                will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))
                if not will_fit:
                    dungeon[(coord[0],coord[1]+1,coord[2])] = {}
                    dungeon[(coord[0],coord[1]+1,coord[2])]['fill'] = 'Rd'
                    new_coord = (coord[0],coord[1]+1,coord[2])
                    # 10 x 10 room need to check contents!

                    #need to implement for set type room
                    new_coord = coord
                    shape_dict = room(coord, room_stack, size="10") #10 is special case to mandate 1 roll for size

                    print("ROOM SHAPE:",shape_dict)
                    rm = room_make(shape_dict, coord)
                    if rm == "GOOD":
                        secret_doors(shape_dict)                    

            ### previously not in missing problem
            if e_dict['beyond'] == 'A':              
                d = roll_dice(1,20)              
                if d >=3 and d <= 5:
                    will_fit = in_dungeon((coord[0],coord[1]+1,coord[2]))
                    if not will_fit:
                        exit_stack[(coord[0],coord[1]+1,coord[2])] = {}
                else:
                    #30m passage that direction
                    for x in range(3):
                        will_fit = in_dungeon((coord[0],coord[1]+x+1,coord[2]))
                        if not will_fit:
                            dungeon[(coord[0],coord[1]+x+1,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0],coord[1]+x+1,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0],coord[1]+x+1,coord[2])]['fill'] = 'Cd'
                            new_coord = ((coord[0],coord[1]+x+1,coord[2]))                        


            if e_dict['beyond'] == '4AB':   ##45 A
                which_way = roll_dice(1,2)           
                if which_way == 1:  #corridor left
                    for x in range(3):
                        will_fit = in_dungeon((coord[0]-1-x,coord[1]+1+x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1-x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
                            if which_way == 1:
                                new_coord = (coord[0]-1-x,coord[1]+1+x,coord[2])
                        else:
                            break
                else:
                    for x in range(3): #corridor right
                        will_fit = in_dungeon((coord[0]+1+x,coord[1]+1+x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+1+x,coord[1]+1+x,coord[2])]['fill'] = 'Cd'
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
                            if x != 0:
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]-1-x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                            if which_way == 1:
                                new_coord = (coord[0]-1-x,coord[1]-1-x,coord[2])
                        else:
                            break
                else:
                    for x in range(3): #corridor right
                        will_fit = in_dungeon((coord[0]+1+x,coord[1]-1-x,coord[2]))
                        if not will_fit:                
                            dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])] = {}
                            if x != 0:
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'C'
                            else:
                                dungeon[(coord[0]+1+x,coord[1]-1-x,coord[2])]['fill'] = 'Cd'
                            if which_way == 2:
                                new_coord = (coord[0]+1+x,coord[1]-1-x,coord[2])
                        else:
                            break

            if e_dict['beyond'] == 'Room':
                #want those we randomly position lr
                new_coord = coord
                #new part!
                #if coming from here pass door to room function?
                #dungeon[coord]['fill'] = dungeon[coord]['fill'] + 'd'  #add door indicator

                shape_dict = room(coord, room_stack, size='Rd' )  ## different type to get slightly different table pass Rd to indicate from door
                #room_stack = shape_dict['room_stack']
                #each room part check for inside

                print("ROOM SHAPE:",shape_dict)
                ## do simple version first of x directions and y directions of rectangular
                rm = room_make(shape_dict, coord)
                if rm == "GOOD":
                    secret_doors(shape_dict)                    

def monster_check(level, monster):
    lst = monster[level]
    r = roll_dice(1,20)
    print("MONSTER LEVEL ROLL:",r)
    for index, l in enumerate(lst):
        if index == 0:
            if r <= lst[index]:
                return(index+1)
        else:
            if r <= lst[index] and r > lst[index-1]:
                return(index+1)

def level_matrix(level):
    '''
    level is level of the dungeon
    '''
    print("MONSTER LEVEL MATRIX:", level)

    monster = {}
    monster[1] = [16,19,20]
    monster[2] = [12,16,18,19,20]
    monster[3] = [12,16,18,19,20]
    monster[4] = [5,6,16,18,19,20]
    monster[5] = [3,6,12,16,18,19,20]
    monster[6] = [2,4,6,12,16,18,19,20]
    monster[7] = [1,3,5,10,14,16,18,19,20]
    monster[8] = [1,2,4,7,10,14,16,18,19,20]
    monster[9] = [1,2,3,5,8,12,15,17,19,20]
    monster[10] = [1,2,3,4,6,9,12,16,19,20]
    monster[11] = [1,2,3,4,6,9,12,16,19,20]
    monster[12] = [1,2,3,4,5,7,9,12,18,20]
    monster[13] = [1,2,3,4,5,7,9,12,18,20]
    monster[14] = [1,2,3,4,5,6,8,11,17,20]
    monster[15] = [1,2,3,4,5,6,8,11,17,20]
    monster[16] = [1,2,3,4,5,6,7,10,16,20]

    if level < 1:
        #edge case of adventuring up on 0 level
        monster_level = monster_check(1, monster)
    if level >= 1 and level <=16:                        
        monster_level = monster_check(level, monster)
    else:
        monster_level = monster_check(16, monster)

    return monster_level


#need data structure
#do we have an exit order stack?
#array of corridors and walls, where corridor can be room/staircase etc odd corridor, even wall
#how big a fake canvas to make - or do we just have a dictionary and add parts in as they go
#eg have 1000 x 1000 and fake easting and northing
#direction preference - n,w,e,s? - roll randomly?

#not checking to backtrack the exit stack if dead-end
#not checking any level stacks to go up down, similarly
#not implemented passage width as yet - default only

from monsters import testmonster
from treasure import testtreasure
print (testmonster() + ' ' + testtreasure())
#print(testtreasure())


PERIODIC_CHECKS = 1  #number of rolls to make before stopping algorithm  #don't count first one down

if len(ARGV) > 1:
    if int(ARGV[1]) > 1:
        PERIODIC_CHECKS = int(ARGV[1])

    
#make this a script argument
START_LEVEL = 0

#above maybe also add to dungeon coordinates instead?
#function as counters to add keys?

exit_stack = {}  #only non-dead ends etc?

##add room key as identifier
door_stack= {}
level_stack = {}
room_stack = {}
room_stack['key_count'] = 0
room_stack['shape_dict'] = {}

trap_stack = {}

##add room key as identifier
wandering_monster_stack = {}
wandering_monster_stack['key_count'] = 0

monster_stack = {}
dead_end_dict = {}

error_dict = {}
error_dict['key_count'] = 0
error_dict['type'] = {}

water_dict = {}
#make water log as need to run a lot to get one and can't scroll that far

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
print("SETUP: roll_first", roll_first)
#no possible dead_end on first action
while roll_first == 18:
    roll_first = random_check()


first_action = check_action(roll_first, coord, room_stack)    

i = 0
result_coord = first_action
print("END SETUP:",)

while i < PERIODIC_CHECKS:
    print("\n--- ROLL:",i," ---\n")
    roll_first = random_check()
    result_coord = check_action(roll_first, result_coord, room_stack)
    print("\n--- END ROLL:",i," ---\n")
    i +=1
    

coord_lim = coord_limits(dungeon)
xmin = coord_lim[0][0]
ymin = coord_lim[0][1]
zmin = coord_lim[0][2]
xmax = coord_lim[1][0]
ymax = coord_lim[1][1]
zmax = coord_lim[1][2]

xwidth = xmax - xmin + 1
ywidth = ymax - ymin + 1
zwidth = zmax - zmin + 1

zwidth = max(1, zwidth)

print("\n --- FINAL OUTPUT ---")
print("MIN:",xmin,ymin,zmin)
print("MAX:",xmax,ymax,zmax)

print("COORD:", coord, result_coord, coord_lim)

print("\nDUNGEON:", dungeon)
print("\nEXIT_STACK:", exit_stack)
print("\nLEVEL_STACK:", level_stack)
print("\nROOM_STACK:", room_stack)

#can handle up to 4 characters
#map chararray to independent for each level
## ignore any random tiny up level things for now on chimneys or trapdoros
downlist = []
print("\nLEVELS DOWN:",zwidth-1)
for down in range(zwidth-1):
    print("downloop:",down)
    chararray = np.full((xwidth,ywidth,1), 'B', dtype='U10')
    print("SHAPE",chararray.shape)
    for key in dungeon:
        #print("KEY:",key,"KEYWIDTH:",key[0]+xwidth-1,key[1]+ywidth-1,key[2]+zwidth-1)
        #print("KEY:",key,"KEYWIDTH:",key[0]+xmax-key[0],key[1]+ymax-key[1],key[2]+zmax - key[2])
        
        if key[2] == (0 - down -1): #-1, -2, etc
            if 'fill' in dungeon[key] :  
                print("KEY:",key,"KEYWIDTH:",key[0]+xmin*-1,key[1]+ymin*-1,key[2]+zmin*-1,dungeon[key]['fill'])
                #chararray[[key][0],key[1],key[2]] = dungeon[key]['fill']
                #chararray[key[0]+xmax-key[0],key[1]+ymax-key[1],key[2]+zmax - key[2]] = dungeon[key]['fill']
                chararray[key[0]+xmin*-1,key[1]+ymin*-1,0] = dungeon[key]['fill']
            else:
                print("KEY:",key,"KEYWIDTH:",key[0]+xmin*-1,key[1]+ymin*-1,key[2]+zmin*-1)
    downlist.append(chararray)

    #only for first level        
    if down == 0:
        #print("START CHECK")
        #possible bug here
        #chararray[0+xmin*-1,0+ymin*-1,0+zmax*-1] = 'O'        
        chararray[0+xmin*-1,0+ymin*-1,0] = 'O'          ##first thing and has only one z level
        #print("START CHECK",chararray[0+xmin*-1,0+ymin*-1,0+zmin],0+xmin*-1,0+ymin*-1,-1)
    #print(chararray)
    #need a multi-level maker, this is just doing first for now
    #Each side can be set individually using border-top-color, border-right-color, border-bottom-color, and border-left-color; or using the writing mode-aware border-block-start-color, border-block-end-color, border-inline-start-color, and border-inline-end-color.
    #make dungeon html
    #            

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
            width:auto
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
        .grey_background {
                background-color: grey;
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

        divl {
            border-left-style: dotted
        }            
        divr {
            border-right-style: dotted
        }            
        divt {
            border-top-style: dotted
        }            
        divb {
            border-bottom-style: dotted
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
    strend = '''
    </body>
    </html>
    '''

    legend_dict =  {}
    legend_dict['O'] = "Outside Entrance"
    legend_dict['C'] = "Corridor/Passage"
    legend_dict['R'] = "Chamber/Room"
    legend_dict['D'] = "Dead End"
    legend_dict['CH'] = "Chasm"
    legend_dict['ri'] = "river"
    legend_dict['br'] = "bridge"
    legend_dict['bo'] = "boat - opposide side"
    legend_dict['bn'] = "boat - near side"
    legend_dict['L'] = "Lake"
    legend_dict['P'] = "Pool"
    legend_dict['W'] = "Well"
    legend_dict['S'] = "Shaft"
    legend_dict['d'] = "door"
    legend_dict[':'] = "direction of Door"
    legend_dict['wm'] = "Wandering Monster"
    legend_dict['sd'] = "Secret Door"
    legend_dict['st'] = "Stairs"
    legend_dict['ch'] = "Chute"
    legend_dict['cm'] = "Chimney"
    legend_dict['td'] = "Trapdoor"
    legend_dict['pi'] = "Pit Trap"
    legend_dict['pt'] = "Pit Trap: Secret Door"
    legend_dict['ps'] = "Pit Trap: Spikes"
    legend_dict['pc'] = "Pit Trap: Crushing Walls"
    legend_dict['el'] = "Elevator Trap"
    legend_dict['ar'] = "Arrow Trap"
    legend_dict['sp'] = "Spear Trap"
    legend_dict['df'] = "Door Falls Trap"
    legend_dict['sf'] = "Stone Falls Trap"
    legend_dict['gs'] = "Gas Trap"
    legend_dict['bw'] = "Blocked Wall Trap"
    legend_dict['ol'] = "Oil Trap"
    legend_dict['m'] = "Monster"
    legend_dict['t'] = "Treasure"
    legend_dict['p'] = "Pool"
    legend_dict['c'] = "Treasure: Copper"  
    legend_dict['s'] = "Treasure: Silver"
    legend_dict['e'] = "Treasure: Electrum"
    legend_dict['g'] = "Treasure: Gold"
    legend_dict['p'] = "Treasure: Platinum"
    legend_dict['G'] = "Treasure: Gems"
    legend_dict['j'] = "Treasure: Jewellery"
    legend_dict['M'] = "Treasure: Magic"

    background_dict = {}
    background_dict['black'] = 'nothing'
    background_dict['green'] = 'outside entrance'
    background_dict['blue'] = 'water'
    background_dict['red'] = 'bad_things'
    background_dict['white'] = 'corridor/passage'
    background_dict['brown'] = 'dead end'

    strlegendhead = '''
    <table>
    <th>Key</th>
    <th>Explanation</th>
    '''
    
    def colorcheck(dungeonstr):
        '''
        html coloring for copper, silver, electrum, gold, platinum, Gems, jewellery, Magic
        '''

        if 'c' in dungeonstr:
            return '#B87333'
        elif 'g' in dungeonstr:
            return '#FFD700'
        elif 'p' in dungeonstr:
            return '#E5E4E2'
        elif 'e' in dungeonstr:
            return '#E7G697'
        elif 'G' in dungeonstr:
            return '#B9F2FF'
        elif 'j' in dungeonstr:
            return '#E0115F '
        elif 'M' in dungeonstr: 
            return '#FF1493'
        elif 's' in dungeonstr:
            if 'sd' not in dungeonstr:
                return '#C0C0C0'
            else:
                return '#EAEAEA'
        else:
            return 'notreasure'

    
    with open('dungeon_' + str(down+1) + '.html','w') as f:
        f.write(strhead)
        
        for j in range(downlist[down].shape[1]):            
            f.write('<TR>')
            for i in range(downlist[down].shape[0]):                
                if downlist[down][i,j,0] == 'B':
                    strdata = '<td class="black_background">' + downlist[down][i,j,0] + '</td>'
                #water [boats/bridges]
                elif 'CH' in downlist[down][i,j,0]:
                    #differentiate from blue bridges
                    strdata = '<td class="brown_background">' + downlist[down][i,j,0] + '</td>'
                elif 'P' in downlist[down][i,j,0] or 'L' in downlist[down][i,j,0] or 'W' in downlist[down][i,j,0] or 'S' in downlist[down][i,j,0] or 'br' in downlist[down][i,j,0] or 'bn' in downlist[down][i,j,0] or 'bo' in downlist[down][i,j,0] or 'ri' in downlist[down][i,j,0]:
                    strdata = '<td class="blue_background">' + downlist[down][i,j,0] + '</td>'
                elif 'C' in downlist[down][i,j,0]:  #could have door markers etc                    
                    usestr = copy.deepcopy(downlist[down][i,j,0])
                    usestr = usestr.replace('C','')

                    if 'd' in usestr and 's' not in usestr:  #number and d
                        print("found door")
                        borderdir = '<divb>'
                        borderdire = '</divb>'
                        strdata = '<td>' + borderdir + downlist[down][i,j,0] + borderdire + '</td>'
                        borderdir = '<divt>'
                        borderdire = '</divt>'
                    else:
                        strdata = '<td>' + downlist[down][i,j,0] + '</td>'
                elif 'R' in downlist[down][i,j,0]:  #could have numbering
                    usestr = copy.deepcopy(downlist[down][i,j,0])
                    sdstr = ''
                    if 'sd' in downlist[down][i,j,0]:
                        print("HAVE SD HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        usestr = copy.deepcopy(downlist[down][i,j,0])
                        usestr = usestr.replace('R','')
                        usestr = usestr.replace('sd','')
                        usestr = usestr.replace('c','')
                        usestr = usestr.replace('e','')
                        usestr = usestr.replace('g','')
                        usestr = usestr.replace('j','')
                        usestr = usestr.replace('G','')
                        usestr = usestr.replace('m','')
                        usestr = usestr.replace('p','')
                        usestr = usestr.replace('s','')
                        usestr = usestr.replace('t','')
                        
                        ## get anything but number eventually regex
                        #usestr = usestr[0]
                        try:
                            secret_door_dict = room_stack['shape_dict'][int(usestr)]['contents']['secret_door_dict']
                            for s in secret_door_dict:
                                print("secret door",s,secret_door_dict[s],"ijk:",i+xmin,j+ymin,0 - down -1)
                                keylist = list(secret_door_dict[s].keys())
                                if keylist[0] == (i+xmin,j+ymin,0 - down -1):  ##try and match real coords
                                    print("found a secret door!")
                                    if secret_door_dict[s][keylist[1]]['loc'] == 'xminloc':
                                        borderdir = '<divl>'
                                        borderdire = '</divl>'
                                    elif secret_door_dict[s][keylist[1]]['loc'] == 'xmaxloc':
                                        borderdir = '<divr>'
                                        borderdire = '</divr>'
                                    elif secret_door_dict[s][keylist[1]]['loc'] == 'yminloc':                                    
                                        borderdir = '<divt>'
                                        borderdire = '</divt>'
                                    else:
                                        borderdir = '<divb>'
                                        borderdire = '</divb>'

                                    sdstr = 'border-' + borderdir + '-style: dashed'
                        except Exception as secretdoorE:
                            error_dict[error_dict['key_count']] = secretdoorE
                            error_dict['type']['key_count'] = "secret door output 3772"
                            error_dict['key_count'] += 1                            

                    color = colorcheck(downlist[down][i,j,0])
                    if color == 'notreasure':
                        if sdstr == '':
                            strdata = '<td class="gray_background">' + downlist[down][i,j,0] + '</td>'
                        else:
                            strdata = '<td class="gray_background">' + borderdir + downlist[down][i,j,0] + borderdire + '</td>'
                    else:
                        if sdstr == "":
                            strdata = '<td class="gray_background" style="color:' + color + '">'  + downlist[down][i,j,0] + '</td>'
                        else:
                            strdata = '<td class="gray_background" style="color:' + color + '">' + borderdir  + downlist[down][i,j,0] + borderdire + '</td>'

                    if 'd' in usestr and 's' not in usestr:  #number and d
                        print("found door")
                        borderdir = '<divb>'
                        borderdire = '</divb>'
                        #strdata = '<td>' + borderdir + downlist[down][i,j,0] + borderdire + '</td>'
                        strdata = '<td class="gray_background" style="color:' + color + '">' + borderdir  + downlist[down][i,j,0] + borderdire + '</td>'

                elif 'D' in downlist[down][i,j,0]:  #could have numbering:
                    usestr = copy.deepcopy(downlist[down][i,j,0])
                    usestr = usestr.replace('C','')


                    if 'sd' in usestr:  #number and d
                        try:
                            dead_end = dead_end_dict[(i+xmin,j+ymin,0 - down -1)]

                            print("found Dead End Secret door")
                            if dead_end == 'ymax':
                                borderdir = '<divb>'
                                borderdire = '</divb>'
                            elif dead_end == 'xmax':
                                borderdir = '<divr>'
                                borderdire = '</divr>'
                            else:
                                borderdir = '<divl>'
                                borderdire = '</divl>'                            
                                strdata = '<td class="brown_background">' + borderdir + downlist[down][i,j,0] + borderdire + '</td>'
                        except Exception as deadendE:
                            error_dict[error_dict['key_count']] = deadendE
                            error_dict['type']['key_count'] = "dead end output 3816"
                            error_dict['key_count'] += 1

                            print("ERROR",deadendE)
                            strdata = '<td class="brown_background">' + downlist[down][i,j,0] + '</td>'
                            #make an error log?

                        
                        borderdir = '<divt>'
                        borderdire = '</divt>'
                    else:
                        strdata = '<td class="brown_background">' + downlist[down][i,j,0] + '</td>'

                elif downlist[down][i,j,0] == 'O':
                    strdata = '<td class="green_background">' + downlist[down][i,j,0] + '</td>'
                else:
                    strdata = '<td class="red_background">' + downlist[down][i,j,0] + '</td>'

                f.write(strdata)
            f.write('</TR>')

        
        #f.write(strlegendhead)
        #for key in legend_dict:
            #f.write('<TR>')
            #f.write('<td>' + key + '</td>')
            #f.write('<td>' + legend_dict[key] + '</td>')
            #f.write('</TR>')
        f.write('</table>')

        if 'shape_dict' in room_stack:
            for room in room_stack['shape_dict']:
                f.write('<h3>Key: ' + str(room) + '</h3>')
                f.write(str(room_stack['shape_dict'][room]) + '<br>')
                if 'water' in room_stack['shape_dict'][room] and room_stack['shape_dict'][room]['water'] != 'N':
                    print("HAS WATER TO DO")
                    water_dict[room] = room_stack['shape_dict']

        if len(wandering_monster_stack) > 0:
            for wm in range(wandering_monster_stack['key_count']):
                f.write('<h4>Wandering Monster: ' + str(wm) + '</h4>')
                f.write(str(wandering_monster_stack[wm+1]) + '<br>')

        #end of page
        f.write(strend)



with open('dungeon.pkl','wb') as fd:
    pickle.dump(dungeon, fd)

with open('downlist.pkl','wb') as fd:
    pickle.dump(downlist, fd)

with open('room_stack.pkl','wb') as fd:
    pickle.dump(room_stack, fd)

with open('dungeon.pkl','rb') as fd:
    df = pickle.load(fd)
    if zwidth -1 > 1:
        #print("picklecheck",df)
        pass

with open('downlist.pkl','rb') as fd:
    df = pickle.load(fd)
    if zwidth -1 > 1:
        #print("picklecheck",df)
        pass

print("\nFINAL ROOM STACK",room_stack)   
    
print("\nERROR LOG",error_dict,"WATER_DICT:",water_dict, "WM_STACK:",wandering_monster_stack)

#print("\nWATER LOG",
