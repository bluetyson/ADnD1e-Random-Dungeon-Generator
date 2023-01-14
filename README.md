# ADnD1e-Random-Dungeon-Generator
Attempt to convert DMG tables to code to do something

# Work in progress
Building things as I go - just using a one roll test for now to see how it goes.
- No retracing steps logic as yet for dead ends to block etc.
- See issues for things to do [lots]
- No random monster, treasure, magic item tables as yet, hence no stocking output keys printed

# Bugs
- Will be quite a few I imagine
- Basically output stops currently if it 'won't fit' and above comments are still valid

# Output to screen for checking purposes
- Makes a basic html map for a level in dungeon_1.html
  - if there are other levels, dungeon_2.html etc.
  - number the rooms basically

- the current legend, in code
- these get concatenated to the base type, C, R, D
- treasure gets some color coding

```python
legend_dict['O'] = "Outside Entrance"
legend_dict['C'] = "Corridor/Passage"
legend_dict['R'] = "Chamber/Room"
legend_dict['D'] = "Dead End"
legend_dict['wm'] = "Wandering Monster"
legend_dict['sd'] = "Secret Door"
legend_dict['st'] = "Stairs"
legend_dict['ch'] = "Chute"
legend_dict['cm'] = "Chimney"
legend_dict['td'] = "Trapdoor"
legend_dict['pi'] = "Pit Trap"
legend_dict['ps'] = "Pit Trap with Spikes"
legend_dict['pc'] = "Pit Trap with Crushing Walls"
legend_dict['el'] = "Elevator Trap"
legend_dict['ar'] = "Arrow Trap"
legend_dict['sp'] = "Spear Trap"
legend_dict['df'] = "Door Falls"
legend_dict['sf'] = "Stone Falls"
legend_dict['gs'] = "Gas Trap"
legend_dict['bw'] = "Blocked Wall"
legend_dict['ol'] = "Oil"
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
    
