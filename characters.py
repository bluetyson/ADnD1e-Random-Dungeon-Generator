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
table_I = table_I = [
    ["2 POTIONS: climbing, flying"],
    ["2 POTIONS: extra-healing, polymorph (self)"],
    ["2 POTIONS: fire resistance, speed"],
    ["2 POTIONS: healing, giant strength"],
    ["2 POTIONS: heroism, invulnerability"],
    ["2 POTIONS: human control, levitation"],
    ["2 POTIONS: super-heroism, animal control"],
    ["1 SCROLL: 1 Spell, level 1-6"],
    ["1 SCROLL: 2 Spells, level 1-4"],
    ["1 SCROLL: protection from magic"],
    ["1 RING: mammal control"],
    ["1 RING: protection +1"],
    ["1 ARMOR: leather +1"],
    ["1 SHIELD: +1"],
    ["1 SWORD: +1 (no special abilities)"],
    ["10 ARROWS: +1"],
    ["4 BOLTS: +2"],
    ["1 DAGGER: +1 (or +2) et al."],
    ["1 JAVELIN +2"],
    ["1 MACE +1"]
]
table_II = [
    ["1 SCROLL: 3 Spells, level 2-9 or 2-7"],
    ["2 RINGS: fire resistance, invisibility"],
    ["1 RING: protection +3"],
    ["1 STAFF: striking"],
    ["1 WAND: illusion"],
    ["1 WAND: negation"],
    ["1 bracers of defense, armor class 4"],
    ["1 brooch of shielding"],
    ["1 cloak of elvenkind"],
    ["1 dust of appearance"],
    ["1 FIGURINE OF WONDROUS POWER: serpentine owl"],
    ["3 javelins of lightning"],
    ["1 set: chainmail +1, shield +2"],
    ["1 ARMOR: splint mail +4"],
    ["1 SWORD: +3 (no special abilities)"],
    ["2 WEAPONS: crossbow of speed, hammer +2"]
]
table_III = [
    ["1 RING: spell storing"],
    ["1 ROD: cancellation"],
    ["1 STAFF: serpent - python or adder"],
    ["1 bag of tricks"],
    ["1 boots of speed"],
    ["1 boots of striding and leaping"],
    ["1 cloak of displacement"],
    ["1 gauntlets of ogre power"],
    ["1 pipe of the sewers"],
    ["1 robe of blending"],
    ["2 ROPES: climbing, entanglement"],
    ["1 set: plate mail +3, shield +2"],
    ["1 SHIELD: +5"],
    ["1 SWORD: +4, defender"],
    ["1 mace +3"],
    ["1 spear +3"]
]
table_IV = [
    ["1 RING: djinni summoning"],
    ["1 RING: spell turning"],
    ["1 ROD: smiting"],
    ["1 WAND: fire"],
    ["1 cube of force"],
    ["1 eyes of charming"],
    ["1 horn of valhalla"],
    ["1 robe of scintillating colors"],
    ["1 talisman of either ultimate evil or pure good"],
    ["1 set: plate mail +4, shield +3"],
    ["1 SWORD: wounding"],
    ["1 arrow of slaying (select character type)"]
]

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

def get_race_and_class(dice_score):
    if dice_score >= 1 and dice_score <= 25:
        race = "Dwarf"
        multi_class_percentage = 15
    elif dice_score >= 26 and dice_score <= 50:
        race = "Elf"
        multi_class_percentage = 85
    elif dice_score >= 51 and dice_score <= 60:
        race = "Gnome"
        multi_class_percentage = 25
    elif dice_score >= 61 and dice_score <= 85:
        race = "Half-elf"
        multi_class_percentage = 85
    elif dice_score >= 86 and dice_score <= 95:
        race = "Halfling"
        multi_class_percentage = 10
    else:
        race = "Half-Orc"
        multi_class_percentage = 50
    return (race, multi_class_percentage)


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
        party_members[c+1]['race'] = 'Human'
        party_members[c+1]['multi'] = 'N'
        #print(characters, "Character Party:")

        non_human = roll_dice(1,100)
        if non_human <= 20:
            dice_score = random.randint(1,100)
            race, multi_class_percentage = get_race_and_class(dice_score)        
            party_members[c+1]['race'] = race

            multi = roll_dice(1,100)
            if multi <= multi_class_percentage:
                party_members[c+1]['multi'] = 'Y'
                party_members[c+1]['multi_no'] = 2
                #check 2 or 3
                multino = 2
                multi_classes = roll_dice(1,3)
                if multi_classes == 3:
                    multino = 3
                    party_members[c+1]['multi_no'] = 3

        party_members[c+1]['magic_items'] = magic_items

    for h in range(henchmen):
        party_members[c+1+h+1] = {}
        s = roll_dice(1,2)
        if s == 1:
            if level <= 3:
                party_members[c+1+h+1]['class'] = 'man-at-arms/henchman'
            else:
                party_members[c+1+h+1]['class'] = 'henchman' #need to roll as per character details
        else:
            if level <= 3:
                party_members[c+1+h+1]['class'] = 'woman-at-arms'
            else:
                party_members[c+1+h+1]['class'] = 'henchwoman' #need to roll as per character details


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

