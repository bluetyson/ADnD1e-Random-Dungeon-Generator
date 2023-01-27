## Advanced Dungeons & Dragons style random dungeon generator
Convert DMG tables to code to do for wandering around and down to make a dungeon.

- Version 0.60
- See blog for more examples and notes as it was worked on https://cosmicheroes.space/blog/index.php/tag/random-dungeon-generator/

# Setup
- simulation is a current dev branch

# Environment
- Only non-standard type libraries used are numpy and pandas [the latter to do dungeon accounting csv, not necessary for dungeon generation]

# Binder
- click the below to fire up a web container environment that lets you run this in your browser
- you get jupyterlab, just click on the terminal link at the lower left and then type 'python dungeon.py 1' [or however many rolls as you like] and the files created will also be in the main directory, one for each dungeon level.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bluetyson/ADnD1e-Random-Dungeon-Generator/HEAD)

# Running

- So converting to something else will just need something that can do char/string arrays
- At the moment it is just run for a number of 'rolls' - PERIODIC CHECK can set in code
  - or overide on command line to do 3 rolls for example:
  ```python
  python dungeon.py 3
  ```

# Work in progress
Building things as I go - just using a one roll test for now to see how it goes.
- Generates monsters in rooms
- Generates treasures in rooms
- Rolls for gems and jewellery
- Generates an in lair roll
- Generates basic individual treasure
- Does dungeon accounting  - adds up treasure and some XP metrics and traps, wet monsters
    - Outputs this to a csv when run
- Links to each level are at the bottom of each Dungeon Level html page
```python
Monster Total XP:71798

Monster Total Treasure:{'copper': 6000, 'silver': 6000, 'electrum': 42558, 'gold': 53794, 'platinum': 29000, 'gems': 29, 'jewellery': 12, 'magic': 0}

Monster Total Valuations:{'gems': [110.0, 800.0, 5.0, 12.0, 500, 16.0, 500, 1000, 120.0, 20, 100, 25.0, 50, 120.0, 8.0, 14.0, 1000, 20, 110.0, 800.0, 5.0, 12.0, 500, 16.0, 500, 1000, 120.0, 20, 100, 25.0, 50, 120.0, 8.0, 14.0, 1000, 20, 10, 65.0, 100, 100, 5.0, 2000, 200, 50, 50, 500, 90.0, 10, 65.0, 100, 100, 5.0, 2000, 200, 50, 50, 500, 90.0], 'jewellery': [4000, 6000, 300, 1000, 4000, 1200, 4000, 500, 4000, 1600, 900, 9000], 'magic': [], 'magic_xp': [], 'magic_values': [], 'magic_list': []}

Wandering Monster Total XP:829030

Wandering Monster Total Treasure:{'copper': 427, 'silver': 234, 'electrum': 0, 'gold': 733, 'platinum': 42, 'gems': 35, 'jewellery': 0, 'magic': 0}

Wandering Monster Subtable:['monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'human', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'character', 'monster', 'monster', 'monster', 'monster', 'dragon', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'character', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'dragon', 'character', 'monster', 'monster', 'dragon', 'dragon', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'character', 'monster', 'monster', 'monster', 'monster', 'dragon', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'character', 'character', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'dragon', 'character', 'monster', 'monster', 'dragon', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'monster', 'character', 'monster', 'monster', 'monster', 'dragon', 'monster', 'monster', 'monster', 'character', 'monster', 'monster']

Room Total Treasure:{'copper': 132200, 'silver': 65400, 'electrum': 48525, 'gold': 15750, 'platinum': 3030, 'gems': 33, 'jewellery': 0, 'magic': 3}

Room Total Gems:5453.0

Room Total Jewellery:0

Room Total Magic:20400
Total Treasure: {'copper': 138627, 'silver': 71634, 'electrum': 91083, 'gold': 70277, 'platinum': 32072, 'gems': 97, 'jewellery': 12, 'magic': 3}
Coins: 445088.17
Gems: 20633.0
Jewellery: 15180.0
Magic: 20400
Total Gold Equivalent: 501301.17
```

- Does basic Human and Character subtables (for running into adventuring parties)
```python
1 : {'class': 'THIEF', 'level': '1', 'race': 'Human', 'multi': 'N', 'magic_items': []}
2 : {'class': 'FIGHTER', 'level': '1', 'race': 'Gnome', 'multi': 'N', 'magic_items': []}
3 : {'class': 'woman-at-arms/henchwoman'}
4 : {'class': 'woman-at-arms/henchwoman'}
5 : {'class': 'man-at-arms/henchman'}
6 : {'class': 'man-at-arms/henchman'}
7 : {'class': 'woman-at-arms/henchwoman'}
8 : {'class': 'woman-at-arms/henchwoman'}
9 : {'class': 'man-at-arms/henchman'}
 ```
