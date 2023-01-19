if pc_dict['direction'] == 'ahead':

        new_coord = passage_make(coord,loop=6,ymod=1,yloop=1,xwidth=1)

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

else:
    pass


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
                                new_coord = passage_make(coord, xloop=-1,yloop=1,ywidth=1)
                            else:
                                new_coord = passage_make(coord, xloop=-1,yloop=-1,ywidth=1)

                        elif usedir == 'xmaxloc': 
                            which_way = roll_dice(1,2)           
                            if which_way == 1:  #corridor left
                                new_coord = passage_make(coord, xloop=1,yloop=1,ywidth=1)
                            else:
                                new_coord = passage_make(coord, xloop=1,yloop=-1,ywidth=1)

                        elif usedir == 'yminloc':                             
                            which_way = roll_dice(1,2)           
                            if which_way == 1:  #corridor left
                                new_coord = passage_make(coord, xloop=-1,yloop=1,xwidth=1)
                            else:
                                new_coord = passage_make(coord, xloop=1,yloop-1,xwidth=1)

                        else: #ymaxloc
                            which_way = roll_dice(1,2)         
                            if which_way == 1:  #corridor left
                                new_coord = passage_make(coord, xloop=-1,yloop=1,xwidth=1)
                            else:
                                new_coord = passage_make(coord, xloop=1,yloop1,xwidth=1)

                    elif secret_door_dict[s + 1][key]['beyond'] == 'A':                    
                        print("in secret door passage ahead")
                        if usedir == 'xminloc':
                            new_coord = passage_make(coord, xloop=-1,ywidth=1)
                        elif usedir == 'xmaxloc':                             
                            new_coord = passage_make(coord, xloop=1,ywidth=1)
                        elif usedir == 'yminloc':                             
                            new_coord = passage_make(coord, yloop=-1,xwidth=1)
                        else: #ymaxloc
                            new_coord = passage_make(coord, yloop=1,xwidth=1)

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
