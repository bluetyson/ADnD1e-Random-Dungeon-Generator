import random
import sys

def testtreasure():
    return "Basic treasure goes in shape_dict for room! Not done random gems, jewellery, magic."

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

def select_gemstone():
    dice_roll = roll_dice(1, 100)
    print(dice_roll)
    if dice_roll <= 25:
        return 10, "Ornamental Stones"
    elif dice_roll <= 50:
        return 50, "Semi-precious Stones"
    elif dice_roll <= 70:
        return 100, "Fancy Stones"
    elif dice_roll <= 90:
        return 500, "Fancy Stones (Precious)"
    elif dice_roll <= 99:
        return 1000, "Gem Stones"
    else:
        return 5000, "Gem Stones (Jewels)"

def update_gemstone(base_value):
    dice_roll = roll_dice(1, 10)
    print(dice_roll)
    if dice_roll == 1:
        next_base_value = base_value * 2
        if next_base_value > 1000000:
            return 1000000
        return next_base_value
    elif dice_roll == 2:
        return base_value * 2
    elif dice_roll == 3:
        percent_increase = roll_dice(1, 6) * 10
        return base_value + (base_value * percent_increase) / 100
    elif dice_roll == 4 or dice_roll == 5 or dice_roll == 6 or dice_roll == 7 or dice_roll == 8:
        return base_value
    elif dice_roll == 9:
        percent_decrease = roll_dice(1, 4) * 10
        return base_value - (base_value * percent_decrease) / 100
    else:
        next_base_value = base_value / 2
        if next_base_value < 5:
            return 5
        return next_base_value

def select_jewellery():
    dice_roll = roll_dice(1, 100)
    if dice_roll <= 10:
        base_value = roll_dice(1, 10) * 100
        description = "Ivory or wrought silver"
    elif dice_roll <= 20:
        base_value = (roll_dice(1, 6) + roll_dice(1, 6)) * 100
        description = "Wrought silver and gold"
    elif dice_roll <= 40:
        base_value = (roll_dice(1, 6) + roll_dice(1, 6)+ roll_dice(1, 6)) * 100
        description = "Wrought gold"
    elif dice_roll <= 50:
        base_value = (roll_dice(1, 6) + roll_dice(1, 6)+ roll_dice(1, 6)+ roll_dice(1, 6)+ roll_dice(1, 6)) * 100
        description = "Jade, coral or wrought platinum"
    elif dice_roll <= 70:
        base_value = roll_dice(1, 10) * 1000
        description = "Silver with gems"
    elif dice_roll <= 90:
        base_value = roll_dice(1, 4) * 1000 + roll_dice(1, 4) * 1000
        description = "Gold with gems"
    else:
        base_value = (roll_dice(1, 6) + roll_dice(1, 6)) * 1000
        description = "Platinum with gems"
    # Check for exceptional value
    w = roll_dice(1,10)
    v = roll_dice(1,10)
    if w == 1:
        base_value = min(base_value * 2, 120000)
        description = "Exceptional Workmanship " + description
    if v == 1:
        base_value = min(base_value * 2, 120000)
        description = "Exceptional Design " + description
    # Check for exceptional gems
    if "gems" in description:
        e = roll_dice(1,8)
        if e == 1:
            gem_bonus = 5000
            ec = roll_dice(1,6)
            while ec == 1:
                if ec == 1:
                    gem_bonus *= 2
                    gem_bonus = min(gem_bonus, 640000)
                base_value += gem_bonus
                ec = roll_dice(1,6)

    return base_value, description

