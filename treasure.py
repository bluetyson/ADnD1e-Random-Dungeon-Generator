import random
import sys

'''verbosity v
'''
v = 0

def testtreasure():
    return "Basic treasure goes in shape_dict for room! Not done random gems, jewellery, magic."

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

def select_gemstone():
    dice_roll = roll_dice(1, 100)
    if v:
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
    if v:
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
        base_value = roll_dice(1, 6) + roll_dice(1, 6)
        base_value = base_value * 100
        description = "Wrought silver and gold"
    elif dice_roll <= 40:
        base_value = roll_dice(1, 6) + roll_dice(1, 6)+ roll_dice(1, 6)
        base_value = base_value * 100
        description = "Wrought gold"
    elif dice_roll <= 50:
        base_value = roll_dice(1, 6) + roll_dice(1, 6)+ roll_dice(1, 6)+ roll_dice(1, 6)+ roll_dice(1, 6)
        base_value = base_value * 100
        description = "Jade, coral or wrought platinum"
    elif dice_roll <= 70:
        base_value = roll_dice(1, 10) * 1000
        description = "Silver with gems"
    elif dice_roll <= 90:
        base_value = roll_dice(1, 4) * 1000 + roll_dice(1, 4) * 1000
        description = "Gold with gems"
    else:
        base_value = roll_dice(1, 6) + roll_dice(1, 6)
        base_value = base_value * 1000
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

def jewellery_type():
    i = roll_dice(1,100)
    items = {
        2: "anklet",
        6: "arm band",
        9: "belt",
        12: "box small",
        16: "bracelet",
        19: "brooch",
        21: "buckle",
        25: "chain",
        26: "chalice",
        27: "choker",
        30: "clasp",
        32: "coffer",
        33: "collar",
        35: "comb",
        36: "coronet",
        37: "crown",
        39: "decanter",
        40: "diadem",
        45: "earring",
        47: "fob",
        52: "goblet",
        54: "headband fillet",
        57: "idol",
        59: "locket",
        62: "medal",
        68: "medallion",
        75: "necklace",
        78: "pendant",
        83: "pin",
        84: "orb",
        93: "ring",
        94: "sceptre",
        96: "seal",
        99: "statuette",
        100: "tiara"
    }    
    for key in items:
        if i <= key:
            return items[key]

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

def potion_choice():
    roll = roll_dice(1,100)
    if roll <= 3:
        return ("Animal Control*", 250, 400)
    elif roll <= 6:
        return ("Clairaudience", 250, 400)
    elif roll <= 9:
        return ("Clairvoyance", 300, 500)
    elif roll <= 12:
        return ("Climbing", 300, 500)
    elif roll <= 15:
        return ("Delusion**", 0, 150)
    elif roll <= 18:
        return ("Diminution", 300, 500)
    elif roll <= 20:
        return ("Dragon Control*", 5000, 9000) #random this
    elif roll <= 23:
        return ("ESP", 500, 850)
    elif roll <= 26:
        return ("Extra-Healing", 400, 800)
    elif roll <= 29:
        return ("Fire Resistance", 250, 400)    
    elif roll <= 32:
        return ('Flying', 500, 750)
    elif roll <= 34:
        return ('Gaseous Form', 300, 400)
    elif roll <= 36:
        g = roll_dice(1,6)
        return ('Giant Control', 300 +g*100, g*1000)
    elif roll <= 39:
        g = roll_dice(1,6)
        return ('Giant Strength', 450 +g*50, 800+g*100)
    elif roll <= 41:
        return ('Growth', 250, 300)
    elif roll <= 47:
        return ('Healing', 200, 400)
    elif roll <= 49:
        return ('Heroism', 300, 500)
    elif roll <= 51:
        return ('Human Control', 500, 900)
    elif roll <= 54:
        return ('Invisibility', 250, 500)
    elif roll <= 57:
        return ('Invulnerability', 350, 500)
    elif roll <= 60:
        return ('Levitation', 250, 400)
    elif roll <= 63:
        return ('Longevity', 500, 1000)
    elif roll <= 66:
        return ('Oil of Etherealness', 600, 1500)
    elif roll <= 69:
        return ('Oil of Slipperiness', 400, 750)
    elif roll <= 72:
        return ('Philter of Love', 200, 300)
    elif roll <= 75:
        return ('Philter of Persuasiveness', 400, 850)
    elif roll <= 78:
        return ('Plant Control', 250, 300)
    elif roll <= 81:
        return ('Polymorph (self)', 200, 350)
    elif roll <= 84:
        return ('Poison', 0, 0)
    elif roll <= 87:
        return ('Speed', 200, 450)
    elif roll <= 90:
        return ('Super-Heroism', 450, 750)
    elif roll <= 93:
        return ('Sweet Water', 200, 250)
    elif roll <= 96:
        return ('Treasure Finding', 600, 2000)
    elif roll <= 97:
        return ('Undead Control*', 700, 2500)
    else: #Water Breathing
        return ('Water Breathing', 400, 900)

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
        cl = roll_dice(1,100)
        if cl >= 76:
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
        return 7, random.randint(2,9) if st==1 else random.randint(2,7), -1, sc
    elif roll <= 60:
        return 7, random.randint(4,9) if st==1 else random.randint(4,7), -1, sc
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

def cleric_choice(level):
    first_level = ["Bless", "Command", "Create Water", "Cure Light Wounds", "Detect Evil", "Detect Magic", "Light", "Protection From Evil", "Purify Food & Drink", "Remove Fear", "Resist Cold", "Sanctuary"]
    second_level = ["Augury", "Chant", "Detect Charm", "Find Traps", "Hold Person", "Know Alignment", "Resist Fire", "Silence 15 Radius", "Slow Poison","Snake Charm","Speak With Animals","Spiritual Hammer"]
    third_level = ["Animate Dead", "Continual Light","Create Food & Water", "Cure Blindness", "Cure Disease", "Dispel Magic", "Feign Death","Glyph Of Warding", "Locate Object", "Prayer", "Remove Curse",  "Speak With Dead"]
    fourth_level = ["Cure Serious Wounds", "Detect Lie", "Cure Critical Wounds","Divination","Exorcise","Lower Water","Neutralize Poison","Protection from Evil 10 Radius","Speak With Plants","Sticks To Snakes","Tongues"]
    fifth_level = ["Atonement", "Commune", "Cure Critical Wounds","Dispel Evil", "Earthquake", "Flame Strike", "Insect Plague", "Plane Shift", "Quest", "Raise Dead","True Seeing"]
    sixth_level = ["Aerial Servant", "Animate Object",  "Blade Barrier","Conjure Animals", "Find The Path","Heal","Part Water","Speak With Monsters","Stone Tell", "Word Of Recall"]
    seventh_level = [ "Astral Spell","Control Weather", "Earthquake","Gate",  "Holy (Unholy) Word","Regenerate", "Restoration", "Resurrection", "Symbol", "Wind Walk"]

    if level == 1:
        return random.choice(first_level)
    elif level == 2:
        return random.choice(second_level)
    elif level == 3:
        return random.choice(third_level)
    elif level == 4:
        return random.choice(fourth_level)
    elif level == 5:
        return random.choice(fifth_level)
    elif level == 6:
        return random.choice(sixth_level)
    elif level == 7:
        return random.choice(seventh_level)
    else:
        return "Invalid Level"

