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

def update_gemstone(base_value):
    dice_roll = roll_dice(1, 10)
    if dice_roll == 1:
        next_base_value = base_value * 2
        if next_base_value > 1000000:
            return 1000000
        return select_gemstone(next_base_value)
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

