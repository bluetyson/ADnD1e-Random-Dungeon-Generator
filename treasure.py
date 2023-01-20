import random
import sys

def testtreasure():
    return "Basic treasure goes in shape_dict for room! Not done random gems, jewellery, magic."

def roll_dice(number, sides):
    roll = roll_dice(number,sides)
    return roll

def select_gemstone():
    dice_roll = roll_dice(1, 100)
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


if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        character_level = ARGV[1]
    else:
        character_level = 1

    base_value, description = select_gemstone()
    print(f"The selected gemstone has a base value of {base_value} gold pieces and is described as {description}")

    new_base_value = update_gemstone(base_value)
    print(f"The upgrade value of the gemstone is {new_base_value} gold pieces.")

    #base_value, description = select_jewelry()
    #print(f"The selected jewelry has a base value of {base_value} gold pieces and is described as {description}")