- Dragons
```python
monster:{'level': 10, 'type': 'Dragon-Copper:2', 'No': '2-2', 'XP': 0}
treasure:{'type': {'copper': 23100, 'silver': 0, 'electrum': 0, 'gold': 0, 'platinum': 0, 'gems': 0, 'jewellery': 0, 'magic': 0}, 'gems_list': [], 'jewellery_list': [], 'magic_list': [], 'magic_xp': [], 'magic_values': [], 'store': 'Bloody Great Chests', 'protection': 'guard', 'guard': 'Blade: across inside'}
```
- They are given a basic set XP value.  Have not found a table where someone has worked out every age combination and XP as yet.
- Same goes for generic adventuring parties.

- Adventuring parties at lower levels with henchpeople
```python
monster:{'level': 9, 'type': {1: {'class': 'CLERIC', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 JAVELIN +2'], ['1 MACE +1'], ['1 SCROLL: protection from magic'], ['1 SWORD: +3 (no special abilities)'], ['1 FIGURINE OF WONDROUS POWER: serpentine owl']]}, 2: {'class': 'BARD', 'level': 9, 'race': 'Elf', 'multi': 'Y', 'multi_no': 3, 'magic_items': [['1 SCROLL: protection from magic'], ['2 POTIONS: super-heroism, animal control'], ['2 POTIONS: extra-healing, polymorph (self)'], ['1 SCROLL: 3 Spells, level 2-9 or 2-7'], ['1 bracers of defense, armor class 4']]}, 3: {'class': 'CLERIC', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 MACE +1'], ['1 RING: protection +1'], ['4 BOLTS: +2'], ['1 WAND: illusion'], ['1 RING: protection +3']]}, 4: {'class': 'FIGHTER', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 SWORD: +4, defender']]}, 5: {'class': 'MAGIC-USER', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 JAVELIN +2'], ['1 RING: protection +1'], ['10 ARROWS: +1'], ['2 WEAPONS: crossbow of speed, hammer +2'], ['1 bracers of defense, armor class 4'], ['1 pipe of the sewers']]}, 6: {'class': 'CLERIC', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': [['3 javelins of lightning']]}, 7: {'class': 'FIGHTER', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': []}, 8: {'class': 'MAGIC-USER', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': []}, 9: {'class': 'FIGHTER', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 SCROLL: 1 Spell, level 1-6'], ['2 POTIONS: human control, levitation']]}}, 'No': 9, 'XP': 0}
treasure:{'type': {'copper': 25300, 'silver': 0, 'electrum': 0, 'gold': 0, 'platinum': 0, 'gems': 0, 'jewellery': 0, 'magic': 0}, 'gems_list': [], 'jewellery_list': [], 'magic_list': [], 'magic_xp': [], 'magic_values': [], 'store': 'Sacks', 'protection': 'hide', 'hide': 'Secret: Disguised as other'}
```
- No retracing steps logic as yet for dead ends to block etc.
- See issues for things to do [lots of minor things]

# Bugs
- Will be quite a few I imagine, mostly minor or things to do with set facings or placements.  
- Most of the data should be ok now.

# Output to screen for checking purposes
- Makes a basic html map for a level in dungeon_1.html
  - if there are other levels, dungeon_2.html etc.
  - number the rooms basically

- the current legend, in code
- these get concatenated to the base type, C, R, D
- treasure gets some color coding
- outputs room data 
- outputs relevant room key
- gives a treasure total accounting at the end

