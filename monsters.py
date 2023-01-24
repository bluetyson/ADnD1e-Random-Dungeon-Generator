import random
import sys
import json

def multi_roll(rolls, sides):
    total = 0
    for i in range(rolls):
        total = total + roll_dice(1,sides)
    return total

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

def testmonster():
    return "On level of monsters so far!"

def create_dragon(level):
    pass

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

def xp_hack():
    dragon_xp = {}
    dragon_xp[1] = 10
    dragon_xp[2] = 50
    dragon_xp[3] = 150
    dragon_xp[4] = 250
    dragon_xp[5] = 500
    dragon_xp[6] = 1000
    dragon_xp[7] = 1000
    dragon_xp[8] = 1000
    dragon_xp[9] = 10000
    dragon_xp[10] = 20000
    return dragon_xp

def human_data():
    hd = {'human-bandit': {'usename': 'human-bandit',
  'lair': '20%',
  'Treasure': 'M (A)',
  'HD': '1-2',
  'XP': 'I/5+1/hp',
  'XPbase': '5',
  'XPhp': '1',
  'HP': 6,
  'XPtotal': 11,
  'treasure_individual': ['M'],
  'treasure_lair': ['A']},
 'human-berserker': {'usename': 'human-berserker',
  'lair': '10%',
  'Treasure': 'K (B)',
  'HD': '1-1',
  'XP': 'I/10+1/hp',
  'XPbase': '10',
  'XPhp': '1',
  'HP': 5,
  'XPtotal': 15,
  'treasure_individual': ['K'],
  'treasure_lair': ['B']},
 'human-brigand': {'usename': 'human-brigand',
  'lair': '20%',
  'Treasure': 'M (A)',
  'HD': '1-2',
  'XP': 'I/5+1/hp',
  'XPbase': '5',
  'XPhp': '1',
  'HP': 6,
  'XPtotal': 11,
  'treasure_individual': ['M'],
  'treasure_lair': ['A']}}
    return hd

