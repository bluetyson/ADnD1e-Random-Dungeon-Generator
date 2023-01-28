import random
import sys

v = 0

def roll_dice(number, sides):
    roll = random.randint(number,sides)
    return roll

def dungeon_dressing():
    ac = roll_dice(1,100)
    air_currents = {
        5: "breeze, slight",
        10: "breeze, slight, damp",
        12: "breeze, gusting",
        18: "cold current",
        20: "downdraft, slight",
        22: "downdraft, strong",
        69: "still",
        75: "still, very chill",
        85: "still, warm (or hot)",
        87: "updraft, slight",
        89: "updraft, strong",
        93: "wind, strong",
        95: "wind, strong, gusting",
        100: "wind, strong, moaning"
    }

    o = roll_dice(1,100)
    odors = {
        3: "acrid smell",
        5: "chlorine smell",
        39: "dank, mouldy smell",
        49: "earthy smell",
        57: "manure smell",
        61: "metallic smell",
        65: "ozone smell",
        70: "putrid smell",
        75: "rotting vegetation smell",
        77: "salty, wet smell",
        82: "smoky smell",
        89: "stale, fetid smell",
        95: "sulphurous smell",
        100: "urine smell"
    }

    a = roll_dice(1,100)
    air = {
        70: "clear",
        80: "foggy (or steamy)",
        88: "foggy near floor (or steamy)",
        90: "hazy (dust)",
        98: "hazy (smoke)",
        100: "misted"
    }

    g = roll_dice(1,100)
    general = {
        1: "arrow, broken",
        2: "ashes",
        3: "ashes",
        4: "ashes",
        5: "bones",
        6: "bones",
        7: "bottle, broken",
        8: "chain, corroded",
        9: "club, splintered",
        10: "cobwebs",
        11: "cobwebs",
        12: "cobwebs",
        13: "cobwebs",
        14: "cobwebs",
        15: "cobwebs",
        16: "cobwebs",
        17: "cobwebs",
        18: "cobwebs",
        19: "cobwebs",
        20: "coin, copper (bent)",
        21: "cracks, ceiling",
        22: "cracks, ceiling",
        23: "cracks, floor",
        24: "cracks, floor",
        25: "cracks, wall",
        26: "cracks, wall",
        27: "dagger hilt",
        28: "dampness, ceiling",
        29: "dampness, ceiling",
        30: "dampness, wall",
        31: "dampness, wall",
        32: "dampness, wall",
        33: "dampness, wall",
        34: "dripping",
        35: "dripping",
        36: "dripping",
        37: "dripping",
        38: "dripping",
        39: "dripping",
        40: "dripping",
        41: "dried blood",
        42: "dung",
        43: "dung",
        44: "dung",
        45: "dust",
        46: "dust",
        47: "dust",
        48: "dust",
        49: "dust",
        50: "flask, cracked",
        51: "food scraps",
        52: "fungi, common",
        53: "guano",
        54: "guano",
        55: "guano",
        56: "hair or fur bits",
        57: "hammer head, cracked",
        58: "helmet, badly dented",
        59: "iron bar, bent, rusted",
        60: "javelin head, blunt",
        61: "leather boot",
        62: "leaves (dry) & twigs",
        63: "leaves (dry) & twigs",
        64: "leaves (dry) & twigs",
        65: "mold (common)",
        66: "mold (common)",
        67: "mold (common)",
        68: "mold (common)",
        69: "pick handle",
        70: "pole, broken (5foot)",
        71: "pottery shards",
        72: "rags",
        73: "rags",
        74: "rope, rotten",
        75: "rubble & dirt",
        76: "rubble & dirt",
        77: "sack, torn",
        78: "slimy coating, ceiling",
        79: "slimy coating, floor", 
        80: "slimy coating, wall", 
        81: "spike, rusted", 
        83: "sticks", 
        84: "stones, small", 
        85: "straw", 
        86: "sword blade, broken", 
        87: "teeth/fangs, scattered", 
        88: "torch stub", 
        89: "wall scratchings", 
        91: "water, small puddle", 
        93: "water, large puddle", 
        95: "water, trickle", 
        96: "wax drippings", 
        97: "wax blob (candle stub)", 
        100: "wood pieces, rotting"        

    }

    dressing_list = [air_currents, odors, air, general]
    roll_list = [ac, o, a, g]
    dressing_result = []
    for i, d in enumerate(dressing_list):
        for key in d:
            if roll_list[i] <= key:
                dressing_result.append(d[key])
                break

    return dressing_result


if __name__ == "__main__":
    ARGV = sys.argv

    print(dungeon_dressing())
