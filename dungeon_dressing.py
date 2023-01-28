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

    dressing_list = [air_currents, odors]
    roll_list = [ac, o]
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
