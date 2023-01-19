

def select_character_type():
    roll_dice = random.randint(1, 100)
    if roll_dice <= 17:
        return "CLERIC", 3
    elif roll_dice <= 20:
        return "DRUID", 2
    elif roll_dice <= 60:
        return "FIGHTER", 5
    elif roll_dice <= 62:
        return "PALADIN", 2
    elif roll_dice <= 65:
        return "RANGER", 2
    elif roll_dice <= 86:
        return "MAGIC-USER", 3
    elif roll_dice <= 88:
        return "ILLUSIONIST", 1
    elif roll_dice <= 98:
        return "THIEF", 4
    elif roll_dice <= 99:
        return "ASSASSIN", 2
    else:
        roll = random.randint(0,1)
        if roll == 0:
            return "MONK", 1
        else:
            return "BARD", 1

def magic_item_chance(level):
    pass

if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        character_level = ARGV[1]
    else:
        character_level = 1

    print("CHARACTER LEVEL:",monster_level)

    #print(monster_tables(monster_level))