def druid_choice(level):
    druid = {1: ['Animals Friendship',
    'Detect Magic',
    'Detect Snares & Pits',
    'Entangle',
    'Faerie Fire',
    'Invisibility To Animals',
    'Locate Animals',
    'Pass Without Trace',
    'Predict Weather',
    'Purify Water',
    'Shillelagh',
    'Speak With Animals'],
    2: ['Barkskin',
    'Charm Person/Mammal',
    'Create Water',
    'Cure Light Wounds',
    'Feign Death',
    'Fire Trap',
    'Heat Metal',
    'Locate Plants',
    'Obscurement',
    'Produce Flame',
    'Trip',
    'Warp Wood'],
    3: ['Call Lightning',
    'Cure Disease',
    'Hold Animal',
    'Neutralize Poison',
    'Plant Growth',
    'Protection From Fire',
    'Pyrotechnics',
    'Snare',
    'Stone Shape',
    'Summon Insects',
    'Tree',
    'Water Breathing'],
    4: ['Animals Summoning I',
    'Call Woodland Beings',
    'Control Temperature',
    'Cure Serious Wounds',
    'Dispel Magic',
    'Hallucinatory Forest',
    'Hold Plant',
    'Plant Door',
    'Produce Fire',
    'Prot. From Lightning',
    'Repel Insects',
    'Speak With Plants'],
    5: ['Animals Growth',
    'Animals Summoning II',
    'Anti-Plant Shell',
    'Commune With Nature',
    'Control Winds',
    'Insect Plague',
    'Pass Plant',
    'Sticks To Snakes',
    'Trans Rock To Mud',
    'Wall Of Fire'],
    6: ['Animals Summoning III',
    'Anti-Animals Shell',
    'Conjure Fire Elemental',
    'Cure Critical Wounds',
    'Feeblemind',
    'Fire Seeds',
    'Transport Via Plants',
    'Turn Wood',
    'Wall Of Thorns',
    'Weather Summoning'],
    7: ['Animate Rock',
    'Chariot Of Sustarre',
    'Confusion',
    'Conjure Earth Elemental',
    'Control Weather',
    'Creeping Doom',
    'Finger Of Death',
    'Fire Storm',
    'Reincarnate',
    'Trans Metal To Wood']
    }

    return random.choice(druid[level])

def magicuser_choice(level):
    magicuser = {1: ['Affect Normal Fires',
    'Burning Hands',
    'Charm Person',
    'Comprehend Languages',
    'Dancing Lights',
    'Detect Magic',
    'Enlarge',
    'Erase',
    'Feather Fall',
    'Find Familiar',
    'Friends',
    'Hold Portal',
    'Identify',
    'Jump',
    'Light',
    'Magic Missile',
    'Mending',
    'Message',
    "Nystul's Magic Aura",
    'Protection From Evil',
    'Push',
    'Read Magic',
    'Shield',
    'Shocking Grasp',
    'Sleep',
    'Spider Climb',
    "Tenser's Floating Disc",
    'Unseen Servant',
    'Ventriloquism',
    'Write'],
    2: ['Audible Glamour',
    'Continual Light',
    "Darkness 15' Radius",
    'Detect Evil',
    'Detect Invisibility',
    'ESP',
    'Fools Gold',
    'Forget',
    'Invisibility',
    'Knock',
    "Leomund's Trap",
    'Levitate',
    'Locate Object',
    'Magic Mouth',
    'Mirror Image',
    'Pyrotechnics',
    'Ray Of Enfeeblement',
    'Rope Trick',
    'Scare',
    'Shatter',
    'Stinking Cloud',
    'Strength',
    'Web',
    'Wizard Lock'],
    3: ['Blink',
    'Clairaudience',
    'Clairvoyance',
    'Dispel Magic',
    'Explosive Runes',
    'Feign Death',
    'Fireball',
    'Flame Arrow',
    'Fly',
    'Gust Of Wind',
    'Haste',
    'Hold Person',
    'Infravision',
    "Invisibility 10' Radius",
    "Leomund's Tiny Hut",
    'Lightning Bolt',
    'Monster Summoning I',
    'Phantasmal Force',
    "Protection From Evil 10' Radius",
    'Protection From Normal Missiles',
    'Slow',
    'Suggestion',
    'Tongues',
    'Water Breathing'],
    4: ['Charm Monster',
    'Confusion',
    'Dig',
    'Dimension Door',
    'Enchanted Weapon',
    'Extension I',
    'Fear',
    'Fire Charm',
    'Fire Shield',
    'Fire Trap',
    'Fumble',
    'Hallucinatory Terrain',
    'Ice Storm',
    'Massmorph',
    'Minor Globe Of Invulnerability',
    'Monster Summoning II',
    'Plant Growth',
    'Polymorph Other',
    'Polymorph Self',
    "Rary's Mnemonic Enhancer",
    'Remove Curse',
    'Wall Of Fire',
    'Wall Of Ice',
    'Wizard Eye'],
    5: ['Airy Water',
    'Animals Growth',
    'Animate Dead',
    "Bigby's Interposing Hand",
    'Cloudkill',
    'Conjure Elemental',
    'Cone Of Cold',
    'Contact Other Plane',
    'Distance Distortion',
    'Extension II',
    'Feeblemind',
    'Hold Monster',
    "Leomund's Secret Chest",
    'Magic Jar',
    'Monster Summoning III',
    "Mordenkainen's Faithful Hound",
    'Passwall',
    'Stone Shape',
    'Telekinesis',
    'Teleport',
    'Transmute Rock To Mud',
    'Wall Of Force',
    'Wall Of Iron',
    'Wall Of Stone'],
    6: ['Anti-Magic Shell',
    'Bigbys Forceful Hand',
    'Control Weather',
    'Death Spell',
    'Disintegrate',
    'Enchant An Item',
    'Extension III',
    'Geas',
    'Glassee',
    'Globe Of Invulnerability',
    'Guards And Wards',
    'Invisible Stalker',
    'Legend Lore',
    'Lower Water',
    'Monster Summoning IV',
    'Move Earth',
    'Otilukes Freezing Sphere',
    'Part Water',
    'Project Image',
    'Reincarnation',
    'Repulsion',
    'Spiritwrack',
    'Stone To Flesh',
    'Tensers Transformation'],
    7: ['Bigbys Grasping Hand',
    'Cacodemon',
    'Charm Plants',
    'Delayed Blast Fireball',
    'Drawmijs Instant Summons',
    'Duo-Dimension',
    'Limited Wish',
    'Mass Invisibility',
    'Monster Summoning V',
    'Mordenkainens Sword',
    'Phase Door',
    'Power Word, Stun',
    'Reverse Gravity',
    'Simulacrum',
    'Statue',
    'Vanish'],
    8: ['Antipathy/Sympathy',
    'Bigbys Clenched Fist',
    'Clone',
    'Glassteel',
    'Incendiary Cloud',
    'Mass Charm',
    'Maze',
    'Mind Blank',
    'Monster Summoning VI',
    'Ottos Irresistible Dance',
    'Permanency',
    'Polymorph Any Object',
    'Power Word, Blind',
    'Sertens Spell Immunity',
    'Symbol',
    'Trap The Soul'],
    9: ['Astral Spell',
    'Bigbys Crushing Hand',
    'Gate',
    'Imprisonment',
    'Meteor Swarm',
    'Monster Summoning VII',
    'Power Word, Kill',
    'Prismatic Sphere',
    'Shape Change',
    'Temporal Stasis',
    'Time Stop',
    'Wish']}

    return random.choice(magicuser[level])


def illusionist_choice(level):
    illusionist =  {
    1: ["Audible Glamour", "Change Self", "Colour Spray", "Dancing Lights", "Darkness", "Detect Illusion", "Detect Invisibility", "Gaze Reflection"],
    2: ["Blindness", "Blur", "Deafness", "Detect Magic", "Fog Cloud", "Hypnotic Pattern", "Improved Phantasmal Force", "Invisibility"],
    3: ["Continual Darkness", "Continual Light", "Dispel Illusion", "Emotion", "Hallucinatory Terrain", "Illusionary Script", "Invisibility 10' Radius", "Non-detection"],
    4: ["Confusion", "Dispel Exhaustion", "Fear", "Improved Invisibility", "Massmorph", "Minor Creation", "Phantasmal Killer", "Shadow Monsters"],
    5: ["Chaos", "Demi-Shadow Monsters", "Major Creation", "Maze", "Projected Image", "Shadow Door", "Shades", "Summon Shadow"],
    6: ["Conjure Animals", "Demi-Shadow Magic", "Mass Suggestion", "Permanent Illusion", "Programmed Illusion", "True Sight", "Veil"],
    7: ["Alter Reality", "Astral Spell", "Prismatic Spray", "Prismatic Wall", "Vision"]
}
    return random.choice(illusionist[level])


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

