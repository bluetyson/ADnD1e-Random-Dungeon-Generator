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

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

#pass location?
def periodic_check:
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
        pc_dict['check'] = 3
    elif pc == 18:
        pc_dict['direction'] = 'stop'
        pc_dict['check'] = 3
    elif pc == 19:
        pc_dict['direction'] = 'bad_things'
        pc_dict['check'] = 3
    elif pc == 20:
        pc_dict['direction'] = 'random_encounter'
        pc_dict['check'] = 3


    ```
    Die Result
    1-2 Continue straight — check again in 60’ (this table)
    3-5 Door (see TABLE II.)
    6-10 Side Passage (see TABLE III.) — check again in 30’ (this table)
    11-13 Passage Turns (see TABLE IV., check width on TABLE III.) — check
    again in 30’ (this table)
    14-16 Chamber (see TABLE V.) — check 30’ after leaving (this table)
    17 Stairs (see TABLE VI.)
    18 Dead End (walls left, right, and ahead can be checked for Secret
    Doors, see TABLE V.D., footnote)
    19 Trick/Trap (see TABLE VII.), passage continues — check again in 30’
    (this table)
    20 Wandering Monster, check again immediately to see what lies ahead
    so direction of monster’s approach can be determined.
    ```
    