def dragon_data():    
    dd = {'Black': {'usename': 'dragon-black',
    'lair': '30%',
    'Treasure': 'H',
    'HD': '6 to 8',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H']},
    'Blue': {'usename': 'dragon-blue',
    'lair': '50%',
    'Treasure': 'H,S',
    'HD': '8 to 10',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H', 'S']},
    'Brass': {'usename': 'dragon-brass',
    'lair': '25%',
    'Treasure': 'H',
    'HD': '6 to 8',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H']},
    'Bronze': {'usename': 'dragon-bronze',
    'lair': '45%',
    'Treasure': 'H,S,T',
    'HD': '8 to 10',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H', 'S', 'T']},
    'Copper': {'usename': 'dragon-copper',
    'lair': '35%',
    'Treasure': 'H,S',
    'HD': '7 to 9',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H', 'S']},
    'Gold': {'usename': 'dragon-gold',
    'lair': '65%',
    'Treasure': 'H,R,S,T',
    'HD': '10 to 12',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H', 'R', 'S', 'T']},
    'Green': {'usename': 'dragon-green',
    'lair': '40%',
    'Treasure': 'H',
    'HD': '7 to 9',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H']},
    'Red': {'usename': 'dragon-red',
    'lair': '60%',
    'Treasure': 'H,S,T',
    'HD': '9 to 11',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H', 'S', 'T']},
    'Silver': {'usename': 'dragon-silver',
    'lair': '55%',
    'Treasure': 'H,T',
    'HD': '9 to 11',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['H', 'T']},
    'White': {'usename': 'dragon-white',
    'lair': '20%',
    'Treasure': 'E,O,S',
    'HD': '5 to 7',
    'XP': -1,
    'treasure_individual': [],
    'treasure_lair': ['E', 'O', 'S']},
    'Chromatic': {'usename': 'dragon-chromatic-tiamat',
    'lair': '90%',
    'Treasure': 'H,S,T,U',
    'HD': '16 (128 hp)',
    'XP': '63580',
    'treasure_individual': [],
    'treasure_lair': ['H', 'S', 'T', 'U']},
    'Platinum': {'usename': 'dragon-platinum-bahamut',
    'lair': '75%',
    'Treasure': 'H,R,S,T,V',
    'HD': '21 (168 hp)',
    'XP': '58080',
    'treasure_individual': [],
    'treasure_lair': ['H', 'R', 'S', 'T', 'V']}}

    return dd

def all_data():
    ad = {'ant-giant': {'usename': 'ant-giant',
  'lair': '10%',
  'Treasure': 'Q(x3),S',
  'HD': '2',
  'XP': 'I/20+2/hp',
  'XPbase': '20',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 38,
  'treasure_individual': [],
  'treasure_lair': ['Q', 'Q', 'Q', 'S']},
 'badger': {'usename': 'badger',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1+2',
  'XP': 'I/20+2/hp',
  'XPbase': '20',
  'XPhp': '2',
  'HP': 2,
  'XPtotal': 24,
  'treasure_individual': [],
  'treasure_lair': []},
 'beetle-fire': {'usename': 'beetle-fire',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1+2',
  'XP': 'I/20+2/hp',
  'XPbase': '20',
  'XPhp': '2',
  'HP': 2,
  'XPtotal': 24,
  'treasure_individual': [],
  'treasure_lair': []},
 'demon-manes': {'usename': 'demon-manes',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1',
  'XP': 'I/14+1/hp',
  'XPbase': '14',
  'XPhp': '1',
  'HP': 4,
  'XPtotal': 18,
  'treasure_individual': [],
  'treasure_lair': []},
 'dwarf-hill': {'usename': 'dwarf-hill',
  'lair': '50%',
  'Treasure': 'Mx5 (G,Qx20,R)',
  'HD': '1',
  'XP': 'I/14+1/hp',
  'XPbase': '14',
  'XPhp': '1',
  'HP': 4,
  'XPtotal': 18,
  'treasure_individual': ['M', 'M', 'M', 'M', 'M', 'Mx5'],
  'treasure_lair': ['G',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']},
 'dwarf-mountain': {'usename': 'dwarf-mountain',
  'lair': '50%',
  'Treasure': 'Mx5 (G,Qx20,R)',
  'HD': '1+1',
  'XP': 'I/24+2/hp',
  'XPbase': '24',
  'XPhp': '2',
  'HP': 3,
  'XPtotal': 30,
  'treasure_individual': ['M', 'M', 'M', 'M', 'M', 'Mx5'],
  'treasure_lair': ['G',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']},
 'ear-seeker': {'usename': 'ear-seeker',
  'lair': '90%',
  'Treasure': 'Nil',
  'HD': '1-7',
  'XP': 'I/35+1/hp',
  'XPbase': '35',
  'XPhp': '1',
  'HP': 11,
  'XPtotal': 46,
  'treasure_individual': [],
  'treasure_lair': []},
 'elf': {'usename': 'elf',
  'lair': '10%',
  'Treasure': 'N (G,S,T)',
  'HD': '1+1',
  'XP': 'I/24+2/hp',
  'XPbase': '24',
  'XPhp': '2',
  'HP': 3,
  'XPtotal': 30,
  'treasure_individual': ['N'],
  'treasure_lair': ['G', 'S', 'T']},
 'gnome': {'usename': 'gnome',
  'lair': '50%',
  'Treasure': 'Mx3 (C,Qx20)',
  'HD': '1',
  'XP': 'I/14+1/hp',
  'XPbase': '14',
  'XPhp': '1',
  'HP': 4,
  'XPtotal': 18,
  'treasure_individual': ['M', 'M', 'M', 'Mx3'],
  'treasure_lair': ['C',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q']},
 'goblin': {'usename': 'goblin',
  'lair': '40%',
  'Treasure': 'K (C)',
  'HD': '1-1',
  'XP': 'I/10+1/hp',
  'XPbase': '10',
  'XPhp': '1',
  'HP': 5,
  'XPtotal': 15,
  'treasure_individual': ['K'],
  'treasure_lair': ['C']},
 'halfling': {'usename': 'halfling',
  'lair': '70%',
  'Treasure': 'K (B)',
  'HD': '1-2',
  'XP': 'I/7+1/hp',
  'XPbase': '7',
  'XPhp': '1',
  'HP': 6,
  'XPtotal': 13,
  'treasure_individual': ['K'],
  'treasure_lair': ['B']},
 'hobgoblin': {'usename': 'hobgoblin',
  'lair': '25%',
  'Treasure': 'J (M,D,Qx5)',
  'HD': '1+1',
  'XP': 'I/20+2/hp',
  'XPbase': '20',
  'XPhp': '2',
  'HP': 3,
  'XPtotal': 26,
  'treasure_individual': ['J'],
  'treasure_lair': ['M', 'D', 'Q', 'Q', 'Q', 'Q', 'Q']},
 'kobold': {'usename': 'kobold',
  'lair': '40%',
  'Treasure': 'J (O,Qx5)',
  'HD': '1-2',
  'XP': 'I/5+1/hp',
  'XPbase': '5',
  'XPhp': '1',
  'HP': 6,
  'XPtotal': 11,
  'treasure_individual': ['J'],
  'treasure_lair': ['O', 'Q', 'Q', 'Q', 'Q', 'Q']},
 'orc': {'usename': 'orc',
  'lair': '35%',
  'Treasure': 'L (C,O,Qx10,S)',
  'HD': '1',
  'XP': 'I/10+1/hp',
  'XPbase': '10',
  'XPhp': '1',
  'HP': 4,
  'XPtotal': 14,
  'treasure_individual': ['L'],
  'treasure_lair': ['C',
   'O',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'S']},
 'piercer-1hd': {'usename': 'piercer-1hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1',
  'XP': 'I/14+1/hp',
  'XPbase': '14',
  'XPhp': '1',
  'HP': 4,
  'XPtotal': 18,
  'treasure_individual': [],
  'treasure_lair': []},
 'rat-giant': {'usename': 'rat-giant',
  'lair': '10%',
  'Treasure': 'C',
  'HD': '1-2',
  'XP': 'I/7+1/hp',
  'XPbase': '7',
  'XPhp': '1',
  'HP': 6,
  'XPtotal': 13,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'rot-grub': {'usename': 'rot-grub',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1-7',
  'XP': 'I/35+1/hp',
  'XPbase': '35',
  'XPhp': '1',
  'HP': 11,
  'XPtotal': 46,
  'treasure_individual': [],
  'treasure_lair': []},
 'shrieker': {'usename': 'shrieker',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '3',
  'XP': 'I/5+1/hp',
  'XPbase': '5',
  'XPhp': '1',
  'HP': 13,
  'XPtotal': 18,
  'treasure_individual': [],
  'treasure_lair': []},
 'skeleton': {'usename': 'skeleton',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1',
  'XP': 'I/18+1/hp',
  'XPbase': '18',
  'XPhp': '1',
  'HP': 4,
  'XPtotal': 22,
  'treasure_individual': [],
  'treasure_lair': []},
 'zombie': {'usename': 'zombie',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '2',
  'XP': 'I/20+2/hp',
  'XPbase': '20',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 38,
  'treasure_individual': [],
  'treasure_lair': []},
 'badger-giant': {'usename': 'badger-giant',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1+2',
  'XP': 'II/35+3/hp',
  'XPbase': '35',
  'XPhp': '3',
  'HP': 2,
  'XPtotal': 41,
  'treasure_individual': [],
  'treasure_lair': []},
 'centipede-giant': {'usename': 'centipede-giant',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1-4',
  'XP': 'II/30+1/hp',
  'XPbase': '30',
  'XPhp': '1',
  'HP': 8,
  'XPtotal': 38,
  'treasure_individual': [],
  'treasure_lair': []},
 'devil-lemure': {'usename': 'devil-lemure',
  'lair': '100%',
  'Treasure': 'Nil',
  'HD': '3',
  'XP': 'III/65+3/hp',
  'XPbase': '65',
  'XPhp': '3',
  'HP': 13,
  'XPtotal': 104,
  'treasure_individual': [],
  'treasure_lair': []},
 'gas-spore': {'usename': 'gas-spore',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '1-8',
  'XP': 'II/33+1/hp',
  'XPbase': '33',
  'XPhp': '1',
  'HP': 12,
  'XPtotal': 45,
  'treasure_individual': [],
  'treasure_lair': []},
 'gnoll': {'usename': 'gnoll',
  'lair': '20%',
  'Treasure': 'L,M (D,Qx5,S)',
  'HD': '2',
  'XP': 'II/28+2/hp',
  'XPbase': '28',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 46,
  'treasure_individual': ['M', 'M'],
  'treasure_lair': ['D', 'Q', 'Q', 'Q', 'Q', 'Q', 'S']},
 'piercer-2hd': {'usename': 'piercer-2hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '2',
  'XP': 'II/28+2/hp',
  'XPbase': '28',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 46,
  'treasure_individual': [],
  'treasure_lair': []},
 'stirge': {'usename': 'stirge',
  'lair': '60%',
  'Treasure': 'D',
  'HD': '1+1',
  'XP': 'II/36+2/hp',
  'XPbase': '36',
  'XPhp': '2',
  'HP': 3,
  'XPtotal': 42,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'toad-giant': {'usename': 'toad-giant',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '2+4',
  'XP': 'II/50+3/hp',
  'XPbase': '50',
  'XPhp': '3',
  'HP': 5,
  'XPtotal': 65,
  'treasure_individual': [],
  'treasure_lair': []},
 'troglodyte': {'usename': 'troglodyte',
  'lair': '15%',
  'Treasure': 'A',
  'HD': '2',
  'XP': 'II/28+2/hp',
  'XPbase': '28',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 46,
  'treasure_individual': [],
  'treasure_lair': ['A']},
 'beetle-boring': {'usename': 'beetle-boring',
  'lair': '40%',
  'Treasure': 'C,R,S,T',
  'HD': '5',
  'XP': 'III/90+5/hp',
  'XPbase': '90',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 200,
  'treasure_individual': [],
  'treasure_lair': ['C', 'R', 'S', 'T']},
 'bugbear': {'usename': 'bugbear',
  'lair': '25%',
  'Treasure': 'J,K,L,M (B)',
  'HD': '3+1',
  'XP': 'III/135+4/hp',
  'XPbase': '135',
  'XPhp': '4',
  'HP': 12,
  'XPtotal': 183,
  'treasure_individual': ['M', 'M', 'M', 'M'],
  'treasure_lair': ['B']},
 'fungi-violet': {'usename': 'fungi-violet',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '3',
  'XP': 'III/80+3/hp',
  'XPbase': '80',
  'XPhp': '3',
  'HP': 13,
  'XPtotal': 119,
  'treasure_individual': [],
  'treasure_lair': []},
 'gelatinous-cube': {'usename': 'gelatinous-cube',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '4',
  'XP': 'III/150+4/hp',
  'XPbase': '150',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 222,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'ghoul': {'usename': 'ghoul',
  'lair': '20%',
  'Treasure': 'B,T',
  'HD': '2',
  'XP': 'III/65+2/hp',
  'XPbase': '65',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 83,
  'treasure_individual': [],
  'treasure_lair': ['B', 'T']},
 'lizard-giant': {'usename': 'lizard-giant',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '3+1',
  'XP': 'III/60+4/hp',
  'XPbase': '60',
  'XPhp': '4',
  'HP': 12,
  'XPtotal': 108,
  'treasure_individual': [],
  'treasure_lair': []},
 'lycanthrope-wererat': {'usename': 'lycanthrope-wererat',
  'lair': '30%',
  'Treasure': 'C',
  'HD': '3+1',
  'XP': 'III/150+4/hp',
  'XPbase': '150',
  'XPhp': '4',
  'HP': 12,
  'XPtotal': 198,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'ochre-jelly': {'usename': 'ochre-jelly',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '6',
  'XP': 'IV/225+6/hp',
  'XPbase': '225',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 387,
  'treasure_individual': [],
  'treasure_lair': []},
 'ogre': {'usename': 'ogre',
  'lair': '20%',
  'Treasure': 'Mx10 (Q,B,S)',
  'HD': '4+1',
  'XP': 'III/90+5/hp',
  'XPbase': '90',
  'XPhp': '5',
  'HP': 17,
  'XPtotal': 175,
  'treasure_individual': ['M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'Mx10'],
  'treasure_lair': ['Q', 'B', 'S']},
 'piercer-3hd': {'usename': 'piercer-3hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '3',
  'XP': 'II/50+3/hp',
  'XPbase': '50',
  'XPhp': '3',
  'HP': 13,
  'XPtotal': 89,
  'treasure_individual': [],
  'treasure_lair': []},
 'piercer-4hd': {'usename': 'piercer-4hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '4',
  'XP': 'III/85+4/hp',
  'XPbase': '85',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 157,
  'treasure_individual': [],
  'treasure_lair': []},
 'spider-huge': {'usename': 'spider-huge',
  'lair': '50%',
  'Treasure': 'J-N,Q',
  'HD': '2+2',
  'XP': 'III/90+3/hp',
  'XPbase': '90',
  'XPhp': '3',
  'HP': 7,
  'XPtotal': 111,
  'treasure_individual': ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'],
  'treasure_lair': ['Q', 'B', 'S']},
 'spider-large': {'usename': 'spider-large',
  'lair': '60%',
  'Treasure': 'J-N',
  'HD': '1+1',
  'XP': 'III/65+2/hp',
  'XPbase': '65',
  'XPhp': '2',
  'HP': 3,
  'XPtotal': 71,
  'treasure_individual': ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'],
  'treasure_lair': ['Q', 'B', 'S']},
 'tick-giant-2hd': {'usename': 'tick-giant-2hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '2',
  'XP': 'II/28+2/hp',
  'XPbase': '28',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 46,
  'treasure_individual': [],
  'treasure_lair': []},
 'tick-giant-3hd': {'usename': 'tick-giant-3hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '3',
  'XP': 'II/50+3/hp',
  'XPbase': '50',
  'XPhp': '3',
  'HP': 13,
  'XPtotal': 89,
  'treasure_individual': [],
  'treasure_lair': []},
 'tick-giant-4hd': {'usename': 'tick-giant-4hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '4',
  'XP': 'III/85+4/hp',
  'XPbase': '85',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 157,
  'treasure_individual': [],
  'treasure_lair': []},
 'weasel-giant': {'usename': 'weasel-giant',
  'lair': '15%',
  'Treasure': 'Nil',
  'HD': '3+3',
  'XP': 'III/125+4/hp',
  'XPbase': '125',
  'XPhp': '4',
  'HP': 10,
  'XPtotal': 165,
  'treasure_individual': [],
  'treasure_lair': []},
 'ape-carnivorous': {'usename': 'ape-carnivorous',
  'lair': '10%',
  'Treasure': 'C',
  'HD': '5',
  'XP': 'III/130+5/hp',
  'XPbase': '130',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 240,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'blink-dog': {'usename': 'blink-dog',
  'lair': '20%',
  'Treasure': 'C',
  'HD': '4',
  'XP': 'III/110+4/hp',
  'XPbase': '110',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 182,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'gargoyle': {'usename': 'gargoyle',
  'lair': '20%',
  'Treasure': 'M(x10) (C)',
  'HD': '4+4',
  'XP': 'IV/205+5/hp',
  'XPbase': '205',
  'XPhp': '5',
  'HP': 14,
  'XPtotal': 275,
  'treasure_individual': ['M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'M',
   'Mx10'],
  'treasure_lair': ['C']},
 'ghast': {'usename': 'ghast',
  'lair': '10%',
  'Treasure': 'B,Q,R,S,T',
  'HD': '4',
  'XP': 'IV/190+4/hp',
  'XPbase': '190',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 262,
  'treasure_individual': [],
  'treasure_lair': ['B', 'Q', 'R', 'S', 'T']},
 'gray-ooze': {'usename': 'gray-ooze',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '3+3',
  'XP': 'IV/200+4/hp',
  'XPbase': '200',
  'XPhp': '4',
  'HP': 10,
  'XPtotal': 240,
  'treasure_individual': [],
  'treasure_lair': []},
 'hell-hound-4hd': {'usename': 'hell-hound-4hd',
  'lair': '30%',
  'Treasure': 'C,S',
  'HD': '4',
  'XP': 'III/85+4/hp',
  'XPbase': '85',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 157,
  'treasure_individual': [],
  'treasure_lair': ['C', 'S']},
 'hell-hound-5hd': {'usename': 'hell-hound-5hd',
  'lair': '30%',
  'Treasure': 'C,S',
  'HD': '5',
  'XP': 'III/130+5/hp',
  'XPbase': '130',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 240,
  'treasure_individual': [],
  'treasure_lair': ['C', 'S']},
 'hell-hound-6hd': {'usename': 'hell-hound-6hd',
  'lair': '30%',
  'Treasure': 'C,S',
  'HD': '6',
  'XP': 'IV/225+6/hp',
  'XPbase': '225',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 387,
  'treasure_individual': [],
  'treasure_lair': ['C', 'S']},
 'hell-hound-7hd': {'usename': 'hell-hound-7hd',
  'lair': '30%',
  'Treasure': 'C,S',
  'HD': '7',
  'XP': 'V/350+8/hp',
  'XPbase': '350',
  'XPhp': '8',
  'HP': 31,
  'XPtotal': 598,
  'treasure_individual': [],
  'treasure_lair': ['C', 'S']},
 'hydra-5-heads': {'usename': 'hydra-5-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '5',
  'XP': 'IV/170+5/hp',
  'XPbase': '170',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 280,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-6-heads': {'usename': 'hydra-6-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '6',
  'XP': 'V/300+6/hp',
  'XPbase': '300',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 462,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-pyro-5-heads': {'usename': 'hydra-pyro-5-heads',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '7',
  'XP': 'IV/245+5/hp',
  'XPbase': '245',
  'XPhp': '5',
  'HP': 31,
  'XPtotal': 400,
  'treasure_individual': [],
  'treasure_lair': []},
 'lycanthrope-werewolf': {'usename': 'lycanthrope-werewolf',
  'lair': '25%',
  'Treasure': 'B',
  'HD': '4+3',
  'XP': 'IV/205+5/hp',
  'XPbase': '205',
  'XPhp': '5',
  'HP': 15,
  'XPtotal': 280,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'mold-yellow': {'usename': 'mold-yellow',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '0',
  'XP': 'IV/0+0/hp',
  'XPbase': '0',
  'XPhp': '0',
  'HP': 1,
  'XPtotal': 0,
  'treasure_individual': [],
  'treasure_lair': []},
 'owlbear': {'usename': 'owlbear',
  'lair': '30%',
  'Treasure': 'C',
  'HD': '5+2',
  'XP': 'IV/225+6/hp',
  'XPbase': '225',
  'XPhp': '6',
  'HP': 20,
  'XPtotal': 345,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'rust-monster': {'usename': 'rust-monster',
  'lair': '10%',
  'Treasure': 'Qx10',
  'HD': '5',
  'XP': 'IV/165+5/hp',
  'XPbase': '165',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 275,
  'treasure_individual': [],
  'treasure_lair': ['Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q']},
 'shadow': {'usename': 'shadow',
  'lair': '40%',
  'Treasure': 'F',
  'HD': '3+3',
  'XP': 'III/135+4/hp',
  'XPbase': '135',
  'XPhp': '4',
  'HP': 10,
  'XPtotal': 175,
  'treasure_individual': [],
  'treasure_lair': ['F']},
 'snake-giant-constrictor': {'usename': 'snake-giant-constrictor',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '3+2',
  'XP': 'V/350+8/hp',
  'XPbase': '350',
  'XPhp': '8',
  'HP': 11,
  'XPtotal': 438,
  'treasure_individual': [],
  'treasure_lair': []},
 'su-monster': {'usename': 'su-monster',
  'lair': '30%',
  'Treasure': 'C,Y',
  'HD': '5+5',
  'XP': 'V/350+6/hp',
  'XPbase': '350',
  'XPhp': '6',
  'HP': 17,
  'XPtotal': 452,
  'treasure_individual': [],
  'treasure_lair': ['C', 'Y']},
 'toad-ice': {'usename': 'toad-ice',
  'lair': '40%',
  'Treasure': 'C',
  'HD': '5',
  'XP': 'III/130+5/hp',
  'XPbase': '130',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 240,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'toad-poisonous': {'usename': 'toad-poisonous',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '2',
  'XP': 'III/65+2/hp',
  'XPbase': '65',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 83,
  'treasure_individual': [],
  'treasure_lair': []},
 'cockatrice': {'usename': 'cockatrice',
  'lair': '30%',
  'Treasure': 'D',
  'HD': '5',
  'XP': 'IV/165+5/hp',
  'XPbase': '165',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 275,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'displacer-beast': {'usename': 'displacer-beast',
  'lair': '25%',
  'Treasure': 'D',
  'HD': '6',
  'XP': 'V/300+6/hp',
  'XPbase': '300',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 462,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'doppleganger': {'usename': 'doppleganger',
  'lair': '20%',
  'Treasure': 'E',
  'HD': '4',
  'XP': 'IV/175+4/hp',
  'XPbase': '175',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 247,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'hydra-7-heads': {'usename': 'hydra-7-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '7',
  'XP': 'VI/650+8/hp',
  'XPbase': '650',
  'XPhp': '8',
  'HP': 31,
  'XPtotal': 898,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-pyro-6-heads': {'usename': 'hydra-pyro-6-heads',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '7',
  'XP': 'V/425+6/hp',
  'XPbase': '425',
  'XPhp': '6',
  'HP': 31,
  'XPtotal': 611,
  'treasure_individual': [],
  'treasure_lair': []},
 'imp': {'usename': 'imp',
  'lair': '0%',
  'Treasure': 'O',
  'HD': '2+2',
  'XP': 'V/275+3/hp',
  'XPbase': '275',
  'XPhp': '3',
  'HP': 7,
  'XPtotal': 296,
  'treasure_individual': [],
  'treasure_lair': ['O']},
 'leucrotta': {'usename': 'leucrotta',
  'lair': '40%',
  'Treasure': 'D',
  'HD': '6+1',
  'XP': 'V/350+8/hp',
  'XPbase': '350',
  'XPhp': '8',
  'HP': 26,
  'XPtotal': 558,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'lizard-subterranean': {'usename': 'lizard-subterranean',
  'lair': '20%',
  'Treasure': 'O,P,Qx5',
  'HD': '6',
  'XP': 'IV/225+8/hp',
  'XPbase': '225',
  'XPhp': '8',
  'HP': 27,
  'XPtotal': 441,
  'treasure_individual': [],
  'treasure_lair': ['O', 'P', 'Q', 'Q', 'Q', 'Q', 'Q']},
 'lycanthrope-wereboar': {'usename': 'lycanthrope-wereboar',
  'lair': '20%',
  'Treasure': 'B,S',
  'HD': '5+2',
  'XP': 'IV/225+6/hp',
  'XPbase': '225',
  'XPhp': '6',
  'HP': 20,
  'XPtotal': 345,
  'treasure_individual': [],
  'treasure_lair': ['B', 'S']},
 'minotaur': {'usename': 'minotaur',
  'lair': '20%',
  'Treasure': 'C',
  'HD': '6+3',
  'XP': 'V/350+8/hp',
  'XPbase': '350',
  'XPhp': '8',
  'HP': 24,
  'XPtotal': 542,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'quasit': {'usename': 'quasit',
  'lair': '0%',
  'Treasure': 'Qx3',
  'HD': '3',
  'XP': 'V/325+3/hp',
  'XPbase': '325',
  'XPhp': '3',
  'HP': 13,
  'XPtotal': 364,
  'treasure_individual': [],
  'treasure_lair': ['Q', 'Q', 'Q']},
 'slithering-tracker': {'usename': 'slithering-tracker',
  'lair': '10%',
  'Treasure': 'C',
  'HD': '5',
  'XP': 'IV/245+5/hp',
  'XPbase': '245',
  'XPhp': '5',
  'HP': 22,
  'XPtotal': 355,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'snake-giant-amphisbaena': {'usename': 'snake-giant-amphisbaena',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '6',
  'XP': 'V/275+6/hp',
  'XPbase': '275',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 437,
  'treasure_individual': [],
  'treasure_lair': []},
 'snake-giant-poisonous': {'usename': 'snake-giant-poisonous',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '4+2',
  'XP': 'IV/165+5/hp',
  'XPbase': '165',
  'XPhp': '5',
  'HP': 16,
  'XPtotal': 245,
  'treasure_individual': [],
  'treasure_lair': []},
 'snake-giant-spitting': {'usename': 'snake-giant-spitting',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '4+2',
  'XP': 'IV/165+5/hp',
  'XPbase': '165',
  'XPhp': '5',
  'HP': 16,
  'XPtotal': 245,
  'treasure_individual': [],
  'treasure_lair': []},
 'spider-giant': {'usename': 'spider-giant',
  'lair': '70%',
  'Treasure': 'C',
  'HD': '4+4',
  'XP': 'IV/205+5/hp',
  'XPbase': '205',
  'XPhp': '5',
  'HP': 14,
  'XPtotal': 275,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'basilisk': {'usename': 'basilisk',
  'lair': '40%',
  'Treasure': 'F',
  'HD': '6+1',
  'XP': 'VI/1000+8/hp',
  'XPbase': '1000',
  'XPhp': '8',
  'HP': 26,
  'XPtotal': 1208,
  'treasure_individual': [],
  'treasure_lair': ['F']},
 'carrion-crawler': {'usename': 'carrion-crawler',
  'lair': '50%',
  'Treasure': 'B',
  'HD': '3+1',
  'XP': 'III/150+4/hp',
  'XPbase': '150',
  'XPhp': '4',
  'HP': 12,
  'XPtotal': 198,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'devil-erinyes': {'usename': 'devil-erinyes',
  'lair': '20%',
  'Treasure': 'R',
  'HD': '6+6',
  'XP': 'VI/875+8/hp',
  'XPbase': '875',
  'XPhp': '8',
  'HP': 21,
  'XPtotal': 1043,
  'treasure_individual': [],
  'treasure_lair': ['R']},
 'djinni': {'usename': 'djinni',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '7+3',
  'XP': 'VI/725+10/hp',
  'XPbase': '725',
  'XPhp': '10',
  'HP': 28,
  'XPtotal': 1005,
  'treasure_individual': [],
  'treasure_lair': []},
 'green-slime': {'usename': 'green-slime',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '2',
  'XP': 'III/73+2/hp',
  'XPbase': '73',
  'XPhp': '2',
  'HP': 9,
  'XPtotal': 91,
  'treasure_individual': [],
  'treasure_lair': []},
 'hydra-8-heads': {'usename': 'hydra-8-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '8',
  'XP': 'VI/1000+10/hp',
  'XPbase': '1000',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1360,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-9-heads': {'usename': 'hydra-9-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '9',
  'XP': 'VII/1600+12/hp',
  'XPbase': '1600',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 2080,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'jackalwere': {'usename': 'jackalwere',
  'lair': '30%',
  'Treasure': 'C',
  'HD': '4',
  'XP': 'III/110+4/hp',
  'XPbase': '110',
  'XPhp': '4',
  'HP': 18,
  'XPtotal': 182,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'lammasu': {'usename': 'lammasu',
  'lair': '30%',
  'Treasure': 'R,S,T',
  'HD': '7+7',
  'XP': 'VI/925+10/hp',
  'XPbase': '925',
  'XPhp': '10',
  'HP': 24,
  'XPtotal': 1165,
  'treasure_individual': [],
  'treasure_lair': ['R', 'S', 'T']},
 'lycanthrope-werebear': {'usename': 'lycanthrope-werebear',
  'lair': '10%',
  'Treasure': 'R,T,X',
  'HD': '7+3',
  'XP': 'VI/825+10/hp',
  'XPbase': '825',
  'XPhp': '10',
  'HP': 28,
  'XPtotal': 1105,
  'treasure_individual': [],
  'treasure_lair': ['R', 'T', 'X']},
 'lycanthrope-weretiger': {'usename': 'lycanthrope-weretiger',
  'lair': '15%',
  'Treasure': 'D,Qx5',
  'HD': '6+2',
  'XP': 'VI/525+8/hp',
  'XPbase': '525',
  'XPhp': '8',
  'HP': 25,
  'XPtotal': 725,
  'treasure_individual': [],
  'treasure_lair': ['D', 'Q', 'Q', 'Q', 'Q', 'Q']},
 'manticore': {'usename': 'manticore',
  'lair': '20%',
  'Treasure': 'E',
  'HD': '6+3',
  'XP': 'V/350+8/hp',
  'XPbase': '350',
  'XPhp': '8',
  'HP': 24,
  'XPtotal': 542,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'medusa': {'usename': 'medusa',
  'lair': '50%',
  'Treasure': 'P,Qx10,X,Y',
  'HD': '6',
  'XP': 'V/400+6/hp',
  'XPbase': '400',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 562,
  'treasure_individual': [],
  'treasure_lair': ['P',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'X',
   'Y']},
 'mold-brown': {'usename': 'mold-brown',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '0',
  'XP': 'IV/0+0/hp',
  'XPbase': '0',
  'XPhp': '0',
  'HP': 1,
  'XPtotal': 0,
  'treasure_individual': [],
  'treasure_lair': []},
 'ogre-magi': {'usename': 'ogre-magi',
  'lair': '35%',
  'Treasure': 'G(magic),R,S',
  'HD': '5+2',
  'XP': 'VI/900+6/hp',
  'XPbase': '900',
  'XPhp': '6',
  'HP': 20,
  'XPtotal': 1020,
  'treasure_individual': [],
  'treasure_lair': ['Gmagic', 'R', 'S']},
 'otyugh-6hd': {'usename': 'otyugh-6hd',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '6',
  'XP': 'IV/225+6/hp',
  'XPbase': '225',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 387,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'otyugh-7hd': {'usename': 'otyugh-7hd',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '7',
  'XP': 'V/350+8/hp',
  'XPbase': '350',
  'XPhp': '8',
  'HP': 31,
  'XPtotal': 598,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'otyugh-8hd': {'usename': 'otyugh-8hd',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '8',
  'XP': 'VI/550+10/hp',
  'XPbase': '550',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 910,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'rakshasa': {'usename': 'rakshasa',
  'lair': '25%',
  'Treasure': 'F',
  'HD': '7',
  'XP': 'VII/1050+8/hp',
  'XPbase': '1050',
  'XPhp': '8',
  'HP': 31,
  'XPtotal': 1298,
  'treasure_individual': [],
  'treasure_lair': ['F']},
 'salamander': {'usename': 'salamander',
  'lair': '75%',
  'Treasure': 'F',
  'HD': '7+7',
  'XP': 'VI/725+10/hp',
  'XPbase': '725',
  'XPhp': '10',
  'HP': 24,
  'XPtotal': 965,
  'treasure_individual': [],
  'treasure_lair': ['F']},
 'spider-phase': {'usename': 'spider-phase',
  'lair': '75%',
  'Treasure': 'E',
  'HD': '5+5',
  'XP': 'V/350+6/hp',
  'XPbase': '350',
  'XPhp': '6',
  'HP': 17,
  'XPtotal': 452,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'troll': {'usename': 'troll',
  'lair': '40%',
  'Treasure': 'D',
  'HD': '6+6',
  'XP': 'VI/525+8/hp',
  'XPbase': '525',
  'XPhp': '8',
  'HP': 21,
  'XPtotal': 693,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'wight': {'usename': 'wight',
  'lair': '70%',
  'Treasure': 'B',
  'HD': '4+3',
  'XP': 'V/330+5/hp',
  'XPbase': '330',
  'XPhp': '5',
  'HP': 15,
  'XPtotal': 405,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'wind-walker': {'usename': 'wind-walker',
  'lair': '20%',
  'Treasure': 'C,R',
  'HD': '6+3',
  'XP': 'VI/575+8/hp',
  'XPbase': '575',
  'XPhp': '8',
  'HP': 24,
  'XPtotal': 767,
  'treasure_individual': [],
  'treasure_lair': ['C', 'R']},
 'wraith': {'usename': 'wraith',
  'lair': '25%',
  'Treasure': 'E',
  'HD': '5+3',
  'XP': 'VI/525+6/hp',
  'XPbase': '525',
  'XPhp': '6',
  'HP': 19,
  'XPtotal': 639,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'wyvern': {'usename': 'wyvern',
  'lair': '30%',
  'Treasure': 'E',
  'HD': '7+7',
  'XP': 'VI/650+10/hp',
  'XPbase': '650',
  'XPhp': '10',
  'HP': 24,
  'XPtotal': 890,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'black-pudding': {'usename': 'black-pudding',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '10',
  'XP': 'VII/1350+14/hp',
  'XPbase': '1350',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 1980,
  'treasure_individual': [],
  'treasure_lair': []},
 'chimera': {'usename': 'chimera',
  'lair': '40%',
  'Treasure': 'F',
  'HD': '9',
  'XP': 'VII/1300+12/hp',
  'XPbase': '1300',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 1780,
  'treasure_individual': [],
  'treasure_lair': ['F']},
 'demon-succubus': {'usename': 'demon-succubus',
  'lair': '5%',
  'Treasure': 'I,Q',
  'HD': '6',
  'XP': 'VI/900+6/hp',
  'XPbase': '900',
  'XPhp': '6',
  'HP': 27,
  'XPtotal': 1062,
  'treasure_individual': ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'],
  'treasure_lair': []},
 'demon-type-i': {'usename': 'demon-type-i',
  'lair': '5%',
  'Treasure': 'B',
  'HD': '8',
  'XP': 'VII/1275+10/hp',
  'XPbase': '1275',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1635,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'demon-type-ii': {'usename': 'demon-type-ii',
  'lair': '10%',
  'Treasure': 'C',
  'HD': '9',
  'XP': 'VII/2300+12/hp',
  'XPbase': '2300',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 2780,
  'treasure_individual': [],
  'treasure_lair': ['C']},
 'demon-type-iii': {'usename': 'demon-type-iii',
  'lair': '15%',
  'Treasure': 'D',
  'HD': '10',
  'XP': 'VIII/3150+14/hp',
  'XPbase': '3150',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 3780,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'devil-barbed': {'usename': 'devil-barbed',
  'lair': '50%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VII/1250+10/hp',
  'XPbase': '1250',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1610,
  'treasure_individual': [],
  'treasure_lair': []},
 'devil-bone': {'usename': 'devil-bone',
  'lair': '55%',
  'Treasure': 'Nil',
  'HD': '9',
  'XP': 'VII/2400+12/hp',
  'XPbase': '2400',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 2880,
  'treasure_individual': [],
  'treasure_lair': []},
 'devil-horned': {'usename': 'devil-horned',
  'lair': '55%',
  'Treasure': 'I',
  'HD': '5+5',
  'XP': 'VI/825+6/hp',
  'XPbase': '825',
  'XPhp': '6',
  'HP': 17,
  'XPtotal': 927,
  'treasure_individual': ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'],
  'treasure_lair': []},
 'efreeti': {'usename': 'efreeti',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '10',
  'XP': 'VII/1950+14/hp',
  'XPbase': '1950',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 2580,
  'treasure_individual': [],
  'treasure_lair': []},
 'elemental-air-8hd': {'usename': 'elemental-air-8hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VI/825+10/hp',
  'XPbase': '825',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1185,
  'treasure_individual': [],
  'treasure_lair': []},
 'elemental-earth-8hd': {'usename': 'elemental-earth-8hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VI/825+10/hp',
  'XPbase': '825',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1185,
  'treasure_individual': [],
  'treasure_lair': []},
 'elemental-fire-8hd': {'usename': 'elemental-fire-8hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VI/825+10/hp',
  'XPbase': '825',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1185,
  'treasure_individual': [],
  'treasure_lair': []},
 'elemental-water-8hd': {'usename': 'elemental-water-8hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VI/825+10/hp',
  'XPbase': '825',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1185,
  'treasure_individual': [],
  'treasure_lair': []},
 'ettin': {'usename': 'ettin',
  'lair': '20%',
  'Treasure': 'O (C,Y)',
  'HD': '10',
  'XP': 'VII/1500+14/hp',
  'XPbase': '1500',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 2130,
  'treasure_individual': ['O'],
  'treasure_lair': ['C','Y']},
 'giant-hill': {'usename': 'giant-hill',
  'lair': '25%',
  'Treasure': 'D',
  'HD': '8+2',
  'XP': 'VI/900+12/hp',
  'XPbase': '900',
  'XPhp': '12',
  'HP': 34,
  'XPtotal': 1308,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'giant-stone': {'usename': 'giant-stone',
  'lair': '30%',
  'Treasure': 'D',
  'HD': '9+3',
  'XP': 'VII/1800+14/hp',
  'XPbase': '1800',
  'XPhp': '14',
  'HP': 37,
  'XPtotal': 2318,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'giant-fire': {'usename': 'giant-fire',
  'lair': '25%',
  'Treasure': 'E',
  'HD': '11+5',
  'XP': 'VIII/3550+16/hp',
  'XPbase': '3550',
  'XPhp': '16',
  'HP': 44,
  'XPtotal': 4254,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'giant-frost': {'usename': 'giant-frost',
  'lair': '30%',
  'Treasure': 'E',
  'HD': '10+4',
  'XP': 'VII/2400+14/hp',
  'XPbase': '2400',
  'XPhp': '14',
  'HP': 41,
  'XPtotal': 2974,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'golem-flesh': {'usename': 'golem-flesh',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '40 hp',
  'XP': 'VII/2980+0/hp',
  'XPbase': '2980',
  'XPhp': '0',
  'HP': '40',
  'XPtotal': 2980,
  'treasure_individual': [],
  'treasure_lair': []},
 'gorgon': {'usename': 'gorgon',
  'lair': '40%',
  'Treasure': 'E',
  'HD': '8',
  'XP': 'VI/650+10/hp',
  'XPbase': '650',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1010,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'groaning-spirit': {'usename': 'groaning-spirit',
  'lair': '10%',
  'Treasure': 'D',
  'HD': '7',
  'XP': 'VII/1100+8/hp',
  'XPbase': '1100',
  'XPhp': '8',
  'HP': 31,
  'XPtotal': 1348,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'hydra-10-heads': {'usename': 'hydra-10-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '10',
  'XP': 'VII/2400+14/hp',
  'XPbase': '2400',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 3030,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-11-heads': {'usename': 'hydra-11-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '11',
  'XP': 'VIII/3550+16/hp',
  'XPbase': '3550',
  'XPhp': '16',
  'HP': 49,
  'XPtotal': 4334,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-12-heads': {'usename': 'hydra-12-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '12',
  'XP': 'VIII/3550+16/hp',
  'XPbase': '3550',
  'XPhp': '16',
  'HP': 54,
  'XPtotal': 4414,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-pyro-8-heads': {'usename': 'hydra-pyro-8-heads',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '7',
  'XP': 'VII/1275+10/hp',
  'XPbase': '1275',
  'XPhp': '10',
  'HP': 31,
  'XPtotal': 1585,
  'treasure_individual': [],
  'treasure_lair': []},
 'intellect-devourer': {'usename': 'intellect-devourer',
  'lair': '60%',
  'Treasure': 'D',
  'HD': '6+6',
  'XP': 'VI/1000+8/hp',
  'XPbase': '1000',
  'XPhp': '8',
  'HP': 21,
  'XPtotal': 1168,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'invisible-stalker': {'usename': 'invisible-stalker',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VI/1000+10/hp',
  'XPbase': '1000',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1360,
  'treasure_individual': [],
  'treasure_lair': []},
 'lamia': {'usename': 'lamia',
  'lair': '60%',
  'Treasure': 'D',
  'HD': '9',
  'XP': 'VII/1300+12/hp',
  'XPbase': '1300',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 1780,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'lizard-fire': {'usename': 'lizard-fire',
  'lair': '50%',
  'Treasure': 'B,Qx10,S,T',
  'HD': '10',
  'XP': 'VII/1950+14/hp',
  'XPbase': '1950',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 2580,
  'treasure_individual': [],
  'treasure_lair': ['B',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'S',
   'T']},
 'lurker-above': {'usename': 'lurker-above',
  'lair': '50%',
  'Treasure': 'C,Y',
  'HD': '10',
  'XP': 'VII/1500+14/hp',
  'XPbase': '1500',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 2130,
  'treasure_individual': [],
  'treasure_lair': ['C', 'Y']},
 'mezzodaemon': {'usename': 'mezzodaemon',
  'lair': '0%',
  'Treasure': 'Qx5 (X)',
  'HD': '10+40',
  'XP': 'VII/2800+14/hp',
  'XPbase': '2800',
  'XPhp': '14',
  'HP': 5,
  'XPtotal': 2870,
  'treasure_individual': [],
  'treasure_lair': []},
 'mimic-8hd': {'usename': 'mimic-8hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VI/550+10/hp',
  'XPbase': '550',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 910,
  'treasure_individual': [],
  'treasure_lair': []},
 'mimic-9hd': {'usename': 'mimic-9hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '9',
  'XP': 'VI/900+12/hp',
  'XPbase': '900',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 1380,
  'treasure_individual': [],
  'treasure_lair': []},
 'mimic-10hd': {'usename': 'mimic-10hd',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '10',
  'XP': 'VII/1350+14/hp',
  'XPbase': '1350',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 1980,
  'treasure_individual': [],
  'treasure_lair': []},
 'mind-flayer': {'usename': 'mind-flayer',
  'lair': '50%',
  'Treasure': 'B,S,T,X',
  'HD': '8+4',
  'XP': 'VII/1800+12/hp',
  'XPbase': '1800',
  'XPhp': '12',
  'HP': 32,
  'XPtotal': 2184,
  'treasure_individual': [],
  'treasure_lair': ['B', 'S', 'T', 'X']},
 'mummy': {'usename': 'mummy',
  'lair': '80%',
  'Treasure': 'D',
  'HD': '6+3',
  'XP': 'VII/1150+8/hp',
  'XPbase': '1150',
  'XPhp': '8',
  'HP': 24,
  'XPtotal': 1342,
  'treasure_individual': [],
  'treasure_lair': ['D']},
 'naga-spirit-10hd': {'usename': 'naga-spirit-10hd',
  'lair': '60%',
  'Treasure': 'B,T,X',
  'HD': '10',
  'XP': 'VII/2700+14/hp',
  'XPbase': '2700',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 3330,
  'treasure_individual': [],
  'treasure_lair': ['B', 'T', 'X']},
 'neo-otyugh-9hd': {'usename': 'neo-otyugh-9hd',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '9',
  'XP': 'VII/1500+14/hp',
  'XPbase': '1500',
  'XPhp': '14',
  'HP': 40,
  'XPtotal': 2060,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'neo-otyugh-10hd': {'usename': 'neo-otyugh-10hd',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '10',
  'XP': 'VII/2250+14/hp',
  'XPbase': '2250',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 2880,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'night-hag': {'usename': 'night-hag',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VII/1750+10/hp',
  'XPbase': '1750',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 2110,
  'treasure_individual': [],
  'treasure_lair': []},
 'roper-10hd': {'usename': 'roper-10hd',
  'lair': '90%',
  'Treasure': 'Special',
  'HD': '10',
  'XP': 'VII/3000+14/hp',
  'XPbase': '3000',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 3630,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'roper-11hd': {'usename': 'roper-11hd',
  'lair': '90%',
  'Treasure': 'Special',
  'HD': '11',
  'XP': 'VIII/4400+16/hp',
  'XPbase': '4400',
  'XPhp': '16',
  'HP': 49,
  'XPtotal': 5184,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'roper-12hd': {'usename': 'roper-12hd',
  'lair': '90%',
  'Treasure': 'Special',
  'HD': '12',
  'XP': 'VIII/4400+16/hp',
  'XPbase': '4400',
  'XPhp': '16',
  'HP': 54,
  'XPtotal': 5264,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'shambling-mound-8hd': {'usename': 'shambling-mound-8hd',
  'lair': '30%',
  'Treasure': 'B,T,X',
  'HD': '8',
  'XP': 'VII/1175+10/hp',
  'XPbase': '1175',
  'XPhp': '10',
  'HP': 36,
  'XPtotal': 1535,
  'treasure_individual': [],
  'treasure_lair': ['B', 'T', 'X']},
 'shambling-mound-9hd': {'usename': 'shambling-mound-9hd',
  'lair': '30%',
  'Treasure': 'B,T,X',
  'HD': '9',
  'XP': 'VII/1900+12/hp',
  'XPbase': '1900',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 2380,
  'treasure_individual': [],
  'treasure_lair': ['B', 'T', 'X']},
 'shambling-mound-10hd': {'usename': 'shambling-mound-10hd',
  'lair': '30%',
  'Treasure': 'B,T,X',
  'HD': '10',
  'XP': 'VII/2850+14/hp',
  'XPbase': '2850',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 3480,
  'treasure_individual': [],
  'treasure_lair': ['B', 'T', 'X']},
 'shambling-mound-11hd': {'usename': 'shambling-mound-11hd',
  'lair': '30%',
  'Treasure': 'B,T,X',
  'HD': '11',
  'XP': 'VIII/4250+16/hp',
  'XPbase': '4250',
  'XPhp': '16',
  'HP': 49,
  'XPtotal': 5034,
  'treasure_individual': [],
  'treasure_lair': ['B', 'T', 'X']},
 'shedu': {'usename': 'shedu',
  'lair': '25%',
  'Treasure': 'G',
  'HD': '9+9',
  'XP': 'VII/1950+14/hp',
  'XPbase': '1950',
  'XPhp': '14',
  'HP': 31,
  'XPtotal': 2384,
  'treasure_individual': [],
  'treasure_lair': ['G']},
 'slug-giant': {'usename': 'slug-giant',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '12',
  'XP': 'VII/2000+16/hp',
  'XPbase': '2000',
  'XPhp': '16',
  'HP': 54,
  'XPtotal': 2864,
  'treasure_individual': [],
  'treasure_lair': []},
 'spectre': {'usename': 'spectre',
  'lair': '20%',
  'Treasure': 'Qx3,X,Y',
  'HD': '7+3',
  'XP': 'VII/1350+10/hp',
  'XPbase': '1350',
  'XPhp': '10',
  'HP': 28,
  'XPtotal': 1630,
  'treasure_individual': [],
  'treasure_lair': ['Q', 'Q', 'Q', 'X', 'Y']},
 'trapper': {'usename': 'trapper',
  'lair': '85%',
  'Treasure': 'G',
  'HD': '12',
  'XP': 'VII/2850+16/hp',
  'XPbase': '2850',
  'XPhp': '16',
  'HP': 54,
  'XPtotal': 3714,
  'treasure_individual': [],
  'treasure_lair': ['G']},
 'umber-hulk': {'usename': 'umber-hulk',
  'lair': '30%',
  'Treasure': 'G',
  'HD': '8+8',
  'XP': 'VII/1600+12/hp',
  'XPbase': '1600',
  'XPhp': '12',
  'HP': 28,
  'XPtotal': 1936,
  'treasure_individual': [],
  'treasure_lair': ['G']},
 'will-o-wisp': {'usename': 'will-o-wisp',
  'lair': '5%',
  'Treasure': 'Z',
  'HD': '9',
  'XP': 'VII/1600+12/hp',
  'XPbase': '1600',
  'XPhp': '12',
  'HP': 40,
  'XPtotal': 2080,
  'treasure_individual': [],
  'treasure_lair': ['Z']},
 'xorn': {'usename': 'xorn',
  'lair': '40%',
  'Treasure': 'O,P,Qx5,X,Y',
  'HD': '7+7',
  'XP': 'VII/1275+10/hp',
  'XPbase': '1275',
  'XPhp': '10',
  'HP': 24,
  'XPtotal': 1515,
  'treasure_individual': [],
  'treasure_lair': ['O', 'P', 'Q', 'Q', 'Q', 'Q', 'Q', 'X', 'Y']},
 'aerial-servant': {'usename': 'aerial-servant',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '16',
  'XP': 'IX/6500+20/hp',
  'XPbase': '6500',
  'XPhp': '20',
  'HP': 72,
  'XPtotal': 7940,
  'treasure_individual': [],
  'treasure_lair': []},
 'demon-type-iv': {'usename': 'demon-type-iv',
  'lair': '15%',
  'Treasure': 'E',
  'HD': '11',
  'XP': 'VIII/5250+16/hp',
  'XPbase': '5250',
  'XPhp': '16',
  'HP': 49,
  'XPtotal': 6034,
  'treasure_individual': [],
  'treasure_lair': ['E']},
 'demon-type-v': {'usename': 'demon-type-v',
  'lair': '10%',
  'Treasure': 'G',
  'HD': '7+7',
  'XP': 'VII/2000+10/hp',
  'XPbase': '2000',
  'XPhp': '10',
  'HP': 24,
  'XPtotal': 2240,
  'treasure_individual': [],
  'treasure_lair': ['G']},
 'demon-type-vi': {'usename': 'demon-type-vi',
  'lair': '20%',
  'Treasure': 'F',
  'HD': '8+8',
  'XP': 'IX/5600+12/hp',
  'XPbase': '5600',
  'XPhp': '12',
  'HP': 28,
  'XPtotal': 5936,
  'treasure_individual': [],
  'treasure_lair': ['F']},
 'devil-ice': {'usename': 'devil-ice',
  'lair': '60%',
  'Treasure': 'Q,R',
  'HD': '11',
  'XP': 'VIII/4400+16/hp',
  'XPbase': '4400',
  'XPhp': '16',
  'HP': 49,
  'XPtotal': 5184,
  'treasure_individual': [],
  'treasure_lair': ['Q', 'R']},
 'ghost': {'usename': 'ghost',
  'lair': '25%',
  'Treasure': 'E,S',
  'HD': '10',
  'XP': 'VIII/4050+14/hp',
  'XPbase': '4050',
  'XPhp': '14',
  'HP': 45,
  'XPtotal': 4680,
  'treasure_individual': [],
  'treasure_lair': ['E', 'S']},
 'giant-cloud': {'usename': 'giant-cloud',
  'lair': '40%',
  'Treasure': 'E,Q(x5',
  'HD': '12+7',
  'XP': 'VIII/4250+16/hp',
  'XPbase': '4250',
  'XPhp': '16',
  'HP': 47,
  'XPtotal': 5002,
  'treasure_individual': [],
  'treasure_lair': ['E', 'Q', 'Q', 'Q', 'Q', 'Q']},
 'golem-clay': {'usename': 'golem-clay',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '50 hp',
  'XP': 'VII/5350+0/hp',
  'XPbase': '5350',
  'XPhp': '0',
  'HP': '50',
  'XPtotal': 5350,
  'treasure_individual': [],
  'treasure_lair': []},
 'hydra-13-heads': {'usename': 'hydra-13-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '13',
  'XP': 'VIII/4900+18/hp',
  'XPbase': '4900',
  'XPhp': '18',
  'HP': 58,
  'XPtotal': 5944,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-14-heads': {'usename': 'hydra-14-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '14',
  'XP': 'VIII/4900+18/hp',
  'XPbase': '4900',
  'XPhp': '18',
  'HP': 63,
  'XPtotal': 6034,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-15-heads': {'usename': 'hydra-15-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '15',
  'XP': 'IX/6500+20/hp',
  'XPbase': '6500',
  'XPhp': '20',
  'HP': 67,
  'XPtotal': 7840,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'hydra-pyro-12-heads': {'usename': 'hydra-pyro-12-heads',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '8',
  'XP': 'VIII/4400+16/hp',
  'XPbase': '4400',
  'XPhp': '16',
  'HP': 36,
  'XPtotal': 4976,
  'treasure_individual': [],
  'treasure_lair': []},
 'naga-guardian-11hd': {'usename': 'naga-guardian-11hd',
  'lair': '75%',
  'Treasure': 'H',
  'HD': '11',
  'XP': 'VIII/3550+16/hp',
  'XPbase': '3550',
  'XPhp': '16',
  'HP': 49,
  'XPtotal': 4334,
  'treasure_individual': [],
  'treasure_lair': ['H']},
 'naga-guardian-12hd': {'usename': 'naga-guardian-12hd',
  'lair': '75%',
  'Treasure': 'H',
  'HD': '12',
  'XP': 'VIII/3550+16/hp',
  'XPbase': '3550',
  'XPhp': '16',
  'HP': 54,
  'XPtotal': 4414,
  'treasure_individual': [],
  'treasure_lair': ['H']},
 'neo-otyugh-11hd': {'usename': 'neo-otyugh-11hd',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '11',
  'XP': 'VIII/3400+16/hp',
  'XPbase': '3400',
  'XPhp': '16',
  'HP': 49,
  'XPtotal': 4184,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'neo-otyugh-12hd': {'usename': 'neo-otyugh-12hd',
  'lair': '0%',
  'Treasure': 'Special',
  'HD': '12',
  'XP': 'VIII/3400+16/hp',
  'XPbase': '3400',
  'XPhp': '16',
  'HP': 54,
  'XPtotal': 4264,
  'treasure_individual': [],
  'treasure_lair': ['Special']},
 'purple-worm': {'usename': 'purple-worm',
  'lair': '30%',
  'Treasure': 'B,Q(x5),X',
  'HD': '15',
  'XP': 'IX/5600+20/hp',
  'XPbase': '5600',
  'XPhp': '20',
  'HP': 67,
  'XPtotal': 6940,
  'treasure_individual': [],
  'treasure_lair': ['B', 'Q', 'Q', 'Q', 'Q', 'Q', 'X']},
 'vampire': {'usename': 'vampire',
  'lair': '25%',
  'Treasure': 'F',
  'HD': '8+3',
  'XP': 'VIII/3800+12/hp',
  'XPbase': '3800',
  'XPhp': '12',
  'HP': 33,
  'XPtotal': 4196,
  'treasure_individual': [],
  'treasure_lair': ['F']},
 'devil-pit-fiend': {'usename': 'devil-pit-fiend',
  'lair': '65%',
  'Treasure': 'J,R',
  'HD': '13',
  'XP': 'IX/7900+18/hp',
  'XPbase': '7900',
  'XPhp': '18',
  'HP': 58,
  'XPtotal': 8944,
  'treasure_individual': ['Q', 'Q', 'Q', 'Q', 'Q'],
  'treasure_lair': []},
 'giant-storm': {'usename': 'giant-storm',
  'lair': '55%',
  'Treasure': 'E,Q(x10),S',
  'HD': '15+7',
  'XP': 'IX/5600+20/hp',
  'XPbase': '5600',
  'XPhp': '20',
  'HP': 60,
  'XPtotal': 6800,
  'treasure_individual': [],
  'treasure_lair': ['E',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'S']},
 'golem-stone': {'usename': 'golem-stone',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '60 hp',
  'XP': 'IX/8950+0/hp',
  'XPbase': '8950',
  'XPhp': '0',
  'HP': '60',
  'XPtotal': 8950,
  'treasure_individual': [],
  'treasure_lair': []},
 'hydra-16-heads': {'usename': 'hydra-16-heads',
  'lair': '20%',
  'Treasure': 'B',
  'HD': '16',
  'XP': 'IX/6500+20/hp',
  'XPbase': '6500',
  'XPhp': '20',
  'HP': 72,
  'XPtotal': 7940,
  'treasure_individual': [],
  'treasure_lair': ['B']},
 'nycadaemon': {'usename': 'nycadaemon',
  'lair': '0%',
  'Treasure': 'Qx10,X',
  'HD': '12+36',
  'XP': 'IX/6800+16/hp',
  'XPbase': '6800',
  'XPhp': '16',
  'HP': 18,
  'XPtotal': 7088,
  'treasure_individual': [],
  'treasure_lair': ['Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'X']},
 'titan-17hd': {'usename': 'titan-17hd',
  'lair': '10%',
  'Treasure': 'E,Qx10,R',
  'HD': '17',
  'XP': 'IX/9000+25/hp',
  'XPbase': '9000',
  'XPhp': '25',
  'HP': 76,
  'XPtotal': 10900,
  'treasure_individual': [],
  'treasure_lair': ['E',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']},
 'titan-18hd': {'usename': 'titan-18hd',
  'lair': '10%',
  'Treasure': 'E,Qx10,R',
  'HD': '18',
  'XP': 'IX/9000+25/hp',
  'XPbase': '9000',
  'XPhp': '25',
  'HP': 81,
  'XPtotal': 11025,
  'treasure_individual': [],
  'treasure_lair': ['E',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']},
 'titan-19hd': {'usename': 'titan-19hd',
  'lair': '10%',
  'Treasure': 'E,Qx10,R',
  'HD': '19',
  'XP': 'X/13600+30/hp',
  'XPbase': '13600',
  'XPhp': '30',
  'HP': 85,
  'XPtotal': 16150,
  'treasure_individual': [],
  'treasure_lair': ['E',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']},
 'titan-20hd': {'usename': 'titan-20hd',
  'lair': '10%',
  'Treasure': 'E,Qx10,R',
  'HD': '20',
  'XP': 'X/13600+30/hp',
  'XPbase': '13600',
  'XPhp': '30',
  'HP': 90,
  'XPtotal': 16300,
  'treasure_individual': [],
  'treasure_lair': ['E',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']},
 'beholder': {'usename': 'beholder',
  'lair': '80%',
  'Treasure': 'I,S,T',
  'HD': '45 to 75 hp',
  'XP': 'X/12900+20/hp',
  'XPbase': '12900',
  'XPhp': '20',
  'HP': '45',
  'XPtotal': 13800,
  'treasure_individual': ['Q', 'Q', 'Q', 'Q', 'Q'],
  'treasure_lair': []},
 'demon-prince-demogorgon': {'usename': 'demon-prince-demogorgon',
  'lair': '50%',
  'Treasure': 'R,S,T,V',
  'HD': '200 hp',
  'XP': 'X/74000+0/hp',
  'XPbase': '74000',
  'XPhp': '0',
  'HP': '200',
  'XPtotal': 74000,
  'treasure_individual': [],
  'treasure_lair': ['R', 'S', 'T', 'V']},
 'demon-prince-juiblex': {'usename': 'demon-prince-juiblex',
  'lair': '60%',
  'Treasure': 'P(x2),R(x2)',
  'HD': '88 hp',
  'XP': 'X/47280+0/hp',
  'XPbase': '47280',
  'XPhp': '0',
  'HP': '88',
  'XPtotal': 47280,
  'treasure_individual': [],
  'treasure_lair': ['P', 'P', 'R', 'R']},
 'demon-prince-orcus': {'usename': 'demon-prince-orcus',
  'lair': '50%',
  'Treasure': 'P,S,T,U',
  'HD': '120 hp',
  'XP': 'X/63900+0/hp',
  'XPbase': '63900',
  'XPhp': '0',
  'HP': '120',
  'XPtotal': 63900,
  'treasure_individual': [],
  'treasure_lair': ['P', 'S', 'T', 'U']},
 'demon-prince-yeenoghu': {'usename': 'demon-prince-yeenoghu',
  'lair': '35%',
  'Treasure': 'C,G,I',
  'HD': '100 hp',
  'XP': 'X/54500+0/hp',
  'XPbase': '54500',
  'XPhp': '0',
  'HP': '100',
  'XPtotal': 54500,
  'treasure_individual': ['Q', 'Q', 'Q', 'Q', 'Q'],
  'treasure_lair': []},
 'devil-arch-asmodeus': {'usename': 'devil-arch-asmodeus',
  'lair': '90%',
  'Treasure': 'I,R,U,V',
  'HD': '199 hp',
  'XP': 'X/70965+0/hp',
  'XPbase': '70965',
  'XPhp': '0',
  'HP': '199',
  'XPtotal': 70965,
  'treasure_individual': ['Q', 'Q', 'Q', 'Q', 'Q'],
  'treasure_lair': []},
 'devil-arch-baalzebul': {'usename': 'devil-arch-baalzebul',
  'lair': '80%',
  'Treasure': 'E,R,V',
  'HD': '166 hp',
  'XP': 'X/61410+0/hp',
  'XPbase': '61410',
  'XPhp': '0',
  'HP': '166',
  'XPtotal': 61410,
  'treasure_individual': [],
  'treasure_lair': ['E', 'R', 'V']},
 'devil-arch-dispater': {'usename': 'devil-arch-dispater',
  'lair': '80%',
  'Treasure': 'Q(x10),S',
  'HD': '144 hp',
  'XP': 'X/48040+0/hp',
  'XPbase': '48040',
  'XPhp': '0',
  'HP': '144',
  'XPtotal': 48040,
  'treasure_individual': [],
  'treasure_lair': ['Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'S']},
 'devil-arch-geryon': {'usename': 'devil-arch-geryon',
  'lair': '70%',
  'Treasure': 'H,R',
  'HD': '133 hp',
  'XP': 'X/47795+0/hp',
  'XPbase': '47795',
  'XPhp': '0',
  'HP': '133',
  'XPtotal': 47795,
  'treasure_individual': [],
  'treasure_lair': ['H', 'R']},
 'golem-iron': {'usename': 'golem-iron',
  'lair': '0%',
  'Treasure': 'Nil',
  'HD': '80 hp',
  'XP': 'X/14550+0/hp',
  'XPbase': '14550',
  'XPhp': '0',
  'HP': '80',
  'XPtotal': 14550,
  'treasure_individual': [],
  'treasure_lair': []},
 'lich': {'usename': 'lich',
  'lair': '90%',
  'Treasure': 'A',
  'HD': '12',
  'XP': 'X/10500+25/hp',
  'XPbase': '10500',
  'XPhp': '25',
  'HP': 54,
  'XPtotal': 11850,
  'treasure_individual': [],
  'treasure_lair': ['A']},
 'titan-21hd': {'usename': 'titan-21hd',
  'lair': '10%',
  'Treasure': 'E,Qx10,R',
  'HD': '21',
  'XP': 'X/16600+35/hp',
  'XPbase': '16600',
  'XPhp': '35',
  'HP': 94,
  'XPtotal': 19890,
  'treasure_individual': [],
  'treasure_lair': ['E',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']},
 'titan-22hd': {'usename': 'titan-22hd',
  'lair': '10%',
  'Treasure': 'E,Qx10,R',
  'HD': '22',
  'XP': 'X/16600+35/hp',
  'XPbase': '16600',
  'XPhp': '35',
  'HP': 99,
  'XPtotal': 20065,
  'treasure_individual': [],
  'treasure_lair': ['E',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'Q',
   'R']}}
    return ad    

def monster_tables(level):
    v = 0
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
    #human variable need to do for dwarves etc.
    level_01 ='''01-02 Ant, giant 1-4
    03-04 Badger 1-4
    05-14 Beetle, fire 1-4
    15 Demon, manes 1-4
    16 Dwarf-hill 4-14
    17 Dwarf-mountain 4-14
    18 Ear-seeker 1-1
    19 Elf 3-11
    20-21 Gnome 5-15
    22-26 Goblin 6-15
    27-28 Halfling 9-16
    29-33 Hobgoblin 2-8
    34-48 Human — see Human Subtable below 1-1
    49-54 Kobold 6-18
    55-66 Orc 7-12
    67-70 Piercer-1HD 1-3
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

    level_02='''01 Badger, giant 1-4
    02-16 Centipede, giant 3-13
    17-27 Character — see Character Subtable 1-1
    28-29 Devil, lemure 2-5
    30-31 Gas-spore 1-2
    32-38 Gnoll 4-10
    39-46 Piercer-2HD 1-4
    47-58 Rat, giant 6-24
    59-60 Rot-grub 1-4
    61-72 Shrieker 1-3
    73-77 Stirge 5-15
    78-87 Toad, giant 1-4
    88-100 Troglodyte 2-8'''

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
    73 Piercer-3HD 2-5
    74 Piercer-4HD 2-5
    75 Rot-grub 1-4
    76-77 Shrieker 2-5
    78-84 Spider, huge 1-3
    85-93 Spider, large 2-5
    94 Tick, giant-2HD 1-3
    95 Tick, giant-3HD 1-3
    96 Tick, giant-4HD 1-3
    97-100 Weasel, giant 1-4''' 

    dragon_level_03 = '''01-28 Black:very-young (1)
    29-62 Brass:very-young (1)
    63-100 White:very-young (1)'''
    
    #, 5-or-6heads and, pyro-5-heads
    level_04 = '''01-08 Ape, carnivorous 1-3
    09-14 Blink-dog 2-5
    15-22 Character — see Character Subtable 1-1
    23-24 Dragon — see Dragon Subtable below 1-1
    25-30 Gargoyle 1-2
    31-36 Ghast 1-4
    37-40 Gray-ooze 1-1
    41 Hell-hound-4HD 1-2
    42 Hell-hound-5HD 1-2
    43 Hell-hound-6HD 1-2
    44 Hell-hound-7HD 1-2
    45-46 Hydra-5-heads 1-1
    47 Hydra-6-heads 1-1
    48 Hydra-pyro-5-heads 1-1
    49-62 Lycanthrope, werewolf 1-2
    63-75 Mold, yellow 1-1
    76-78 Owlbear 1-2
    79 Rust-monster 1-1
    80-82 Shadow 1-3
    83-90 Snake, giant, constrictor 1-1
    91-94 Su-monster 1-2
    95-96 Toad, ice 1-1
    97-100 Toad, poisonous 1-3'''

    dragon_level_04 = '''01-09 Black:young/sub-adult (2/3)
    10-20 Blue:very young/young (1/2)
    21-30 Brass:young/sub-adult (2/3)
    31-37 Bronze:very-young/young (1/2)
    38-50 Copper:very-young/young (1/2)
    51-54 Gold:very-young/young (1/2)
    55-70 Green:very-young/young (1/2)
    71-80 Red:very-young/young (1/2)
    81-88 Silver:very-young/young (1/2)
    89-100 White:young/sub-adult (2/3)'''

    #, 7heads and, pyro-6-heads
    level_05='''01-08 Character — see Character Subtable 1-1
    09-15 Cockatrice 1-2
    16-18 Displacer-beast 1-2
    19-22 Doppleganger 1-3
    23-24 Dragon — see Dragon Subtable below 1-1
    25-26 Hydra-7-heads 1-1
    27 Hydra-pyro-6-heads 1-1
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
    87-100 Spider, giant 1-2'''

    dragon_level_05='''01-08 Black:young-adult/adult (4/5)
    09-20 Blue:sub-adult/young-adult (3/4)
    21-30 Brass:young-adult/adult (4/5)
    31-37 Bronze:sub-adult/young-adult (3/4)
    38-50 Copper:sub-adult/young-adult (3/4)
    51-54 Gold:sub-adult/young-adult (3/4)
    55-70 Green:sub-adult/young-adult (3/4)
    71-80 Red:sub-adult/young-adult (3/4)
    81-88 Silver:sub-adult/young-adult (3/4)
    89-100 White:young-adult/adult (4/5)'''    

    #8-9heads
    level_06='''01-03 Basilisk 1-1
    04-10 Carrion-crawler 1-2
    11-16 Character — see Character Subtable 1-1
    17 Devil, erinyes 1-2
    18-19 Djinni 1-1
    20-21 Dragon — see Dragon Subtable below 1-1
    22-25 Green-slime 1-1
    26 Hydra-8-heads 1-1
    27 Hydra-8-heads 1-1
    28 Hydra-9-heads 1-1
    29-32 Jackalwere 1-2
    33-36 Lammasu 1-3
    37-38 Lycanthrope, werebear 1-1
    39-41 Lycanthrope, weretiger 1-2
    42-50 Manticore 1-2
    51-55 Medusa 1-1
    56 Mold, brown 1-1
    57-58 Mold, yellow 1-1
    59-60 Ogre-magi 1-2
    61-63 Otyugh-6HD 1-1
    64-66 Otyugh-7HD 1-1
    67-68 Otyugh-8HD 1-1
    69-70 Rakshasa 1-1
    71-73 Salamander 1-2
    74-77 Spider, phase 1-3
    78-88 Troll 1-3
    89-93 Wight 1-4
    94-95 Wind-walker 1-2
    96-98 Wraith 1-2
    99-100 Wyvern 1-1'''

    dragon_level_06='''01-08 Black:old (6)
    09-19 Blue:adult (5)
    20-29 Brass:old (6)
    30-36 Bronze:adult (5)
    37-48 Copper:adult (5)
    49-52 Gold:adult (5)
    53-65 Green:adult (5)
    66-78 Red:adult (5)
    79-87 Silver:adult (5)
    88-100 White:old (6)'''   

    #10-12heads and, pyro-7-9-heads
    #modified a few to have HD
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
    25 Elemental-air-8HD 1-1
    26 Elemental-earth-8HD 1-1
    27 Elemental-fire-8HD 1-1
    28 Elemental-water-8HD 1-1
    29-31 Ettin 1-2
    32-33 Giant, hill 1-3
    34-35 Giant, stone 1-3
    36-37 Giant, fire 1-2
    38 Giant, frost 1-2
    39 Golem, flesh 1-1
    40-41 Gorgon 1-1
    42-43 Groaning-spirit 1-1
    44 Hydra-10-heads 1-1
    45 Hydra-11-heads 1-1
    46 Hydra-12-heads 1-1
    47 Hydra-pyro-8-heads 1-1
    48-49 Intellect-devourer 1-1
    50 Invisible-stalker 1-1
    51-52 Lamia 1-2
    53-56 Lizard, fire 1-3
    57-59 Lurker-above 1-1
    60 Mezzodaemon 1-1
    61 Mimic-8HD 1-1
    62 Mimic-9HD 1-1
    63 Mimic-10HD 1-1
    64-65 Mind-flayer 1-2
    66-69 Mummy 1-2
    70 Naga, spirit-10HD 1-2
    71-72 Neo-otyugh-9HD 1-1
    73 Neo-otyugh-10HD 1-1
    74 Night-hag 1-2
    75-76 Roper-10HD 1-2
    77 Roper-11HD 1-2
    78 Roper-12HD 1-2
    79 Shambling-mound-8HD 1-2
    80 Shambling-mound-9HD 1-2
    81 Shambling-mound-10HD 1-2
    82 Shambling-mound-11HD 1-2
    83-86 Shedu 1-2
    87 Slug, giant 1-1
    88-91 Spectre 1-1
    92-93 Trapper 1-1
    94-95 Umber-hulk 1-1
    96-97 Will-o-wisp 1-3
    98-100 Xorn 1-3'''

    dragon_level_07='''01-10 Black:very-old (7)
    11-21 Blue:old (6)
    22-29 Brass:very-old (7)
    30-36 Bronze:old (6)
    37-48 Copper:old (6)
    49-52 Gold:old (6)
    53-66 Green:old (6)
    67-80 Red:old (6)
    81-87 Silver:old (6)
    88-100 White:very-old (7)'''    

    #13-16heads and, pyro-12heads
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
    24 Hydra-13-heads 1-1
    25 Hydra-14-heads 1-1
    26 Hydra-15-heads 1-1
    27 Hydra-pyro-12-heads 1-1
    28-29 Intellect-devourer 1-2
    30-35 Lurker-above 1-1
    36-41 Mold, brown 1-1
    42-43 Mold, yellow 1-1
    44-47 Mind-flayer 1-4
    48-49 Naga, guardian-11HD 1-2
    50 Naga, guardian-12HD 1-2
    51-53 Neo-otyugh-11HD 1-1
    54-56 Neo-otyugh-12HD 1-1
    57-64 Purple-worm 1-1
    65-69 Rust-monster 1-1
    70-73 Slug, giant 1-1
    74-78 Trapper 1-1
    79-86 Vampire 1-1
    87-92 Will-o-wisp 2-5
    93-100 Xorn 2-5'''

    dragon_level_08='''01-13 Black:ancient (8)
    14-24 Blue:very-old (7)
    25-31 Brass:ancient (8)
    32-35 Bronze:very-old (7)
    36-43 Copper:very-old (7)
    44-47 Gold:very-old (7)
    48-62 Green:very-old (7)
    63-78 Red:very-old (7)
    79-82 Silver:very-old (7)
    83-100 White:ancient (8)'''

    #17-20heads and, pyro-12heads
    #Titan lesser minor
    level_09='''01-09 Character — see Character Subtable 1-1
    10-12 Devil, pit-fiend 1-1
    13-15 Dragon — see Dragon Subtable below 1-2
    16-21 Giant, storm 1-2
    22-23 Golem, stone 1-1
    24-30 Hydra-16-heads 1-1
    31-33 Hydra-pyro-12-heads 1-1
    34-40 Mold, brown 1-1
    41-50 Mold, yellow 1-1
    51-52 Nycadaemon 1-1
    53-64 Purple-worm 1-1
    65-67 Rust-monster 1-1
    68 Titan-17HD 1-1
    69 Titan-18HD 1-1
    70-71 Titan-19HD 1-1
    72-73 Titan-20HD 1-1
    74-80 Umber-Hulk 1-4
    81-83 Vampire 1-1
    84-93 Will-o-wisp 2-5
    94-100 Xorn 2-9'''

    dragon_level_09='''01-10 Black:2-ancient-&-old (8&6)
    11-22 Blue:ancient (8)
    23-31 Brass:2-ancient-&-old (8&6)
    32-34 Bronze:ancient (8)
    35-42 Copper:ancient (8)
    43-46 Gold:ancient (8)
    47-62 Green:ancient (8)
    63-78 Red:ancient (8)
    79-82 Silver:ancient (8)
    83-100 White:2-ancient-&-very-old (8&7)'''    

    #Titan elder
    level_10 ='''01-12 Beholder 1-1
    13-20 Character — see Character Subtable 1-1
    21-22 Demon, prince-Demogorgon 1-1
    23-24 Demon, prince-Juiblex 1-1
    25-26 Demon, prince-Orcus 1-1
    27-28 Demon, prince-Yeenoghu 1-1
    29 Devil, arch-Asmodeus 1-1
    30 Devil, arch-Baalzebul 1-1
    31 Devil, arch-Dispater 1-1
    32 Devil, arch-Geryon 1-1
    33-42 Dragon — see Dragon Subtable below 1-2
    43-52 Golem, iron 1-1
    53-62 Lich 1-1
    63-67 Titan-21HD 1-1
    68-72 Titan-22HD 1-1 
    73-82 Vampire 1-1
    83-100 NO-ENCOUNTER 1-1'''    

    dragon_level_10='''01-20 Blue:2-ancient-&-very-old (8&7)
    21-26 Bronze:2-ancient-&-very-old (8&7)
    27-33 Copper:2-ancient-&-very-old (8&7)
    34-35 Chromatic:-(Tiamat) (8)
    36-40 Gold:2-ancient-&-old (8&6)
    41-60 Green:2-ancient-&-very old (8&7)
    61-63 Platinum:-(Bahamut) (8)
    64-94 Red:2-ancient-&-old (8&6)
    95-100 Silver:2-ancient-&-old (8&-6)'''

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


    if int(mcheck['roll'][0]) == 1 and int(mcheck['roll'][1]) == 1:
        mno = 1
    else:
        if mcheck['roll'][0] == 1:
            mno = roll_dice(mcheck['roll'][0],mcheck['roll'][1]) + mcheck['roll'][2]
        else:
            mno = multi_roll(mcheck['roll'][0],mcheck['roll'][1]) + mcheck['roll'][2]

    if v:
        print("CHECKINGM",mcheck,"LEVEL:",level,"ROLL:",m)
        print("choose monster", mcheck)

    mdict = {}
    mdict['name'] = mcheck['name']
    mdict['no'] = mno

    from characters import select_human, create_party

    if mdict['name'] == 'Human-HumanSubtable':
        mdict['details'] = select_human(level)

    if mdict['name'] == 'Character-CharacterSubtable':
        mdict['details'] = create_party(level)

    #dragon test
    #mdict['name'] == 'Dragon-DragonSubtable'
    if mdict['name'] == 'Dragon-DragonSubtable':
        #dragon hack to avoid calculating out every dragon * every age
        #take max value of DMG page 175 table
        #base value
        dragon_xp = {}
        dragon_xp[3] = 150
        dragon_xp[4] = 250
        dragon_xp[5] = 500
        dragon_xp[6] = 1000
        dragon_xp[7] = 1000
        dragon_xp[8] = 1000
        dragon_xp[9] = 10000
        dragon_xp[10] = 20000
        #630580/58080

        mdict['details'] = 'NOT IMPLEMENTED YET'

        if 1 == 1:

            for ld in range(10):
                if ld < 2:
                    continue
                #print("dragon_levels:",ld)
                uselevel = dragon_levels[ld+1]['data'].split("\n")
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
                    
                    #print(number_range, dice_roll, monster)

                    if '-' in monster_list[0]:
                        lo = int(number_range[0])
                        hi = int(number_range[1]) 
                        #print(hi, lo)
                        for i in range(lo,hi+1,1):
                            #print(lo,hi,i)
                            #print(i)
                            dragon_levels[ld+1][i]['name'] = monster
                            #dragon_levels[ld+1][i]['roll'] = dice_lookup[dice_roll]
                            dragon_levels[ld+1][i]['roll'] = '1-1'
                            if '2' in monster:
                                dragon_levels[ld+1][i]['roll'] = '2-2'
                    else:
                        dragon_levels[ld+1][int(number_range[0])]['name'] = monster
                        #dragon_levels[ld+1][int(number_range[0])]['roll'] = dice_lookup[dice_roll]
                        dragon_levels[ld+1][int(number_range[0])]['roll'] = '1-1'
                        if '2' in monster:
                            dragon_levels[ld+1][i]['roll'] = '2-2'

            dcheck = dragon_levels[level][m]
            mdict['details'] = dcheck
            mdict['name'] = 'Dragon-' + dcheck['name']
            mdict['no'] = dcheck['roll']
            #mdict['XP'] = dragon_xp[level]  NOT IMPLEMENTED YET


def monster_subtables_wet(m_dict, wet_dict)

    if 'HumanSubtable' in m_dict['name']:
        wet_dict['monster_details']['type'] = m_dict['details'][0]
        wet_dict['monster_details']['No'] = m_dict['details'][1]

        if 'Character' in m_dict['details']:
            wet_dict['monster_details']['type']  = m_dict['details']
            wet_dict['monster_details']['No'] = 9
            wet_dict['monster_details']['lair'] = '0%'
            wet_dict['monster_details']['treasure_individual'] = []
            wet_dict['monster_details']['treasure_lair'] = []
        else:
            m_data = human_d['human-' + m_dict['details'][0].lower()]                
            wet_dict['monster_details']['XP'] = m_data['XPtotal']
            wet_dict['monster_details']['lair'] = m_data['lair']
            wet_dict['monster_details']['treasure_individual'] = m_data['treasure_individual']
            wet_dict['monster_details']['treasure_lair'] = m_data['treasure_lair']

    elif 'CharacterSubtable' in m_dict['name']:
        wet_dict['monster_details']['type']  = m_dict['details']
        wet_dict['monster_details']['No'] = 9
        wet_dict['monster_details']['lair'] = '0%'
        wet_dict['monster_details']['treasure_individual'] = []
        wet_dict['monster_details']['treasure_lair'] = []

    #elif 'DragonSubtable' in m_dict['name']:
    elif 'Dragon' in m_dict['name']:            
        wet_dict['monster_details']['type']  = m_dict['details']['name']
        wet_dict['monster_details']['No'] = int(m_dict['no'][0])

        dname = m_dict['name'].split(':')[0]
        
        m_data = dragon_d[dname.replace('Dragon-','')]
        if VERBOSITY:
            print("Dragon dname", dname)
            print("Dragon M Data", m_data)
        wet_dict['monster_details']['lair'] = m_data['lair']
        wet_dict['monster_details']['treasure_individual'] = m_data['treasure_individual']
        wet_dict['monster_details']['treasure_lair'] = m_data['treasure_lair']
        wet_dict['monster_details']['XP'] = xp_d[wet_dict['monster_details']['level']]

    else:
        ##monsters
        if 'NO-ENCOUNTER' not in wet_dict['monster_details']['type']:
            m_data = all_d[wet_dict['monster_details']['type'].lower()]
            if VERBOSITY:
                print(m_data)
            wet_dict['monster_details']['XP'] = m_data['XPtotal']
            wet_dict['monster_details']['lair'] = m_data['lair']
            wet_dict['monster_details']['treasure_individual'] = m_data['treasure_individual']
            wet_dict['monster_details']['treasure_lair'] = m_data['treasure_lair']
        else: #dummy, nothing of interest
            wet_dict['monster_details']['lair'] = '0%'
            wet_dict['monster_details']['treasure_individual'] = []
            wet_dict['monster_details']['treasure_lair'] = []

    if VERBOSITY:
        print("CHECKSD FOR MONSTER CHARACTERS AFTER:",wet_dict['monster_details']['level'])
        print("CHECKSD FOR MONSTER CHARACTERS AFTER:",wet_dict['monster_details']['type'])

    return wet_dict

        
    if v:
        print("MONSTER TABLE MDICT:",mdict)

    if 1 == 2:
        print("DUMPING LEVELS")
        with open('levels.json','w') as f:
            json.dump(levels, f)
        return mdict

    if 1 == 2:
        with open('dragons.json','w') as f:
            json.dump(dragon_levels, f)

    return mdict

if __name__ == "__main__":
    ARGV = sys.argv
    #print("lenARGV",len(ARGV))
    if len(ARGV) > 1:
        monster_level = level_matrix(int(ARGV[1]))
    else:
        monster_level = level_matrix(3)
    print("MONSTER LEVEL:",monster_level)

    print(monster_tables(monster_level))

    #print(human_dict)
    #print(dragon_dict)
    #print(all_dict)