import sys
import random

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

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

table_I = ["Ring of Protection", "Amulet of Health", "Staff of Power", "Boots of Speed", "Cloak of Invisibility", "Sword of Sharpness"]
table_II = ["Ring of Invisibility", "Amulet of Life Preservation", "Staff of Striking", "Boots of Levitation", "Cloak of Displacement", "Sword of Dancing"]
table_III = ["Ring of Spell Turning", "Amulet of the Planes", "Staff of the Magi", "Boots of Teleportation", "Cloak of the Bat", "Sword of Sharpness +3"]
table_IV = ["Ring of Regeneration", "Amulet of Proof against Detection and Location", "Staff of the Woodlands", "Boots of Speed +5", "Cloak of Arachnida", "Sword of Life Stealing"]

magic_tables = {}

def magic_item_chance(level):
    magic_items = []
    # Use if-elif statements to determine the chance of getting magic items
    # from each table based on the level
    m1 = roll_dice(1,100)
    m2 = roll_dice(1,100)
    m3 = roll_dice(1,100)
    m4 = roll_dice(1,100)

    if level == 1:
        if m1 <= 10:
            magic_items.extend(random.choices(table_I, k=1))
    elif level == 2:
        if m1 <= 20:
            magic_items.extend(random.choices(table_I, k=1))
    elif level == 3:
        if m1 <= 30:
            magic_items.extend(random.choices(table_I, k=2))
        if m2 <= 10:
            magic_items.extend(random.choices(table_II, k=1))
    elif level == 4:
        if m1 <= 40:
            magic_items.extend(random.choices(table_I, k=2))
        if m2 <= 20:
            magic_items.extend(random.choices(table_II, k=1))
    elif level == 5:
        if m1 <= 50:
            magic_items.extend(random.choices(table_I, k=2))
        if m2 <= 30:
            magic_items.extend(random.choices(table_II, k=1))
    elif level == 6:
        if m1 <= 60:
            magic_items.extend(random.choices(table_I, k=3))
        if m2 <= 40:
            magic_items.extend(random.choices(table_II, k=2))
    elif level == 7:
        if m1 <= 70:
            magic_items.extend(random.choices(table_I, k=3))
        if m2 <= 50:
            magic_items.extend(random.choices(table_II, k=2))
        if m3 <= 10:
            magic_items.extend(random.choices(table_III, k=1))
    elif level == 8:
        if m1 <= 80:
            magic_items.extend(random.choices(table_I, k=3))
        if m2 <= 60:
            magic_items.extend(random.choices(table_II, k=2))
        if m3 <= 20:
            magic_items.extend(random.choices(table_III, k=1))
    elif level == 9:
        if m1 <= 90:
            magic_items.extend(random.choices(table_I, k=3))
        if m2 <= 70:
            magic_items.extend(random.choices(table_II, k=2))
        if m3 <= 30:
            magic_items.extend(random.choices(table_III, k=1))
    elif level == 10:
        magic_items.extend(random.choices(table_I, k=3))
        if m2 <= 80:
            magic_items.extend(random.choices(table_II, k=2))
        if m3 <= 40:
            magic_items.extend(random.choices(table_III, k=1))
    elif level == 11:
        magic_items.extend(random.choices(table_I, k=3))
        if m2 <= 90:
            magic_items.extend(random.choices(table_II, k=2))
        if m3 <= 50:
            magic_items.extend(random.choices(table_III, k=1))
        if m3 <= 10:
            magic_items.extend(random.choices(table_IV, k=1))
    else:
        magic_items.extend(random.choices(table_I, k=3))
        magic_items.extend(random.choices(table_II, k=2))
        if m3 <= 60:
            magic_items.extend(random.choices(table_III, k=1))
        if m3 <= 20:
            magic_items.extend(random.choices(table_IV, k=1))

        return magic_items

if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        character_level = ARGV[1]
    else:
        character_level = 1

    classes =["CLERIC","DRUID","FIGHTER","PALADIN","RANGER","MAGIC-USER", "ILLUSIONIST", "THIEF","ASSASSIN","MONK","BARD"]
    party = {}  
    for cl in classes:
        party[cl] = {}  
    
    characters = roll_dice(1,4) + 1
    for c in range(characters):
        character_class = select_character_type()
        print(character_class, type(character_class[0]))
        while(party[character_class[0]] + 1 > character_class[1]):
            character_class = select_character_type()

        party[character_class[0]] += 1

        magic_items = magic_item_chance(character_level)

        print("CHARACTER LEVEL:",character_level)
        print("CHARACTER CLASS:",character_class)
        print("MAGIC ITEMS:", magic_items)


    print(party)
        #print(monster_tables(monster_level))
