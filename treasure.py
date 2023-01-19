import random
import sys

def testtreasure():
    return "Basic treasure goes in shape_dict for room! Not done random gems, jewellery, magic."

def roll_dice(number, sides):
    roll = random.randint(number,sides)
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

base_value, description = select_gemstone()
print(f"The selected gemstone has a base value of {base_value} gold pieces and is described as {description}")

if __name__ == "__main__":
    ARGV = sys.argv

    if len(ARGV) > 1:
        character_level = ARGV[1]
    else:
        character_level = 1

base_value, description = select_gemstone()
print(f"The selected gemstone has a base value of {base_value} gold pieces and is described as {description}")


