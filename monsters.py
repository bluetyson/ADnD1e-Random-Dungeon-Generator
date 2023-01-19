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
    #dice_lookup['1'] = [1,1,0]
    dice_lookup['1-1'] = [1,1,0]
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
    dragon_levels = {}

    for i in range(10):
        levels[i+1] = {}
        dragon_levels[i+1] = {}        
        for r in range(100):
            levels[i+1][r+1] = {}
            dragon_levels[i+1][r+1] = {}

    #print("TESTLEVELS",levels)

    levels['HumanSubtable'] = {}            
    levels['CharacterSubtable'] = {}            
    levels['DragonSubtable'] = {}            

    #need to do stars for substitutions for levels

    level_01 ='''01-02 Ant, giant 1-4
    03-04 Badger* 1-4
    05-14 Beetle, fire 1-4
    15 Demon, manes 1-4
    16-17 Dwarf 4-14
    18 Ear-seeker 1-1
    19 Elf 3-11
    20-21 Gnome 5-15
    22-26 Goblin 6-15
    27-28 Halfling** 9-16
    29-33 Hobgoblin 2-8
    34-48 Human — see Human Subtable below 1-1
    49-54 Kobold 6-18
    55-66 Orc 7-12
    67-70 Piercer 1-3
    71-83 Rat, giant 5-20
    84-85 Rot-grub 1-3
    86-96 Shrieker 1-2
    97-98 Skeleton 1-4
    99-100 Zombie 1-3'''

    HumanSubtable = '''01-25 Bandit* 5-15
    26-30 Berserker* 3-9
    31-45 Brigand* 5-15
    46-00 Character — see Character Subtable 1'''

    #character level max of dungeon level or monster level up to 4th
    #after that character_level = roll_dice(1,6) + 6
    #if roll > level of dungeon, character_level = character_level -1
    #if roll < level of dungeon, character_level = character_level +1
    #if level of dungeon < 16, character_level = min(12, character_level)

    CharacterNumbers = roll_dice(1,4) + 1
    HenchNumbers = 9 - CharacterNumbers

    CharacterSubtable = '''01-17 CLERIC 3
    18-20 Druid 2
    21-60 FIGHTER 5
    61-62 Paladin 2
    63-65 Ranger 2
    66-86 MAGIC-USER 3
    87-88 Illusionist 1
    89-98 THIEF 4
    99 Assassin 2
    00 MONK-OR-BARD 1'''    

    level_02='''01 Badger, giant* 1-4
    02-16 Centipede, giant 3-13
    17-27 Character — see Character Subtable 1-1
    28-29 Devil, lemure 2-5
    30-31 Gas-spore 1-2
    32-38 Gnoll 4-10
    39-46 Piercer 1-4
    47-58 Rat, giant 6-24
    59-60 Rot-grub 1-4
    61-72 Shrieker 1-3
    73-77 Stirge 5-15
    78-87 Toad, giant 1-4
    88-00 Troglodyte 2-8'''

    level_03='''01-10 Beetle, boring 1-3
    11-20 Bugbear 2-7
    21-30 Character — see Character Subtable 1-1
    31-32 Dragon — see Dragon Subtable below 1-1
    33-34 Fungi, violet 1-3
    35-40 Gelatinous-cube 1-1
    41-45 Ghoul 1-4
    46-50 Lizard, giant 1-3
    51-54 Lycanthrope, wererat 2-5
    55-60 Ochre-jelly 1-1
    61-72 Ogre 1-3
    73-74 Piercer 2-5
    75 Rot-grub 1-4
    76-77 Shrieker 2-5
    78-84 Spider, huge 1-3
    85-93 Spider, large 2-5
    94-95 Tick, giant 1-3
    96-00 Weasel, giant 1-4''' 

    dragon_level_03 = '''01-28 Black:very-young (1)
    29-62 Brass:very-young (1)
    63-00 White:very-young (1)'''
    
    level_04 = '''01-08 Ape, carnivorous 1-3
    09-14 Blink-dog 2-5
    15-22 Character — see Character Subtable 1-1
    23-24 Dragon — see Dragon Subtable below 1-1
    25-30 Gargoyle 1-2
    31-36 Ghast 1-4
    37-40 Gray-ooze 1-1
    41-44 Hell-hound 1-2
    45-47 Hydra, 5-or-6heads 1-1
    48 Hydra, pyro-5-heads 1-1
    49-62 Lycanthrope, werewolf 1-2
    63-75 Mold, yellow 1-1
    76-78 Owlbear 1-2
    79 Rust-monster 1-1
    80-82 Shadow 1-3
    83-90 Snake, giant, constrictor 1-1
    91-94 Su-monster 1-2
    95-96 Toad, ice 1-1
    97-00 Toad, poisonous 1-3'''

    dragon_level_04 = '''01-09 Black:young/sub-adult (2/3)
    10-20 Blue:very young/young (1/2)
    21-30 Brass:young/sub-adult (2/3)
    31-37 Bronze:very-young/young (1/2)
    38-50 Copper:very-young/young (1/2)
    51-54 Gold:very-young/young (1/2)
    55-70 Green:very-young/young (1/2)
    71-80 Red:very-young/young (1/2)
    81-88 Silver:very-young/young (1/2)
    89-00 White:young/sub-adult (2/3)'''

    level_05='''01-08 Character — see Character Subtable 1
    09-15 Cockatrice 1-2
    16-18 Displacer-beast 1-2
    19-22 Doppleganger 1-3
    23-24 Dragon — see Dragon Subtable below 1-1
    25-26 Hydra, 7-heads 1-1
    27 Hydra, pyro-6-heads 1-1
    28 Imp 1-2
    29-31 Leucrotta 1-2
    32-50 Lizard, subterranean 1-3
    51-52 Lycanthrope, wereboar 1-3
    53-60 Minotaur 1-3
    61-64 Mold, yellow 1-1
    65 Quasit 1-1
    66-67 Rust-Monster 1-1
    68-70 Shrieker 2-5
    71-72 Slithering-Tracker 1-1
    73-74 Snake, giant-amphisbaena 1-1
    75-82 Snake, giant-poisonous 1-1
    83-86 Snake, giant-spitting 1-1
    87-00 Spider, giant 1-2'''

    dragon_level_05='''01-08 Black:young-adult/adult (4/5)
    09-20 Blue:sub-adult/young-adult (3/4)
    21-30 Brass:young-adult/adult (4/5)
    31-37 Bronze:sub-adult/young-adult (3/4)
    38-50 Copper:sub-adult/young-adult (3/4)
    51-54 Gold:sub-adult/young-adult (3/4)
    55-70 Green:sub-adult/young-adult (3/4)
    71-80 Red:sub-adult/young-adult (3/4)
    81-88 Silver:sub-adult/young-adult (3/4)
    89-00 White:young-adult/adult (4/5)'''    

    level_06='''01-03 Basilisk 1-1
    04-10 Carrion-crawler 1-2
    11-16 Character — see Character Subtable 1-1
    17 Devil, erinyes 1-2
    18-19 Djinni 1-1
    20-21 Dragon — see Dragon Subtable below 1-1
    22-25 Green-slime 1-1
    26-28 Hydra, 8-9-heads 1-1
    29-32 Jackalwere 1-2
    33-36 Lammasu 1-3
    37-38 Lycanthrope, werebear 1-1
    39-41 Lycanthrope, weretiger 1-2
    42-50 Manticore 1-2
    51-55 Medusa 1-1
    56 Mold, brown 1-1
    57-58 Mold, yellow 1-1
    59-60 Ogre-magi 1-2
    61-68 Otyugh 1-1
    69-70 Rakshasa 1-1
    71-73 Salamander 1-2
    74-77 Spider, phase 1-3
    78-88 Troll 1-3
    89-93 Wight 1-4
    94-95 Wind-walker 1-2
    96-98 Wraith 1-2
    99-00 Wyvern 1-1'''

    dragon_level_06='''01-08 Black:old (6)
    09-19 Blue:adult (5)
    20-29 Brass:old (6)
    30-36 Bronze:adult (5)
    37-48 Copper:adult (5)
    49-52 Gold:adult (5)
    53-65 Green:adult (5)
    66-78 Red:adult (5)
    79-87 Silver:adult (5)
    88-00 White:old (6)'''   

    level_07='''01-05 Black-pudding 1-1
    06-10 Character — see Character Subtable 1-1
    11-14 Chimera 1-2
    15 Demon, succubus 1-1
    16 Demon, type-I 1-1
    17 Demon, type-II 1-1
    18 Demon, type-III 1-1
    19 Devil, barbed 1-1
    20 Devil, bone 1-1
    21 Devil, horned 1-1
    22-23 Dragon — see Dragon Subtable below 1-1
    24 Efreeti 1-1
    25-26 Elemental* 1-1
    27-30 Ettin 1-2
    31-35 Giant, hill-or-stone 1-3
    36-38 Giant, fire-or-frost 1-2
    39 Golem, flesh 1-1
    40-41 Gorgon 1-1
    42-43 Groaning-spirit 1-1
    44-46 Hydra, 10-12-heads 1-1
    47 Hydra, pyro-7-9-heads 1-1
    48-49 Intellect-devourer 1-1
    50 Invisible-stalker 1-1
    51-52 Lamia 1-2
    53-56 Lizard, fire 1-3
    57-59 Lurker-above 1-1
    60 Mezzodaemon 1-1
    61-63 Mimic 1-1
    64-65 Mind-flayer 1-2
    66-69 Mummy 1-2
    70 Naga, spirit 1-2
    71-73 Neo-otyugh 1-1
    74 Night-hag 1-2
    75-78 Roper 1-2
    79-82 Shambling-mound 1-2
    83-86 Shedu 1-2
    87 Slug, giant 1-1
    88-91 Spectre 1-1
    92-93 Trapper 1-1
    94-95 Umber-hulk 1-1
    96-97 Will-o-wisp 1-3
    98-00 Xorn 1-3'''

    dragon_level_07='''01-10 Black:very-old (7)
    11-21 Blue:old (6)
    22-29 Brass:very-old (7)
    30-36 Bronze:old (6)
    37-48 Copper:old (6)
    49-52 Gold:old (6)
    53-66 Green:old (6)
    67-80 Red:old (6)
    81-87 Silver:old (6)
    88-00 White:very-old (7)'''    

    level_08='''01 Aerial-servant 1-1
    02-06 Character — see Character Subtable 1-1
    07 Demon, type-IV 1-1
    08 Demon, type-V 1-1
    09 Demon, type-VI 1-1
    10 Devil, ice 1-1
    11-12 Dragon — see Dragon Subtable below 1-1
    13-17 Ghost 1-1
    18-21 Giant, cloud 1-2
    22-23 Golem, clay 1-1
    24-26 Hydra, 13-16-heads 1-1
    27 Hydra, pyro-12-heads 1-1
    28-29 Intellect-devourer 1-2
    30-35 Lurker-above 1-1
    36-41 Mold, brown 1-1
    42-43 Mold, yellow 1-1
    44-47 Mind-flayer 1-4
    48-50 Naga, guardian 1-2
    51-56 Neo-otyugh 1-1
    57-64 Purple-worm 1-1
    65-69 Rust-monster 1-1
    70-73 Slug, giant 1-1
    74-78 Trapper 1-1
    79-86 Vampire 1-1
    87-92 Will-o-wisp 2-5
    93-00 Xorn 2-5'''

    dragon_level_08='''01-13 Black:ancient (8)
    14-24 Blue:very-old (7)
    25-31 Brass:ancient (8)
    32-35 Bronze:very-old (7)
    36-43 Copper:very-old (7)
    44-47 Gold:very-old (7)
    48-62 Green:very-old (7)
    63-78 Red:very-old (7)
    79-82 Silver:very-old (7)
    83-00 White:ancient (8)'''

    level_09='''01-09 Character — see Character Subtable 1-1
    10-12 Devil, pit-fiend 1-1
    13-15 Dragon — see Dragon Subtable below 1-2
    16-21 Giant, storm 1-2
    22-23 Golem, stone 1-1
    24-30 Hydra, 17-20-heads 1-1
    31-33 Hydra, pyro-12-heads 1-1
    34-40 Mold, brown 1-1
    41-50 Mold, yellow 1-1
    51-52 Nycadaemon 1-1
    53-64 Purple-worm 1-1
    65-67 Rust-monster 1-1
    68-69 Titan, lesser 1-1
    70-73 Titan, minor 1-1
    74-80 Umber-Hulk 1-4
    81-83 Vampire* 1-1
    84-93 Will-o-wisp 2-5
    94-00 Xorn 2-9'''

    dragon_level_09='''01-10 Black:2-ancient-&-old (8&6)
    11-22 Blue:ancient (8)
    23-31 Brass:2-ancient-&-old (8&6)
    32-34 Bronze:ancient (8)
    35-42 Copper:ancient (8)
    43-46 Gold:ancient (8)
    47-62 Green:ancient (8)
    63-78 Red:ancient (8)
    79-82 Silver:ancient (8)
    83-00 White:2-ancient-&-very-old (8&7)'''    

    level_10 ='''01-12 Beholder 1-1
    13-20 Character — see Character Subtable 1-1
    21-28 Demon, prince* 1-1
    29-30 Devil, arch-* 1-1
    31-40 Dragon — see Dragon Subtable below 1-2
    41-50 Golem, iron 1-1
    51-60 Lich 1-1
    61-70 Titan, elder 1-1
    71-80 Vampire** 1-1
    81-00 NO ENCOUNTER 1'''    

    dragon_level_10='''01-20 Blue:2-ancient-&-very-old (8&7)
    21-26 Bronze:2 ancient-&-very-old (8&7)
    27-33 Copper:2 ancient-&-very-old (8&7)
    34-35 Chromatic-(Tiamat) (8)
    36-40 Gold:2-ancient-&-old (8&6)
    41-60 Green:2-ancient-&-very old (8&7)
    61-63 Platinum-(Bahamut) (8)
    64-94 Red:2-ancient-&-old (8&6)
    95-00 Silver:2-ancient-&-old (8&-6)'''

    levels[1]['data'] = level_01
    levels[2]['data'] = level_02
    levels[3]['data'] = level_03
    levels[4]['data'] = level_04
    levels[5]['data'] = level_05
    levels[6]['data'] = level_06
    levels[7]['data'] = level_07
    levels[8]['data'] = level_08
    levels[9]['data'] = level_09
    levels[10]['data'] = level_10

    dragon_levels[3]['data'] = dragon_level_03
    dragon_levels[4]['data'] = dragon_level_04
    dragon_levels[5]['data'] = dragon_level_05
    dragon_levels[6]['data'] = dragon_level_06
    dragon_levels[7]['data'] = dragon_level_07
    dragon_levels[8]['data'] = dragon_level_08
    dragon_levels[9]['data'] = dragon_level_09
    dragon_levels[10]['data'] = dragon_level_10

    levels['HumanSubtable']['data'] = HumanSubtable
    levels['CharacterSubtable']['data'] = CharacterSubtable

    for ld in range(10):
        #print("levels:",ld)
        uselevel = levels[ld+1]['data'].split("\n")
        for l in uselevel:
            usestr = l.replace(', ','-')
            usestr = usestr.replace('see Human Subtable below','HumanSubtable')
            usestr = usestr.replace('see Dragon Subtable below','DragonSubtable')
            usestr = usestr.replace('see Character Subtable','CharacterSubtable')
            usestr = usestr.replace(' — ','-')
            monster_list = usestr.split()
            #print(monster_list)

            number_range = monster_list[0].split('-')
            dice_roll = monster_list[2]
            monster = monster_list[1]

            if '-' in monster_list[0]:
                lo = int(number_range[0])
                hi = int(number_range[1]) 
                #print(hi, lo)
                for i in range(lo,hi+1,1):
                    #print(i)
                    levels[ld+1][i]['name'] = monster
                    levels[ld+1][i]['roll'] = dice_lookup[dice_roll]
            else:
                levels[ld+1][int(number_range[0])]['name'] = monster
                levels[ld+1][int(number_range[0])]['roll'] = dice_lookup[dice_roll]

        m = roll_dice(1,100)
        
    mcheck = levels[level][m]

    mno = roll_dice(mcheck['roll'][0],mcheck['roll'][1]) + mcheck['roll'][2]
    print("choose monster", mcheck)

    mdict = {}
    mdict['name'] = mcheck['name']
    mdict['no'] = mno

    return mdict

if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        monster_level = level_matrix(int(ARGV[1]))
    else:
        monster_level = level_matrix(3)
    print("MONSTER LEVEL:",monster_level)

    print(monster_tables(monster_level))