def wand_choice():
    roll = roll_dice(1, 100)
    if roll <= 3:
        return ('Rod of Absorption', 7500, 40000)
    elif roll <= 4:
        return ('Rod of Beguiling', 5000, 30000)
    elif roll <= 14:
        return ('Rod of Cancellation', 10000, 15000)
    elif roll <= 16:
        return ('Rod of Lordly Might', 6000, 20000)
    elif roll <= 17:
        return ('Rod of Resurrection', 10000, 35000)
    elif roll <= 18:
        return ('Rod of Rulership', 8000, 35000)
    elif roll <= 19:
        return ('Rod of Smiting', 4000, 15000)
    elif roll <= 20:
        return ('Staff of Command', 5000, 25000)
    elif roll <= 22:
        return ('Staff of Curing', 6000, 25000)
    elif roll <= 23:
        return ('Staff of the Magi', 15000, 75000)
    elif roll <= 24:
        return ('Staff of Power', 12000, 60000)
    elif roll <= 27:
        return ('Staff of the Serpent', 7000, 35000)
    elif roll <= 31:
        return ('Staff of Striking', 6000, 15000)
    elif roll <= 33:
        return ('Staff of Withering', 8000, 35000)
    elif roll <= 34:
        return ('Wand of Conjuration', 7000, 35000)
    elif roll <= 38:
        return ('Wand of Enemy Detection', 2000, 10000)
    elif roll <= 41:
        return ('Wand of Fear', 3000, 15000)
    elif roll <= 44:
        return ('Wand of Fire', 4500, 25000)
    elif roll <= 47:
        return ('Wand of Frost', 6000, 50000)
    elif roll <= 52:
        return ('Wand of Illumination', 2000, 10000)
    elif roll <= 56:
        return ("Wand of Illusion", 3000, 20000)
    elif roll <= 59:
        return ("Wand of Lightning", 4000, 30000)
    elif roll <= 68:
        return ("Wand of Magic Detection", 2500, 25000)
    elif roll <= 73:
        return ("Wand of Metal & Mineral Detection", 1500, 7500)
    elif roll <= 78:
        return ("Wand of Magic Missiles", 4000, 35000)
    elif roll <= 86:
        return ("Wand of Negation", 3500, 15000)
    elif roll <= 89:
        return ("Wand of Paralyzation", 3500, 25000)
    elif roll <= 92:
        return ("Wand of Polymorphing", 3500, 25000)
    elif roll <= 94:
        return ("Wand of Secret Door & Trap Location", 5000, 40000)
    else:
        return ("Wand of Wonder", 6000, 10000)

def armour_choice():
    dice_roll = roll_dice(1, 100)
    if dice_roll <= 5:
        return ('Chain Mail +1', 600, 3500)
    elif dice_roll <= 9:
        return ('Chain Mail +2', 1200, 7500)
    elif dice_roll <= 11:
        return ('Chain Mail +3', 2000, 12500)
    elif dice_roll <= 19:
        return ('Leather Armor +1', 300, 2000)
    elif dice_roll <= 26:
        return ('Plate Mail +1', 800, 5000)
    elif dice_roll <= 32:
        return ('Plate Mail +2', 1750, 10500)
    elif dice_roll <= 35:
        return ('Plate Mail +3', 2750, 15500)
    elif dice_roll <= 37:
        return ('Plate Mail +4', 3500, 20500)
    elif dice_roll == 38:
        return ('Plate Mail +5', 4500, 27500)
    elif dice_roll == 39:
        return ('Plate Mail of Etherealness', 5000, 30000)
    elif dice_roll <= 44:
        return ('Plate Mail of Vulnerability', 0, 1500)
    elif dice_roll <= 50:
        return ('Ring Mail +1', 400, 2500)
    elif dice_roll <= 55:
        return ('Scale Mail +1', 500, 3000)
    elif dice_roll <= 59:
        return ('Scale Mail +2', 1100, 6750)
    elif dice_roll <= 63:
        return ('Splint Mail +1', 700, 4000)
    elif dice_roll <= 66:
        return ('Splint Mail +2', 1500, 8500)
    elif dice_roll <= 68:
        return ('Splint Mail +3', 2250, 14500)
    elif dice_roll == 69:
        return ('Splint Mail +4', 3000, 19000)
    elif dice_roll <= 75:
        return ('Studded Leather +1', 400, 2500)
    elif dice_roll <= 84:
        return ('Shield +1', 250, 2500)
    elif dice_roll <= 89:
        return ('Shield +2', 500, 5000)
    elif dice_roll <= 93:
        return ('Shield +3', 800, 8000)
    elif dice_roll <= 95:
        return ('Shield +4', 1200, 12000)   
    elif dice_roll <= 96:
        return ('Shield +5', 1200, 17500)   
    elif dice_roll <= 97:
        return ('Shield large +1 +4 vs missiles', 400, 4000)
    else:
        return ('Shield -1 Missile attractor', 0, 750)

def sword_choice():
    dice_roll = roll_dice(1,100)
    if dice_roll <= 25:
        return ("Sword +1", 400, 2000)
    elif dice_roll <= 30:
        return ("Sword +1 +2 vs magic-using & enchanted creatures", 600, 3000)
    elif dice_roll <= 35:
        return ("Sword +1 +3 vs lycanthropes & shape changers", 700, 3500)
    elif dice_roll <= 40:
        return ("Sword +1 +3 vs regenerating creatures", 800, 4000)
    elif dice_roll <= 45:
        return ("Sword +1 +4 vs reptiles", 800, 4000)
    elif dice_roll <= 49:
        return ("Sword +1 Flame Tongue: +2 vs. regenerating creatures +3 vs cold-using inflammable or avian creatures +4 vs. undead", 900, 4500)
    elif dice_roll <= 50:
        return ("Sword +1 Luck Blade", 1000, 5000)
    elif dice_roll <= 58:
        return ("Sword +2", 800, 4000)
    elif dice_roll <= 62:
        return ("Sword +2 Giant Slayer", 900, 4500)
    elif dice_roll <= 66:
        return ("Sword +2 Dragon Slayer", 900, 4500)
    elif dice_roll <= 67:
        return ("Sword +2 Nine Lives Stealer", 1600, 8000)
    if dice_roll <= 71:
        return ('Sword +3', 1400, 7000)
    elif dice_roll <= 74:
        return ('Sword +3 Frost Brand: +6 vs fire using or dwelling creatures', 1600, 8000)
    elif dice_roll <= 76:
        return ('Sword +4', 2000, 10000)
    elif dice_roll <= 77:
        return ('Sword +4 Defender', 3000, 15000)
    elif dice_roll <= 78:
        return ('Sword +5', 3000, 15000)
    elif dice_roll <= 79:
        return ('Sword +5 Defender', 3600, 18000)
    elif dice_roll <= 80:
        return ('Sword +5 Holy Avenger', 4000, 20000)
    elif dice_roll <= 81:
        return ('Sword of Dancing', 4400, 22000)
    elif dice_roll <= 82:
        return ('Sword of Wounding', 4400, 22000)
    elif dice_roll <= 83:
        return ('Sword of Life Stealing', 5000, 25000)
    elif dice_roll <= 84:
        return ('Sword of Sharpness', 7000, 35000)
    elif dice_roll <= 85:
        return ('Sword Vorpal Weapon', 10000, 50000)
    elif dice_roll <= 90:
        return ('Sword +1 Cursed', 400, 0)
    elif dice_roll <= 95:
        return ('Sword -2 Cursed', 600, 0)
    else:
        return ('Sword Cursed Berserking', 900, 0)        