def potion_choice():
    potion_table = [
            ('Animal Control', 250, 400), 
            ('Clairaudience', 250, 400), 
            ('Clairvoyance', 300, 500), 
            ('Climbing', 300, 500),
            ('Delusion', 0, 150), 
            ('Diminution', 300, 500), 
            ('Dragon Control', 500, 9000), ('ESP', 500, 850),
            ('Extra-Healing', 400, 800), 
            ('Fire Resistance', 250, 400), 
            ('Flying', 500, 750), 
            ('Gaseous Form', 300, 400),
            ('Giant Control', 400, 9000), 
            ('Giant Strength', 500, 1400), 
            ('Growth', 250, 300), 
            ('Healing', 200, 400),
            ('Heroism', 300, 500), 
            ('Human Control', 500, 900), 
            ('Invisibility', 250, 500), 
            ('Invulnerability', 350, 500),
            ('Levitation', 250, 400), 
            ('Longevity', 500, 1000), 
            ('Oil of Etherealness', 600, 1500),
            ('Oil of Slipperiness', 400, 750), 
            ('Philter of Love', 200, 300), 
            ('Philter of Persuasiveness', 400, 850),
            ('Plant Control', 250, 300), 
            ('Polymorph (self)', 200, 350), 
            ('Poison', 0, 0), 
            ('Speed', 200, 450),
            ('Super-Heroism', 450, 750), 
            ('Sweet Water', 200, 250), 
            ('Treasure Finding', 600, 2000),
            ('Undead Control', 700, 2500), 
            ('Water Breathing', 400, 900)
        ]
        
    potion = random.choice(potion_table)
    return potion

def random_potion2():
    roll = random.randint(1, 100)
    if roll <= 3:
        return (250, 400, "Animal Control")
    elif roll <= 6:
        return (250, 400, "Clairaudience")
    elif roll <= 9:
        return (300, 500, "Clairvoyance")
    # continue adding elif statements for the rest of the items in the table
    else:
        return (0, 0, "Invalid Roll")

def scroll_choice():
    s = roll_dice(1,100)
    st = 1
    if s <=70:
        sc = "MAGIC-USER"
        mu = roll_dice(1,100)
        if mu >= 91:
            sc = "ILLUSIONIST"
    else:
        st = 2
        sc = "CLERIC"
        mu = roll_dice(1,100)
        if mu >= 76:
            sc = "DRUID"

    roll = roll_dice(1,100)
    if roll <= 10:
        return 1, random.randint(1,4), -1, sc
    elif roll <= 16:
        return 1, random.randint(1,6), -1, sc
    elif roll <= 19:
        return 1, random.randint(2,9) if st==1 else random.randint(2,7), -1, sc
    elif roll <= 24:
        return 2, random.randint(1,4), -1, sc
    elif roll <= 27:
        return 2, random.randint(1,8) if st==1 else random.randint(1,6), -1, sc
    elif roll <= 32:
        return 3, random.randint(1,4), -1, sc
    elif roll <= 35:
        return 3, random.randint(2,9) if st==1 else random.randint(2,7), -1, sc
    elif roll <= 39:
        return 4, random.randint(1,6), -1, sc
    elif roll <= 42:
        return 4, random.randint(1,8) if st==1 else random.randint(1,6), -1, sc
    elif roll <= 46:
        return 5, random.randint(1,6), -1, sc
    elif roll <= 49:
        return 5, random.randint(1,8) if st==1 else random.randint(1,6), -1, sc
    elif roll <= 52:
        return 6, random.randint(1,6), -1, sc
    elif roll <= 54:
        return 6, random.randint(3,8) if st==1 else random.randint(3,6), -1, sc
    elif roll <= 57:
        return 7, random.randint(1,8), -1, sc
    elif roll <= 59:
        return 7, random.randint(2,9), -1, sc
    elif roll <= 60:
        return 7, random.randint(4,0) if st==1 else random.randint(4,7), -1, sc
    elif roll <= 62:        
        return 1, 'Protection - Demons', 2500, sc
    elif roll <= 64:        
        return 1, 'Protection - Devils', 2500, sc
    elif roll <= 70:        
        return 1, 'Protection - Elementals', 1500, sc
    elif roll <= 76:        
        return 1, 'Protection - Lycanthropes', 1000, sc
    elif roll <= 82:        
        return 1, 'Protection - Magic', 2500, sc
    elif roll <= 87:        
        return 1, 'Protection - Petrification', 2000, sc
    elif roll <= 92:        
        return 1, 'Protection - Possession', 2000, sc
    elif roll <= 97:        
        return 1, 'Protection - Undead', 1500, sc
    elif roll <= 100:        
        return 1, 'Curse', 0, sc

