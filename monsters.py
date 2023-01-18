import random
import sys

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

def testmonster():
    return "On level of monsters so far!"

def monster_check(level, monster):
    lst = monster[level]
    r = roll_dice(1,20)
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

    if level <=16:                        
        monster_level = monster_check(level, monster)
    else:
        monster_level = monster_check(16, monster)

    return monster_level

def monster_tables(level):

    dice_lookup = {}
    #make lists of what for roll_dice
    dice_lookup['1'] = [1,1,0]
    dice_lookup['1-2'] = [1,2,0]
    dice_lookup['1-3'] = [1,3,0]
    dice_lookup['1-4'] = [1,4,0]
    dice_lookup['1-6'] = [1,6,0]
    dice_lookup['1-8'] = [1,8,0]
    dice_lookup['1-10'] = [1,10,0]
    dice_lookup['1-12'] = [1,12,0]
    dice_lookup['2-5'] = [1,4,1]
    dice_lookup['2-7'] = [1,6,1]
    dice_lookup['2-8'] = [2,4,0]
    dice_lookup['2-9'] = [1,8,1]
    dice_lookup['3-9'] = [3,3,0]
    dice_lookup['3-11'] = [4,3,-1]
    dice_lookup['3-13'] = [2,6,1]
    dice_lookup['4-10'] = [2,4,2]
    dice_lookup['4-14'] = [2,6,2]
    dice_lookup['5-15'] = [2,6,3]
    dice_lookup['5-20'] = [5,4,0]
    dice_lookup['6-15'] = [3,4,3]
    dice_lookup['6-18'] = [6,3,0]
    dice_lookup['6-24'] = [6,4,0]
    dice_lookup['7-12'] = [1,6,6]
    dice_lookup['9-16'] = [1,8,8]

    levels = {}
    for i in range(10):
        levels[i+1] = {}
        for r in range(100):
            levels[i+1][r+1] = {}

    level_01 ='''01-02 Ant, giant 1-4
    03-04 Badger* 1-4
    05-14 Beetle, fire 1-4
    15 Demon, manes 1-4
    16-17 Dwarf 4-14
    18 Ear-seeker 1
    19 Elf 3-11
    20-21 Gnome 5-15
    22-26 Goblin 6-15
    27-28 Halfling** 9-16
    29-33 Hobgoblin 2-8
    34-48 Human — see Human Subtable below 1
    49-54 Kobold 6-18
    55-66 Orc 7-12
    67-70 Piercer 1-3
    71-83 Rat, giant 5-20
    84-85 Rot-grub 1-3
    86-96 Shrieker 1-2
    97-98 Skeleton 1-4
    99-100 Zombie 1-3'''

    levels[1]['data'] = level_01

    level_02 = ''
    level_03 = ''
    level_04 = ''
    level_05 = ''
    level_06 = ''
    level_07 = ''
    level_08 = ''
    level_09 = ''
    level_10 = ''

    levels[2]['data'] = level_02
    levels[3]['data'] = level_03
    levels[4]['data'] = level_04
    levels[5]['data'] = level_05
    levels[6]['data'] = level_06
    levels[7]['data'] = level_07
    levels[8]['data'] = level_08
    levels[9]['data'] = level_09
    levels[10]['data'] = level_10

    uselevel = level_01.split("\n")
    for l in uselevel:
        usestr = l.replace(', ','-')
        usestr = usestr.replace('see Human Subtable below','HumanSubtable')
        usestr = usestr.replace(' — ','-')
        monster_list = usestr.split()
        print(monster_list)

        number_range = monster_list[0].split('-')
        dice_roll = monster_list[2]
        monster = monster_list[1]

        if '-' in monster_list[0]:
            lo = int(number_range[0])
            hi = int(number_range[1]) 
            #print(hi, lo)
            for i in range(lo,hi+1,1):
                #print(i)
                levels[1][i]['name'] = monster
                levels[1][i]['roll'] = dice_lookup[dice_roll]
        else:
            levels[1][int(number_range[0])]['name'] = monster
            levels[1][int(number_range[0])]['roll'] = dice_lookup[dice_roll]

    return True

if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        monster_level = level_matrix(int(ARGV[1]))
    else:
        monster_level = level_matrix(3)
    print("MONSTER LEVEL:",monster_level)

    print(monster_tables(monster_level))