def weapon_choice():
    roll = roll_dice(1,100)
    if roll <= 8:
        return ("Arrow +1", 20, 120) #random number of these if want fancier
        #, random.randint(2,24)
    elif roll <= 12:
        return ("Arrow +2", 50, 300) #random number of these if want fancier
        #, random.randint(2,16)
    elif roll == 13:
        return ("Arrow +3", 75, 450)
        #, random.randint(2,12)
    elif roll == 14:
        return ("Arrow of Slaying", 250, 2500)
    elif roll <= 20:
        return ("Axe +1", 300, 1750)
    elif roll <= 22:
        return ("Axe +2", 600, 3750)
    elif roll == 23:
        return ("Axe +2 Throwing", 750, 4500)
    elif roll == 24:
        return ("Axe +3", 1000, 7000)
    elif roll <= 27:
        return ("Battle Axe +1", 400, 2500)
    elif roll <= 32:
        return ("Bolt +2", 50, 300)  #random number of these if want fancier
    elif roll == 33:
        return ("Bow +1", 500, 3500)
    elif roll == 34:
        return ("Crossbow of Accuracy +3", 2000, 12000)
    elif roll == 35:
        return ("Crossbow of Distance", 1500, 7500)
    elif roll == 36:
        return ("Crossbow of Speed", 1500, 7500)
    elif roll <= 46:
        return ("Dagger +1", 100, 750)
    elif roll <= 50:
        return ("Dagger +2", 250, 2000)
    elif roll == 51:
        return ("Dagger of Venom", 350, 3000)
    elif roll <= 56:
        return ("Flail +1", 450, 4000)
    elif roll <= 60:
        return ("Hammer +2", 300, 2500)
    elif roll <= 62:
        return ("Hammer +2", 650, 6000)
    elif roll == 63:
        return ("Hammer +3 Dwarven Thrower", 1500, 15000)
    elif roll == 64:
        return ("Hammer of Thunderbolts", 2500, 25000)
    elif roll <= 67:
        return ("Javelin +2", 750, 5000)
    elif roll <= 72:
        return ("Mace +1", 350, 3000)
    elif roll <= 75:
        return ("Mace +2", 700, 4500)
    elif roll == 76:
        return ("Mace of Disruption", 1750, 17500)
    elif roll == 77:
        return ("Mace +4", 1500, 15000)
    elif roll <= 80:
        return ("Military Pick +1", 350, 2500)
    elif roll <= 83:
        return ("Morning Star +1", 400, 3000)
    elif roll <= 88:
        return ("Scimitar +2", 750, 6000)
    elif roll == 89:
        return ("Sling of Seeking +2", 700, 7000)
    elif roll <= 94:
        return ("Spear +1", 500, 3000)
    elif roll <= 96:
        return ("Spear +2", 1000, 6500)
    elif roll == 97:
        return ("Spear +3", 1750, 15000)
    elif roll <= 99:
        return ("Spear Cursed Backbiter", 0, 1000)
    else:
        return ("Trident-Military Fork +3", 1500, 12500)

def misc_1_choice():
    roll = roll_dice(1, 100)
    if roll <= 2:
        return ("Alchemy Jug", 3000, 12000)
    elif roll <= 4:
        return ("Amulet of Inescapable Location", 0, 1000)
    elif roll == 5:
        return ("Amulet of Life Protection", 5000, 20000)
    elif roll <= 7:
        return ("Amulet of the Planes", 6000, 30000)
    elif roll <= 11:
        return ("Amulet of Proof Against Detection and Location", 4000, 15000)
    elif roll <= 13:
        return ("Apparatus of Kwalish", 8000, 35000)
    elif roll <= 16:
        return ("Arrow of Direction", 2500, 17500)
    elif roll == 17:
        return ("Artifact or Relic (see Special table)", 0, 0)
    elif roll <= 20:
        return ("Bag of Beans", 1000, 5000)
    elif roll == 21:
        return ("Bag of Devouring", 0, 1500)
    elif roll <= 26:
        return ("Bag of Holding", 5000, 25000)
    elif roll == 27:
        return ("Bag of Transmuting", 0, 500)
    elif roll <= 29:
        return ("Bag of Tricks", 2500, 15000)
    elif roll <= 31:
        return ("Beaker of Plentiful Potions", 1500, 12500)
    elif roll == 32:
        return ("Boat-Folding", 10000, 25000)
    elif roll == 33:
        return ("Book of Exalted Deeds (C)", 8000, 40000)
    elif roll == 34:
        return ("Book of Infinite Spells", 9000, 50000)
    elif roll == 35:
        return ("Book of Vile Darkness (C)", 8000, 40000)
    elif roll == 36:
        return ("Boots of Dancing", 0, 5000)
    elif roll <= 42:
        return ("Boots of Elvenkind", 1000, 5000)
    elif roll <= 47:
        return ("Boots of Levitation", 2000, 15000)
    elif roll <= 51:
        return ("Boots of Speed", 2500, 20000)
    elif roll <= 55:
        return ("Boots of Striding and Springing", 2500, 20000)
    elif roll <= 58:
        return ("Bowl Commanding Water Elementals (M)", 4000, 25000)
    elif roll == 59:
        return ("Bowl of Watery Death (M)", 0, 1000)
    elif roll <= 79:
        return ("Bracers of Defense", 500, 3000)
    elif roll <= 81:
        return ("Bracers of Defenselessness", 0, 2000)
    elif roll <= 84:
        return ("Brazier Commanding Fire Elementals (M)", 4000, 25000)
    elif roll == 85:
        return ("Brazier of Sleep Smoke (M)", 0, 1000)
    elif roll <= 92:
        return ("Brooch of Shielding", 1000, 10000)
    elif roll == 93:
        return ("Broom of Animated Attack", 0, 3000)
    elif roll == 93:
        return ("Broom of Flying", 2000, 10000)
    else:
        p = roll_dice(1,3)
        if p == 1:
            return ("Bucknards Everfull Purse", 1500, 15000)
        elif p == 2:
            return ("Bucknards Everfull Purse", 2500, 25000)
        else:
            return ("Bucknards Everfull Purse", 4000, 40000)

def misc_2_choice():
    roll = roll_dice(1, 100)
    if roll <= 6:
        return ("Candle of Invocation", 1000, 5000)
    elif roll <= 8:
        return ("Carpet of Flying", 7500, 25000)
    elif roll == 9:
        return ("Censer Controlling Air Elementals", 4000, 25000)
    elif roll == 10:
        return ("Censer of Summoning Hostile Air Elementals", 0, 1000)
    elif roll <= 13:
        return ("Chime of Opening", 3500, 20000)
    elif roll == 14:
        return ("Chime of Hunger", 0, 0)
    elif roll <= 17:
        return ("Cloak of Displacement", 3000, 17500)
    elif roll <= 27:
        return ("Cloak of Elvenkind", 1000, 6000)
    elif roll <= 30:
        return ("Cloak of Manta Ray", 2000, 12500)
    elif roll <= 32:
        return ("Cloak of Poisonousness", 0, 2500)    
    elif roll <= 55:
        return ("Cloak of Protection", 1000, 10000)
    elif roll <= 60:
        return ("Crystal Ball", 1000, 5000)
    elif roll == 61:
        return ("Crystal Hypnosis Ball", 0, 3000)
    elif roll <= 63:
        return ("Cube of Force", 3000, 20000)
    elif roll <= 65:
        return ("Cube of Frost Resistance", 2000, 14000)
    elif roll <= 67:
        return ("Cubic Gate", 5000, 17500)
    elif roll <= 69:
        return ("Daerns Instant Fortress", 7000, 27500)
    elif roll <= 72:
        return ("Decanter of Endless Water", 1000, 3000)
    elif roll <= 76:
        return ("Deck of Many Things", 0, 10000)
    elif roll == 77:
        return ("Drums of Deafening", 0, 500)
    elif roll <= 79:
        return ("Drums of Panic", 6500, 35000)
    elif roll <= 85:
        return ("Dust of Appearance", 1000, 4000)
    elif roll <= 91:
        return ("Dust of Disappearance", 2000, 8000)
    elif roll == 92:
        return ("Dust of Sneezing and Choking", 0, 1000)
    elif roll == 93:
        return ("Efreeti Bottle", 9000, 45000)
    elif roll == 94:
        return ("Eversmoking Bottle", 500, 2500)
    elif roll == 95:
        return ("Eyes of Charming (M)", 4000, 24000)
    elif roll <= 97:
        return ("Eyes of the Eagle", 3500, 18000)
    elif roll <= 99:
        return ("Eyes of Minute Seeing", 2000, 12500)
    else:
        p = roll_dice(1,2)
        if p == 1:
            return ("Eyes of Reverse Petrification", 12500, 50000)        
        else:
            return ("Eyes of Petrification", 0, 0)        

