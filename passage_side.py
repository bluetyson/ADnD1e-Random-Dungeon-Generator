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
