# ADnD1e-Random-Dungeon-Generator
Attempt to convert DMG tables to code to do something

# Work in progress
Building things as I go - just using a one roll test for now to see how it goes.
- No retracing steps logic as yet for dead ends to block etc.
- See issues for things to do [lots]

# Output to screen for checking purposes
- Makes a basic html map for a level in dungeon_1.html
  - if there are other levels, dungeon_2.html etc.
  - number the rooms basically

# Bugs
- Will be quite a few I imagine
- Basically output stops currently if it 'won't fit' and above comments are still valid

# Example html testing output

## Level 1



    
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
    