def misc_3_choice():
    roll = random.randint(1, 100)
    if roll <= 15:
        return ("Figurine of Wondrous Power", 100, 1000)
    elif roll <= 16:
        return ("Flask of Curses", 0, 1000)
    elif roll <= 18:
        return ("Gauntlets of Dexterity", 1000, 10000)
    elif roll <= 20:
        return ("Gauntlets of Fumbling", 0, 1000)
    elif roll <= 22:
        return ("Gauntlets of Ogre Power", 1000, 15000)
    elif roll <= 25:
        return ("Gauntlets of Swimming and Climbing", 1000, 10000)
    elif roll <= 26:
        return ("Gem of Brightness", 2000, 17500)
    elif roll <= 27:
        return ("Gem of Seeing", 2000, 25000)
    elif roll <= 28:
        return ("Girdle of Femininity-Masculinity", 0, 1000)
    elif roll <= 29:
        return ("Girdle of Giant Strength", 200, 2500)
    elif roll <= 30:
        return ("Helm of Brilliance", 2500, 60000)
    elif roll <= 35:
        return ("Helm of Comprehending Languages and Reading Magic", 1000, 12500)
    elif roll <= 37:
        return ("Helm of Opposite Alignment", 0, 1000)
    elif roll <= 39:
        return ("Helm of Telepathy", 3000, 35000)
    elif roll <= 40:
        return ("Helm of Teleportation", 2500, 30000)
    elif roll <= 45:
        return ("Helm of Underwater Action", 1000, 10000)
    elif roll <= 46:
        return ("Horn of Blasting", 5000, 55000)
    elif roll <= 48:
        return ("Horn of Bubbles", 0, 0)
    elif roll <= 49:
        return ("Horn of Collapsing", 1500, 25000)
    elif roll <= 53:
        return ("Horn of the Tritons", 2000, 17500)
    elif roll <= 60:
        return ("Horn of Valhalla", 1000, 15000)
    elif roll <= 63:
        return ("Horseshoes of Speed", 2000, 10000)
    elif roll <= 65:
        return ("Horseshoes of a Zephyr", 1500, 7500)
    elif roll <= 70:
        return ("Incense of Meditation", 500, 7500)
    elif roll <= 71:
        return ("Incense of Obsession", 0, 500)    
    elif roll <= 72:
        return ("Ioun Stones", 300, 5000)
    elif roll <= 78:
        return ("Instrument of the Bards", 1000, 5000)
    elif roll <= 80:
        return ("Iron Flask", 0, 0)
    elif roll <= 85:
        return ("Javelin of Lightning (F)", 250, 3000)
    elif roll <= 90:
        return ("Javelin of Piercing (F)", 250, 3000)
    elif roll <= 91:
        return ("Jewel of Attacks", 0, 1000)
    elif roll <= 92:
        return ("Jewel of Flawlessness", 0, "1000")
    else:
        return ("Keoghtom’s Ointment", 500, 10000)        

def misc_4_choice():
    roll = roll_dice(1, 100)
    if roll <= 4:
        return ("Libram of Gainful Conjuration", 8000, 40000)
    elif roll <= 8:
        return ("Libram of Ineffable Damnation", 8000, 40000)
    elif roll <= 12:
        return ("Libram of Silver Magic", 8000, 40000)
    elif roll == 5:
        return ("Lyre of Building", 5000, 30000)
    elif roll <= 6:
        return ("Manual of Bodily Health", 5000, 50000)
    elif roll <= 7:
        return ("Manual of Gainful Exercise", 5000, 50000)
    elif roll <= 8:
        return ("Manual of Golems", 3000, 30000)
    elif roll <= 9:
        return ("Manual of Puissant Skill at Arms", 8000, 40000)
    elif roll <= 10:
        return ("Manual of Quickness of Action", 5000, 50000)
    elif roll <= 11:
        return ("Manual of Stealthy Pilfering", 8000, 40000)
    elif roll == 12:
        return ("Mattock of the Titans", 3500, 7000)
    elif roll == 13:
        return ("Maul of the Titans", 4000, 12000)
    elif roll <= 15:
        return ("Medallion of ESP", 1000, 10000)
    elif roll <= 17:
        return ("Medallion of Thought Projection", 0, 1000)
    if roll <= 18:
        return ("Mirror of Life Trapping", 2500, 25000)
    elif roll <= 19:
        return ("Mirror of Mental Prowess", 5000, 50000)
    elif roll == 20:
        return ("Mirror of Opposition", 0, 2000)
    elif roll <= 23:
        return ("Necklace of Adaptation", 1000, 10000)
    elif roll <= 27:
        return ("Necklace of Missiles", 50, 200)
    elif roll <= 33:
        return ("Necklace of Prayer Beads", 500, 3000)
    elif roll <= 35:
        return ("Necklace of Strangulation", 0, 1000)
    elif roll <= 38:
        return ("Net of Entrapment", 1000, 7500)
    elif roll <= 42:
        return ("Net of Snaring", 1000, 6000)
    elif roll <= 44:
        return ("Nolzurs Marvelous Pigments", 500, 3000)
    elif roll <= 46:
        return ("Pearl of Power", 200, 2000)
    elif roll <= 48:
        return ("Pearl of Wisdom", 500, 5000)
    elif roll <= 50:
        return ("Periapt of Foul Rotting", 0, 1000)
    elif roll <= 53:
        return ("Periapt of Health", 1000, 10000)
    elif roll <= 60:
        return ("Periapt of Proof Against Poison", 1500, 12500)
    elif roll <= 64:
        return ("Periapt of Wound Closure", 1000, 10000)
    elif roll <= 70:
        return ("Phylactery of Faithfulness", 1000, 7500)
    elif roll <= 74:
        return ("Phylactery of Long Years", 3000, 25000)
    elif roll <= 76:
        return ("Phylactery of Monstrous Attention", 0, 2000)
    elif roll <= 84:
        return ("Pipes of the Sewers", 1750, 8500)
    elif roll == 85:
        return ("Portable Hole", 5000, 50000)
    else:
        return ("Quaal’s Feather Token", 500, 2000)

def misc_5_choice():
    roll = roll_dice(1, 100)
    if roll <= 1:
        return ("Robe of the Archmagi", 6000, 65000)
    elif roll <= 8:
        return ("Robe of Blending", 3500, 35000)
    elif roll == 9:
        return ("Robe of Eyes", 4500, 50000)
    elif roll == 10:
        return ("Robe of Powerlessness", 0, 1000)
    elif roll == 11:
        return ("Robe of Scintillating Colors", 2750, 25000)
    elif roll <= 19:
        return ("Robe of Useful Items", 1500, 15000)
    elif roll <= 25:
        return ("Rope of Climbing", 1000, 10000)
    elif roll <= 27:
        return ("Rope of Constriction", 0, 1000)
    elif roll <= 31:
        return ("Rope of Entanglement", 1250, 12000)
    elif roll == 32:
        return ("Rug of Smothering", 0, 1500)
    elif roll == 33:
        return ("Rug of Welcome", 6500, 45000)
    elif roll == 34:
        return ("Saw of Mighty Cutting", 1750, 12500)
    elif roll == 35:
        return ("Scarab of Death", 0, 2500)
    elif roll <= 38:
        return ("Scarab of Enraging Enemies", 1000, 8000)
    elif roll <= 40:
        return ("Scarab of Insanity", 1500, 11000)
    elif roll <= 46:
        return ("Scarab of Protection", 2500, 25000)
    elif roll == 47:
        return ("Spade of Colossal Excavation", 1000, 6500)
    elif roll == 48:
        return ("Sphere of Annihilation", 3750, 30000)
    elif roll <= 50:
        return ("Stone of Controlling Earth Elementals", 1500, 12500)
    elif roll <= 52:
        return ("Stone of Good Luck (Luckstone)", 3000, 25000)
    elif roll <= 54:
        return ("Stone of Weight (Loadstone)", 0, 1000)
    elif roll <= 57:
        return ("Talisman of Pure Good", 3500, 27500)
    elif roll == 58:
        return ("Talisman of the Sphere", 100, 10000)
    elif roll <= 60:
        return ("Talisman of Ultimate Evil", 3500, 32500)        
    elif roll <= 66:
        return ("Talisman of Zagy", 1000, 10000)
    elif roll == 67:
        return ("Tome of Clear Thought", 8000, 48000)
    elif roll == 68:
        return ("Tome of Leadership and Influence", 7500, 40000)
    elif roll == 69:
        return ("Tome of Understanding", 8000, 43500)
    elif roll <= 76:
        return ("Trident of Fish Command (C F T)", 500, 4000)
    elif roll <= 78:
        return ("Trident of Submission (F)", 1250, 12500)
    elif roll <= 83:
        return ("Trident of Warning (C F T)", 1000, 10000)
    elif roll <= 85:
        return ("Trident of Yearning", 0, 1000)
    elif roll <= 87:
        return ("Vacuous Grimoire", 0, 1000)
    elif roll <= 90:
        return ("Well of Many Worlds", 6000, 12000)
    else:
        return ("Wings of Flying", 750, 7500)        