def ring_choice():
    dice_roll = roll_dice(1, 100)
    if dice_roll <= 6:
        return ("Contrariness", 0, 1000)
    elif dice_roll <= 12:
        return ("Delusion", 0, 2000)
    elif dice_roll <= 14:
        return ("Djinni Summoning", 3000, 20000)
    elif dice_roll <= 15:
        return ("Elemental Command", 5000, 25000)
    elif dice_roll <= 21:
        return ("Feather Falling", 1000, 5000)
    elif dice_roll <= 27:
        return ("Fire Resistance", 1000, 5000)
    elif dice_roll <= 30:
        return ("Free Action", 1000, 5000)
    elif dice_roll <= 33:
        return ("Human Influence", 2000, 10000)
    elif dice_roll <= 40:
        return ("Invisibility", 1500, 7500)
    elif dice_roll <= 43:
        return ("Mammal Control", 1000, 5000)
    elif dice_roll <= 44:
        return ("Multiple Wishes", 5000, 25000)
    elif dice_roll <= 60:
        dice_roll_2 = random.randint(1, 20)
        if dice_roll_2 <= 10:
            return ("Protection", 2000, 10000)
        elif dice_roll_2 <= 20:
            return ("Protection", 2500, 12500)
        elif dice_roll_2 <= 30:
            return ("Protection", 3000, 15000)
        else:
            return ("Protection", 4000, 20000)
    elif dice_roll <= 63:
        return ("Regeneration", 5000, 40000)
    elif dice_roll <= 65:
        return ("Shooting Stars", 3000, 15000)
    elif dice_roll <= 69:
        return ("Spell Storing", 2500, 22500)
    elif dice_roll <= 75:
        return ("Spell Turning", 2000, 17500)
    elif dice_roll <= 77:
        return ("Swimming", 1000, 5000)
    elif dice_roll <= 79:
        return ("Telekinesis", 2000, 10000)
    elif dice_roll <= 85:
        return ("Three Wishes", 3000, 15000)
    elif dice_roll <= 90:
        return ("Warmth", 1000, 5000)
    elif dice_roll <= 98:
        return ("Water Walking", 1000, 5000)
    elif dice_roll <= 99:
        return ("Weakness", 0, 1000)
    else:
        return ("Wizardry", 4000, 50000)

# Example usage
def select_magic_item():
    roll = roll_dice(1, 100)
    choice = ""
    if roll <= 20:
        item = "Potions (A.)"
        choice = potions_choice()
    elif roll <= 35:
        item = "Scrolls (B.)"
        choice = scroll_choice()
    elif roll <= 40:
        item = "Rings (C.)"
        choice = ring_choice()
    elif roll <= 45:
        item = "Rods, Staves & Wands (D.)"
    elif roll <= 48:
        item = "Miscellaneous Magic (E.1.)"
    elif roll <= 51:
        item = "Miscellaneous Magic (E.2.)"
    elif roll <= 54:
        item = "Miscellaneous Magic (E.3.)"
    elif roll <= 57:
        item = "Miscellaneous Magic (E.4.)"
    elif roll <= 60:
        item = "Miscellaneous Magic (E.5.)"
    elif roll <= 75:
        item = "Armor & Shields (F.)"
    elif roll <= 86:
        item = "Swords (G.)"
    else:
        item = "Miscellaneous Weapons (H.)"
    return item, choice

if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        character_level = ARGV[1]
    else:
        character_level = 1

    print(select_gemstone())
    base_value, description = select_gemstone()
    print(f"The selected gemstone has a base value of {base_value} gold pieces and is described as {description}")

    new_base_value = update_gemstone(base_value)
    print(f"The upgrade value of the gemstone is {new_base_value} gold pieces.")

    base_value, description = select_jewellery()
    print(f"The selected jewelry has a base value of {base_value} gold pieces and is described as {description}")

    exp_val, gold_val, potion_name = random_potion()
    print(f"Experience Value: {exp_val}, Gold Piece Sale Value: {gold_val}, Potion: {potion_name}")

    no, range, xp, class_use = scroll_choice()
    if xp == -1:
        xp = 100 * no * range
    print(f"Spells:{no}, Level:{range}, XP:{xp}, Class:{class_use}")

    no, xp, val = ring_choice()
    print(f"Rings:{no}, XP:{xp}, Gold:{val}")

    item, choice = select_magic_item()
    print(f"Magic:{item}, Choice:{choice})
