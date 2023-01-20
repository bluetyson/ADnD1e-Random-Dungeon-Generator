## Advanced Dungeons & Dragons style random dungeon generator
Convert DMG tables to code to do for wandering around and down to make a dungeon.

# Environment
- Only non-standard type library used is numpy

# Running

- So converting to something else will just need something that can do char/string arrays
- At the moment it is just run for a number of 'rolls' - PERIODIC CHECK can set in code
  - or overide on command line to do 3 rolls for example:
  ```python
  python dungeon.py 3
  ```

# Work in progress
Building things as I go - just using a one roll test for now to see how it goes.
- Generates some monsters now
- Generates treasures in rooms
- Rolls for gems and jewellery
- Have not checked wandering monsters for treasure or implemented treasure tables
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
- Adventuring parties at lower levels with henchpeople
monster:{'level': 9, 'type': {1: {'class': 'CLERIC', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 JAVELIN +2'], ['1 MACE +1'], ['1 SCROLL: protection from magic'], ['1 SWORD: +3 (no special abilities)'], ['1 FIGURINE OF WONDROUS POWER: serpentine owl']]}, 2: {'class': 'BARD', 'level': 9, 'race': 'Elf', 'multi': 'Y', 'multi_no': 3, 'magic_items': [['1 SCROLL: protection from magic'], ['2 POTIONS: super-heroism, animal control'], ['2 POTIONS: extra-healing, polymorph (self)'], ['1 SCROLL: 3 Spells, level 2-9 or 2-7'], ['1 bracers of defense, armor class 4']]}, 3: {'class': 'CLERIC', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 MACE +1'], ['1 RING: protection +1'], ['4 BOLTS: +2'], ['1 WAND: illusion'], ['1 RING: protection +3']]}, 4: {'class': 'FIGHTER', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 SWORD: +4, defender']]}, 5: {'class': 'MAGIC-USER', 'level': 9, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 JAVELIN +2'], ['1 RING: protection +1'], ['10 ARROWS: +1'], ['2 WEAPONS: crossbow of speed, hammer +2'], ['1 bracers of defense, armor class 4'], ['1 pipe of the sewers']]}, 6: {'class': 'CLERIC', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': [['3 javelins of lightning']]}, 7: {'class': 'FIGHTER', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': []}, 8: {'class': 'MAGIC-USER', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': []}, 9: {'class': 'FIGHTER', 'level': 3, 'race': 'Human', 'multi': 'N', 'magic_items': [['1 SCROLL: 1 Spell, level 1-6'], ['2 POTIONS: human control, levitation']]}}, 'No': 9, 'XP': 0}
treasure:{'type': {'copper': 25300, 'silver': 0, 'electrum': 0, 'gold': 0, 'platinum': 0, 'gems': 0, 'jewellery': 0, 'magic': 0}, 'gems_list': [], 'jewellery_list': [], 'magic_list': [], 'magic_xp': [], 'magic_values': [], 'store': 'Sacks', 'protection': 'hide', 'hide': 'Secret: Disguised as other'}
```
- No retracing steps logic as yet for dead ends to block etc.
- See issues for things to do [lots of minor things]

# Bugs
- Will be quite a few I imagine

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
    