def treasure_choice(treasure_type, no):
    if v:
        print(treasure_type, no)
    treasure = {}
    treasure['copper'] = 0
    treasure['silver'] = 0
    treasure['electrum'] = 0
    treasure['gold'] = 0
    treasure['platinum'] = 0
    treasure['gems'] = 0
    treasure['jewellery'] = 0
    treasure['magic'] = 0

    if treasure_type == "A":
        r = roll_dice(1,100)
        if r <= 25:
            treasure['copper'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)
        if r <= 30:
            treasure['silver'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)
        if r <= 35:
            treasure['electrum'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)            
        if r <= 40:
            treasure['gold'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)            
        if r <= 25:
            treasure['platinum'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)            
        if r <= 60:
            treasure['gems'] = roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10) 
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['jewellery'] = roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10) 
        r = roll_dice(1,100)            
        if r <= 30:
            magic_list = []
            for c in range(3):
                magic_list.append(random.choice(["Sword", "Armor", "Misc. Weapon"]))
            treasure['magic'] = magic_list

    elif treasure_type == "B":
        r = roll_dice(1,100)
        if r <= 50:
            treasure['copper'] = roll_dice(1,8) * 1000
        r = roll_dice(1,100)
        if r <= 25:
            treasure['silver'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)
        if r <= 25:
            treasure['electrum'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)            
        if r <= 25:
            treasure['gold'] = roll_dice(1,3) * 1000
        r = roll_dice(1,100)            
        if r <= 30:
            treasure['gems'] = roll_dice(1,8)
        r = roll_dice(1,100)            
        if r <= 20:
            treasure['jewellery'] = roll_dice(1,4)
        r = roll_dice(1,100)            
        if r <= 10:
            magic_list = []
            for c in range(1):
                magic_list.append(random.choice(["Sword", "Armor", "Misc. Weapon"]))
            treasure['magic'] = magic_list

    elif treasure_type == "C":
        r = roll_dice(1,100)
        if r <= 20:
            treasure['copper'] = roll_dice(1,12) * 1000
        r = roll_dice(1,100)
        if r <= 30:
            treasure['silver'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)
        if r <= 10:
            treasure['electrum'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)            
        if r <= 25:
            treasure['gems'] = roll_dice(1,6)
        r = roll_dice(1,100)            
        if r <= 20:
            treasure['jewellery'] = roll_dice(1,3)
        r = roll_dice(1,100)            
        if r <= 10:
            magic_list = []
            for c in range(2):
                magic_list.append(random.choice(["Any"]))
            treasure['magic'] = magic_list

    elif treasure_type == "D":
        r = roll_dice(1,100)
        if r <= 10:
            treasure['copper'] = roll_dice(1,8) * 1000
        r = roll_dice(1,100)
        if r <= 15:
            treasure['silver'] = roll_dice(1,12) * 1000
        r = roll_dice(1,100)
        if r <= 15:
            treasure['electrum'] = roll_dice(1,8) * 1000
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['gold'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)            
        if r <= 30:
            treasure['gems'] = roll_dice(1,10)
        r = roll_dice(1,100)            
        if r <= 25:
            treasure['jewellery'] = roll_dice(1,6)
        r = roll_dice(1,100)            
        if r <= 15:
            magic_list = []
            for c in range(2):
                magic_list.append(random.choice(["Any"]))
            for c in range(1):
                magic_list.append(random.choice(["Potion"]))
            treasure['magic'] = magic_list

    elif treasure_type == "E":
        r = roll_dice(1,100)
        if r <= 5:
            treasure['copper'] = roll_dice(1,10) * 1000
        r = roll_dice(1,100)
        if r <= 25:
            treasure['silver'] = roll_dice(1,12) * 1000
        r = roll_dice(1,100)
        if r <= 25:
            treasure['electrum'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)            
        if r <= 25:
            treasure['gold'] = roll_dice(1,8) * 1000
        r = roll_dice(1,100)            
        if r <= 15:
            treasure['gems'] = roll_dice(1,12)
        r = roll_dice(1,100)            
        if r <= 10:
            treasure['jewellery'] = roll_dice(1,8)
        r = roll_dice(1,100)            
        if r <= 25:
            magic_list = []
            for c in range(3):
                magic_list.append(random.choice(["Any"]))
            for c in range(1):
                magic_list.append(random.choice(["Scroll"]))
            treasure['magic'] = magic_list

    elif treasure_type == "F":
        r = roll_dice(1,100)
        if r <= 10:
            treasure['silver'] = roll_dice(1,20) * 1000
        r = roll_dice(1,100)
        if r <= 15:
            treasure['electrum'] = roll_dice(1,12) * 1000
        r = roll_dice(1,100)            
        if r <= 40:
            treasure['gold'] = roll_dice(1,10) * 1000
        r = roll_dice(1,100)            
        if r <= 35:
            treasure['platinum'] = roll_dice(1,8) * 1000
        r = roll_dice(1,100)            
        if r <= 20:
            treasure['gems'] = roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10)
        r = roll_dice(1,100)            
        if r <= 10:
            treasure['jewellery'] = roll_dice(1,10)
        r = roll_dice(1,100)            
        if r <= 30:
            magic_list = []
            for c in range(3):
                magic_list.append(random.choice(["Potion","Scroll","Ring","Wand","Armor","Misc 1","Misc 2","Misc 3","Misc 4","Misc 5"]))
            for c in range(1):
                magic_list.append(random.choice(["Potion"]))
            for c in range(1):
                magic_list.append(random.choice(["Scroll"]))
            treasure['magic'] = magic_list

    elif treasure_type == "G":
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['gold'] = roll_dice(1,4) * 10 * 1000
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['platinum'] = roll_dice(1,20) * 1000
        r = roll_dice(1,100)            
        if r <= 30:
            treasure['gems'] = roll_dice(1,4) + roll_dice(1,4) + roll_dice(1,4) + roll_dice(1,4) + roll_dice(1,4)
        r = roll_dice(1,100)            
        if r <= 25:
            treasure['jewellery'] = roll_dice(1,10)
        r = roll_dice(1,100)            
        if r <= 30:
            magic_list = []
            for c in range(3):
                if v:
                    print(c)
                magic_list.append(random.choice(["Potion","Scroll","Ring","Wand","Armor","Misc 1","Misc 2","Misc 3","Misc 4","Misc 5"]))
            for c in range(1):
                magic_list.append(random.choice(["Potion"]))
            for c in range(1):
                magic_list.append(random.choice(["Scroll"]))
            treasure['magic'] = magic_list

    elif treasure_type == "H":
        r = roll_dice(1,100)
        if r <= 25:
            treasure['copper'] = roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6)
            treasure['copper'] = treasure['copper'] * 1000
        r = roll_dice(1,100)
        if r <= 40:
            treasure['silver'] = roll_dice(1,100) * 1000
        r = roll_dice(1,100)
        if r <= 40:
            treasure['electrum'] = roll_dice(1,4) * 10 * 1000
        r = roll_dice(1,100)            
        if r <= 55:
            treasure['gold'] = roll_dice(1,6) * 10 * 1000
        r = roll_dice(1,100)            
        if r <= 25:
            treasure['platinum'] = roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10) + roll_dice(1,10)
            treasure['platinum'] = treasure['platinum'] * 1000
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['gems'] = roll_dice(1,100)
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['jewellery'] = roll_dice(1,10) * 4
        r = roll_dice(1,100)            
        if r <= 15:
            magic_list = []
            for c in range(4):
                magic_list.append(random.choice(["Sword", "Armor", "Misc. Weapon"]))
            for c in range(1):
                magic_list.append(random.choice(["Potion"]))
            for c in range(1):
                magic_list.append(random.choice(["Scroll"]))
            treasure['magic'] = magic_list

    elif treasure_type == "I":
        r = roll_dice(1,100)            
        if r <= 30:
            treasure['platinum'] = roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6)
            treasure['platinum'] = treasure['platinum'] * 1000
        r = roll_dice(1,100)            
        if r <= 55:
            treasure['gems'] = roll_dice(1,10) + roll_dice(1,10)
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['jewellery'] = roll_dice(1,12)
        r = roll_dice(1,100)            
        if r <= 15:
            magic_list = []
            for c in range(1):
                magic_list.append(random.choice(["Any"]))
            treasure['magic'] = magic_list

    elif treasure_type == "J":
        for n in range(no):
            treasure['copper'] = treasure['copper'] + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6)
        
    elif treasure_type == "K":
        for n in range(no):
            treasure['silver'] = treasure['silver'] + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6)

    elif treasure_type == "L":
        for n in range(no):
            treasure['electrum'] = treasure['electrum'] + roll_dice(1,6) + roll_dice(1,6)

    elif treasure_type == "M":
        for n in range(no):
            treasure['gold'] = treasure['gold'] + roll_dice(1,4) + roll_dice(1,4)

    elif treasure_type == "N":
        for n in range(no):
            treasure['platinum'] = treasure['platinum'] + roll_dice(1,6)

    elif treasure_type == "O":
        r = roll_dice(1,100)
        if r <= 25:
            treasure['copper'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)
        if r <= 20:
            treasure['silver'] = roll_dice(1,3) * 1000

    elif treasure_type == "P":
        r = roll_dice(1,100)
        if r <= 25:
            treasure['silver'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)
        if r <= 20:
            treasure['electrum'] = roll_dice(1,2) * 1000

    elif treasure_type == "Q":
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['gems'] = roll_dice(1,4)

    elif treasure_type == "R":
        r = roll_dice(1,100)            
        if r <= 40:
            treasure['gold'] = roll_dice(1,4)+roll_dice(1,4)
            treasure['gold'] = treasure['gold'] * 1000
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['platinum'] = roll_dice(1,6) * 10 * 1000
        r = roll_dice(1,100)            
        if r <= 55:
            treasure['gems'] = roll_dice(1,8) + roll_dice(1,8) + roll_dice(1,8) + roll_dice(1,8)
        r = roll_dice(1,100)            
        if r <= 45:
            treasure['jewellery'] = roll_dice(1,12)

    elif treasure_type == "S":
        r = roll_dice(1,100)            
        if r <= 45:
            magic_list = []
            for c in range(roll_dice(1,4) + roll_dice(1,4)):
                magic_list.append(random.choice(["Potion"]))
            treasure['magic'] = magic_list

    elif treasure_type == "T":
        r = roll_dice(1,100)            
        if r <= 50:
            magic_list = []
            for c in range(roll_dice(1,4)):
                magic_list.append(random.choice(["Scroll"]))
            treasure['magic'] = magic_list

    elif treasure_type == "U":
        r = roll_dice(1,100)            
        if r <= 90:
            treasure['gems'] = roll_dice(1,8) * 10
        r = roll_dice(1,100)            
        if r <= 80:
            treasure['jewellery'] = roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6)
        r = roll_dice(1,100)            
        if r <= 70:
            magic_list = []
            magic_list.append(["Ring","Wand","Sword","Weapon","Armor","Misc 1","Misc 2","Misc 3","Misc 4","Misc 5"])
            treasure['magic'] = magic_list

    elif treasure_type == "V":
        r = roll_dice(1,100)            
        if r <= 70:
            magic_list = []
            magic_list.append(["Ring","Wand","Sword","Weapon","Armor","Misc 1","Misc 2","Misc 3","Misc 4","Misc 5"])
            magic_list.append(["Ring","Wand","Sword","Weapon","Armor","Misc 1","Misc 2","Misc 3","Misc 4","Misc 5"])
            treasure['magic'] = magic_list

    elif treasure_type == "W":
        r = roll_dice(1,100)            
        if r <= 60:
            treasure['gold'] = roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6)
            treasure['gold'] = treasure['gold'] * 1000
        r = roll_dice(1,100)            
        if r <= 15:
            treasure['platinum'] = roll_dice(1,8) * 1000
        r = roll_dice(1,100)            
        if r <= 60:
            treasure['gems'] = roll_dice(1,8) * 10
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['jewellery'] = roll_dice(1,8) + roll_dice(1,8) + roll_dice(1,8) + roll_dice(1,8) + roll_dice(1,8)

    elif treasure_type == "X":
        r = roll_dice(1,100)            
        if r <= 70:
            magic_list = []
            magic_list.append(random.choice(["Misc 1","Misc 2","Misc 3","Misc 4","Misc 5"]))
            magic_list.append(["Potion"])
            treasure['magic'] = magic_list

    elif treasure_type == "Y":
        r = roll_dice(1,100)            
        if r <= 70:
            treasure['gold'] = (roll_dice(1,6) + roll_dice(1,6)) * 1000

    else: #treasure_type == "Z":
        r = roll_dice(1,100)
        if r <= 20:
            treasure['copper'] = roll_dice(1,3) * 1000
        r = roll_dice(1,100)
        if r <= 25:
            treasure['silver'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)
        if r <= 25:
            treasure['electrum'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)            
        if r <= 30:
            treasure['gold'] = roll_dice(1,4) * 1000
        r = roll_dice(1,100)            
        if r <= 30:
            treasure['platinum'] = roll_dice(1,6) * 1000
        r = roll_dice(1,100)            
        if r <= 55:
            treasure['gems'] = roll_dice(1,10) * 60
        r = roll_dice(1,100)            
        if r <= 50:
            treasure['jewellery'] = roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6) + roll_dice(1,6)  
        r = roll_dice(1,100)            
        if r <= 30:
            magic_list = []
            for c in range(3):
                magic_list.append(random.choice(["Any"]))
            treasure['magic'] = magic_list

    return treasure

