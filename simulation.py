
import sys
from dungeon_simulation import dungeon_sim

if __name__ == "__main__":
    ARGV = sys.argv
    PERIODIC_CHECKS = 1
    VERBOSITY = 0

    if len(ARGV) > 1:
        if int(ARGV[1]) > 1:
            PERIODIC_CHECKS = int(ARGV[1])

    if len(ARGV) > 2:
        VERBOSITY = int(ARGV[2])

    print(PERIODIC_CHECKS, VERBOSITY)
    df = dungeon_sim(PERIODIC_CHECKS, VERBOSITY)

    print(df)
    



