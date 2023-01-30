
#Version 1.2.1, 20220131

import sys
from dungeon_simulation import dungeon_sim

if __name__ == "__main__":
    #make 3rd one, number of sims!
    #then do multiprocessing

    suffix = ''
    usepath = ''

    ARGV = sys.argv
    PERIODIC_CHECKS = 1
    VERBOSITY = 0
    ROOMS_CHECK = 0
    LEVELS_CHECK = 0

    if len(ARGV) > 1:
        if int(ARGV[1]) > 1:
            PERIODIC_CHECKS = int(ARGV[1])

    if len(ARGV) > 2:
        VERBOSITY = int(ARGV[2])

    if len(ARGV) > 3:
        ROOMS_CHECK = int(ARGV[3])

    if len(ARGV) > 3:
        LEVELS_CHECK = int(ARGV[4])

    print(suffix, usepath, PERIODIC_CHECKS, VERBOSITY)
    df = dungeon_sim(suffix, usepath, PERIODIC_CHECKS, VERBOSITY, ROOMS_CHECK, LEVELS_CHECK)

    #print(df)
    