# Example usage
def select_magic_item():
    roll = roll_dice(1, 100)
    choice = ""
    if roll <= 20:
        item = "Potions (A.)"
        choice = potion_choice()
    elif roll <= 35:
        item = "Scrolls (B.)"

        no, rnge, xp, class_use = scroll_choice()
        individual_spells = []
        if isinstance(rnge, int):
            for s in range(rnge):
                if class_use == 'MAGIC-USER':
                    ispell = magicuser_choice(rnge)
                elif class_use == 'ILLUSIONIST':
                    if rnge > 7:
                        rnge = 7
                    ispell = illusionist_choice(rnge)
                elif class_use == 'CLERIC':
                    ispell = cleric_choice(rnge)
                else:
                    ispell = druid_choice(rnge)
                individual_spells.append(ispell)
            else:
                individual_spells.append(rnge)


        details = str(no) + '-' + str(rnge) + '-' + class_use + '-' + str(individual_spells)
        if xp == -1:
            xp = 100 * no * rnge
            val = 3 * xp
        else:
            val = 3 * xp
        
        choice = (details, xp, val)

    elif roll <= 40:
        item = "Rings (C.)"
        choice = ring_choice()
    elif roll <= 45:
        item = "Rods, Staves & Wands (D.)"
        choice = wand_choice()
    elif roll <= 48:
        item = "Miscellaneous Magic (E.1.)"
        choice = misc_1_choice()
    elif roll <= 51:
        item = "Miscellaneous Magic (E.2.)"
        choice = misc_2_choice()
    elif roll <= 54:
        item = "Miscellaneous Magic (E.3.)"
        choice = misc_3_choice()
    elif roll <= 57:
        item = "Miscellaneous Magic (E.4.)"
        choice = misc_4_choice()
    elif roll <= 60:
        item = "Miscellaneous Magic (E.5.)"
        choice = misc_5_choice()
    elif roll <= 75:
        item = "Armor & Shields (F.)"
        choice = armour_choice()
    elif roll <= 86:
        item = "Swords (G.)"
        choice = sword_choice()
    else:
        item = "Miscellaneous Weapons (H.)"
        choice = weapon_choice()
    return item, choice

