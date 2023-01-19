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

#dummy tables until get proper ones in
table_I = ["Ring of Protection", "Amulet of Health", "Staff of Power", "Boots of Speed", "Cloak of Invisibility", "Sword of Sharpness"]
table_II = ["Ring of Invisibility", "Amulet of Life Preservation", "Staff of Striking", "Boots of Levitation", "Cloak of Displacement", "Sword of Dancing"]
table_III = ["Ring of Spell Turning", "Amulet of the Planes", "Staff of the Magi", "Boots of Teleportation", "Cloak of the Bat", "Sword of Sharpness +3"]
table_IV = ["Ring of Regeneration", "Amulet of Proof against Detection and Location", "Staff of the Woodlands", "Boots of Speed +5", "Cloak of Arachnida", "Sword of Life Stealing"]

magic_tables = {}

def magic_item_chance(level):
    magic_items = []

    m1 = roll_dice(1,100)
    m2 = roll_dice(1,100)
    m3 = roll_dice(1,100)
    m4 = roll_dice(1,100)

    level = int(level)

    if level == 1:
        if m1 <= 10:
            magic_items.extend(random.choices(table_I, k=1))
        print("magic 1:", magic_items)
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

def create_party(level):
    classes =["CLERIC","DRUID","FIGHTER","PALADIN","RANGER","MAGIC-USER", "ILLUSIONIST", "THIEF","ASSASSIN","MONK","BARD"]
    party = {}  
    for cl in classes:
        party[cl] = 0  

    characters = roll_dice(1,4) + 1

    henchmen = 9 - characters

    party_members = {}

    for c in range(characters):
        character_class = select_character_type()
        #print(character_class, type(character_class[0]), type(character_class[1]))

        while(party[character_class[0]] + 1 > character_class[1]):
            character_class = select_character_type()

        party[character_class[0]] += 1
        magic_items = []
        magic_items = magic_item_chance(level)

        #print("CHARACTER LEVEL:",level)
        #print("CHARACTER CLASS:",character_class)
        #print("MAGIC ITEMS:", magic_items)

        party_members[c+1] = {}
        party_members[c+1]['class'] = character_class[0]
        party_members[c+1]['level'] = level
        party_members[c+1]['magic_items'] = magic_items
        #print(characters, "Character Party:")

    for h in range(henchmen):
        party_members[c+1+h+1] = {}
        party_members[c+1+h+1]['class'] = 'man-at-arms/hench'

    for key in party_members:            
        print(key, ":", party_members[key])

    return party_members

def select_human(level):
    h = roll_dice(1,100)
    if h <= 25:
        return ["Bandit", roll_dice(2,6) + 3]
    if h >= 26 and h <= 30:
        return ["Berserker", roll_dice(2,4) + 1]
    if h >= 31 and h <= 45:
        return ["Brigand", roll_dice(2,6) + 3]
    else:
        return ["Character", create_party(level)]

if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        character_level = ARGV[1]
    else:
        character_level = 1

    party_members = create_party(character_level)