```python
legend_dict['O'] = "Outside Entrance"
legend_dict['C'] = "Corridor/Passage"
legend_dict['R'] = "Chamber/Room"
legend_dict['D'] = "Dead End"
legend_dict['CH'] = "Chasm"
legend_dict['ri'] = "river"
legend_dict['br'] = "bridge"
legend_dict['bo'] = "boat - opposide side"
legend_dict['bn'] = "boat - near side"
legend_dict['L'] = "Lake"
legend_dict['P'] = "Pool"
legend_dict['W'] = "Well"
legend_dict['S'] = "Shaft"
legend_dict['d'] = "door"
legend_dict[':'] = "direction of Door"
legend_dict['wm'] = "Wandering Monster"
legend_dict['sd'] = "Secret Door"
legend_dict['st'] = "Stairs"
legend_dict['ch'] = "Chute"
legend_dict['cm'] = "Chimney"
legend_dict['td'] = "Trapdoor"
legend_dict['pi'] = "Pit Trap"
legend_dict['pt'] = "Pit Trap: Secret Door"
legend_dict['ps'] = "Pit Trap: Spikes"
legend_dict['pc'] = "Pit Trap: Crushing Walls"
legend_dict['el'] = "Elevator Trap"
legend_dict['ar'] = "Arrow Trap"
legend_dict['sp'] = "Spear Trap"
legend_dict['df'] = "Door Falls Trap"
legend_dict['sf'] = "Stone Falls Trap"
legend_dict['gs'] = "Gas Trap"
legend_dict['bw'] = "Blocked Wall Trap"
legend_dict['ol'] = "Oil Trap"
legend_dict['m'] = "Monster"
legend_dict['t'] = "Treasure"
legend_dict['p'] = "Pool"
legend_dict['c'] = "Treasure: Copper"  
legend_dict['s'] = "Treasure: Silver"
legend_dict['e'] = "Treasure: Electrum"
legend_dict['g'] = "Treasure: Gold"
legend_dict['p'] = "Treasure: Platinum"
legend_dict['G'] = "Treasure: Gems"
legend_dict['j'] = "Treasure: Jewellery"
legend_dict['M'] = "Treasure: Magic"
```

# Example html testing output

## Level 1

![image](https://user-images.githubusercontent.com/17399794/212467844-2933241b-73ef-4efa-99be-d24a382b2ec9.png)

## Level 2
![image](https://user-images.githubusercontent.com/17399794/212469425-12962172-99a0-42aa-86eb-fd1f74040e39.png)

## Level 3
![image](https://user-images.githubusercontent.com/17399794/212469451-9bcc7095-c722-4601-83aa-86850dc57abb.png)

## Level 4
![image](https://user-images.githubusercontent.com/17399794/212469478-a6210c6b-66b6-4636-98f2-b827189c54d3.png)

###
Dungeon level html now include a basic key output dictionary
e.g. basically using this while I work on things:
Below is an example unrelated to above plots.

#### Key: 1
```python
Data: 23
{'shape': 'R', 'size': [1, 2], 'contents': {'monster': {'level': 8, 'type': 'Xorn', 'No': 5, 'XP': 0}, 'treasure': {'type': {'copper': 0, 'silver': 0, 'electrum': 0, 'gold': 2200, 'platinum': 0, 'gems': 0, 'jewellery': 0, 'magic': 0}, 'gems_list': [], 'jewellery_list': [], 'store': 'Sacks', 'protection': 'hide', 'hide': 'Secret: Loose stone - in wall'}, 'secret_door_dict': {}, 'secret_door_count': 0}, 'exits': 0, 'secretdoors': 'check', 'exitlocations': {}, 'exitdirections': {}}

Key: 23
monster:{'level': 8, 'type': 'Xorn', 'No': 5, 'XP': 0}
treasure:{'type': {'copper': 0, 'silver': 0, 'electrum': 0, 'gold': 2200, 'platinum': 0, 'gems': 0, 'jewellery': 0, 'magic': 0}, 'gems_list': [], 'jewellery_list': [], 'store': 'Sacks', 'protection': 'hide', 'hide': 'Secret: Loose stone - in wall'}
```


### Level 1 html example

    <html>
    <head>
    <title>DUNGEON</title>
    <style>
        table,
        th,
        td {
            padding: 10px;
            border: 1px solid black;
            border-collapse: collapse;
            width:auto
        }
        .red_background {
                background-color: red;
            }
        .green_background {
                background-color: green;
            }
        .gray_background {
                background-color: gray;
            }
        .grey_background {
                background-color: grey;
            }
        .brown_background {
                background-color: brown;
            }

        .blue_background {
                background-color: blue;
            }
        .black_background {
                background-color: black;
            }

        </style>
    </head>
    <body>
    <table>
    <TR><td class="black_background">B</td><td class="green_background">O</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="red_background">st</td><td class="black_background">B</td><td class="black_background">B</td><td class="red_background">cm</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR>
    </table>
    </body>
    </html>
    

## References
- dungeon mapping icons : https://savevsdragon.blogspot.com/2012/03/free-download-master-dungeon-mapping.html
- Monsters
- Treasure
- Spells