def misc_5_choice_test(roll):
    #roll = roll_dice(1, 100)
    if roll <= 1:
        return ("Robe of the Archmagi", 6000, 65000)
    elif roll <= 8:
        return ("Robe of Blending", 3500, 35000)
    elif roll == 9:
        return ("Robe of Eyes", 4500, 50000)
    elif roll == 10:
        return ("Robe of Powerlessness", 0, 1000)
    elif roll == 11:
        return ("Robe of Scintillating Colors", 2750, 25000)
    elif roll <= 19:
        return ("Robe of Useful Items", 1500, 15000)
    elif roll <= 25:
        return ("Rope of Climbing", 1000, 10000)
    elif roll <= 27:
        return ("Rope of Constriction", 0, 1000)
    elif roll <= 31:
        return ("Rope of Entanglement", 1250, 12000)
    elif roll == 32:
        return ("Rug of Smothering", 0, 1500)
    elif roll == 33:
        return ("Rug of Welcome", 6500, 45000)
    elif roll == 34:
        return ("Saw of Mighty Cutting", 1750, 12500)
    elif roll == 35:
        return ("Scarab of Death", 0, 2500)
    elif roll <= 38:
        return ("Scarab of Enraging Enemies", 1000, 8000)
    elif roll <= 40:
        return ("Scarab of Insanity", 1500, 11000)
    elif roll <= 46:
        return ("Scarab of Protection", 2500, 25000)
    elif roll == 47:
        return ("Spade of Colossal Excavation", 1000, 6500)
    elif roll == 48:
        return ("Sphere of Annihilation", 3750, 30000)
    elif roll <= 50:
        return ("Stone of Controlling Earth Elementals", 1500, 12500)
    elif roll <= 52:
        return ("Stone of Good Luck (Luckstone)", 3000, 25000)
    elif roll <= 54:
        return ("Stone of Weight (Loadstone)", 0, 1000)
    elif roll <= 57:
        return ("Talisman of Pure Good", 3500, 27500)
    elif roll == 58:
        return ("Talisman of the Sphere", 100, 10000)
    elif roll <= 60:
        return ("Talisman of Ultimate Evil", 3500, 32500)        
    elif roll <= 66:
        return ("Talisman of Zagy", 1000, 10000)
    elif roll == 67:
        return ("Tome of Clear Thought", 8000, 48000)
    elif roll == 68:
        return ("Tome of Leadership and Influence", 7500, 40000)
    elif roll == 69:
        return ("Tome of Understanding", 8000, 43500)
    elif roll <= 76:
        return ("Trident of Fish Command (C F T)", 500, 4000)
    elif roll <= 78:
        return ("Trident of Submission (F)", 1250, 12500)
    elif roll <= 83:
        return ("Trident of Warning (C F T)", 1000, 10000)
    elif roll <= 85:
        return ("Trident of Yearning", 0, 1000)
    elif roll <= 87:
        return ("Vacuous Grimoire", 0, 1000)
    elif roll <= 90:
        return ("Well of Many Worlds", 6000, 12000)
    else:
        return ("Wings of Flying", 750, 7500)        

def misc_3_choice_test(roll):
    #roll = random.randint(1, 100)
    if roll <= 15:
        return ("Figurine of Wondrous Power", 100, 1000)
    elif roll <= 16:
        return ("Flask of Curses", 0, 1000)
    elif roll <= 18:
        return ("Gauntlets of Dexterity", 1000, 10000)
    elif roll <= 20:
        return ("Gauntlets of Fumbling", 0, 1000)
    elif roll <= 22:
        return ("Gauntlets of Ogre Power", 1000, 15000)
    elif roll <= 25:
        return ("Gauntlets of Swimming and Climbing", 1000, 10000)
    elif roll <= 26:
        return ("Gem of Brightness", 2000, 17500)
    elif roll <= 27:
        return ("Gem of Seeing", 2000, 25000)
    elif roll <= 28:
        return ("Girdle of Femininity-Masculinity", 0, 1000)
    elif roll <= 29:
        return ("Girdle of Giant Strength", 200, 2500)
    elif roll <= 30:
        return ("Helm of Brilliance", 2500, 60000)
    elif roll <= 35:
        return ("Helm of Comprehending Languages and Reading Magic", 1000, 12500)
    elif roll <= 37:
        return ("Helm of Opposite Alignment", 0, 1000)
    elif roll <= 39:
        return ("Helm of Telepathy", 3000, 35000)
    elif roll <= 40:
        return ("Helm of Teleportation", 2500, 30000)
    elif roll <= 45:
        return ("Helm of Underwater Action", 1000, 10000)
    elif roll <= 46:
        return ("Horn of Blasting", 5000, 55000)
    elif roll <= 48:
        return ("Horn of Bubbles", 0, 0)
    elif roll <= 49:
        return ("Horn of Collapsing", 1500, 25000)
    elif roll <= 53:
        return ("Horn of the Tritons", 2000, 17500)
    elif roll <= 60:
        return ("Horn of Valhalla", 1000, 15000)
    elif roll <= 63:
        return ("Horseshoes of Speed", 2000, 10000)
    elif roll <= 65:
        return ("Horseshoes of a Zephyr", 1500, 7500)
    elif roll <= 70:
        return ("Incense of Meditation", 500, 7500)
    elif roll <= 71:
        return ("Incense of Obsession", 0, 500)    
    elif roll <= 72:
        return ("Ioun Stones", 300, 5000)
    elif roll <= 78:
        return ("Instrument of the Bards", 1000, 5000)
    elif roll <= 80:
        return ("Iron Flask", 0, 0)
    elif roll <= 85:
        return ("Javelin of Lightning (F)", 250, 3000)
    elif roll <= 90:
        return ("Javelin of Piercing (F)", 250, 3000)
    elif roll <= 91:
        return ("Jewel of Attacks", 0, 1000)
    elif roll <= 92:
        return ("Jewel of Flawlessness", 0, "1000")
    else:
        return ("Keoghtoms Ointment", 500, 10000)        


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

    potion_name, xp, val,  = potion_choice()
    print(f"Potion: {potion_name}, XP: {xp}, Gold: {val}")

    no, rnge, xp, class_use = scroll_choice()
    if xp == -1:
        xp = 100 * no * rnge
        val = 3 * xp
    else:
        val = 3 * xp

    print(f"Scroll Spells:{no}, Level:{rnge}, XP:{xp}, Gold:{val}, Class:{class_use}")

    no, xp, val = ring_choice()
    print(f"Rings:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = wand_choice()
    print(f"Wands:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = armour_choice()
    print(f"Armour:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = sword_choice()
    print(f"Sword:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = weapon_choice()
    print(f"Weapon:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = misc_1_choice()
    print(f"Misc 1:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = misc_2_choice()
    print(f"Misc 2:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = misc_3_choice()
    print(f"Misc 3:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = misc_4_choice()
    print(f"Misc 4:{no}, XP:{xp}, Gold:{val}")

    no, xp, val = misc_5_choice()
    print(f"Misc 5:{no}, XP:{xp}, Gold:{val}")

    item, choice = select_magic_item()
    print(f"Magic:{item}, Choice:{choice}")

    alphabet_capitalised = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for a in alphabet_capitalised:
        choice = treasure_choice(a, roll_dice(1,6))  #random no appearing
        print(f"Treasure:{a}, Choice:{choice}, Length:{len(choice)}")

    for d in range(100):
        print(d+1)
        test = misc_5_choice_test(d+1) 
        if len(test) < 3:
            print("BAD:", test)
        print(test)

    for d in range(100):
        print(d+1)
        test = misc_3_choice_test(d+1) 
        if len(test) < 3:
            print("BAD:", test)
        print(test)

    print(jewellery_type())