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


def periodic_check:
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
    