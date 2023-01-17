def testmonster():
    return "No monsters yet!"

def monster_check(level, monster):
    lst = monster[level]
    r = roll_dice(1,20)
    for index, l in lst:
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
    monster = {}
    monster[1] == [16,19,20]
    monster[2] == [12,16,18,19,20]
    monster[3] == [12,16,18,19,20]
    monster[4] == [5,6,16,18,19,20]
    monster[5] == [3,6,12,16,18,19,20]
    monster[6] == [2,4,6,12,16,18,19,20]
    monster[7] == [1,3,5,10,14,16,18,19,20]
    monster[8] == [1,2,4,7,10,14,16,18,19,20]
    monster[9] == [1,2,3,5,8,12,15,17,19,20]
    monster[10] == [1,2,3,4,6,9,12,16,19,20]
    monster[11] == [1,2,3,4,6,9,12,16,19,20]
    monster[12] == [1,2,3,4,5,7,9,12,18,20]
    monster[13] == [1,2,3,4,5,7,9,12,18,20]
    monster[14] == [1,2,3,4,5,6,8,11,17,20]
    monster[15] == [1,2,3,4,5,6,8,11,17,20]
    monster[16] == [1,2,3,4,5,6,7,10,16,20]

    if level <=16:                        
        monster_level = monster_check(level, monster)
    else:
        monster_level = monster_check(16, monster)

    return monster_level


monster_level = level_matrix(3)
print("MONSTER LEVEL:",monster_level)

