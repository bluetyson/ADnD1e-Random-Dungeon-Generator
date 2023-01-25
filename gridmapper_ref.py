import re, html

# Remove well-formed tags, fixing mistakes by legitimate users
legend_gridmapper =  {}
legend_gridmapper['B'] = "pVVVV"
legend_gridmapper['O'] = "Outside Entrance"
legend_gridmapper['C'] = "Corridor/Passage"
legend_gridmapper['R'] = "Chamber/Room"
legend_gridmapper['D'] = "Dead End"
legend_gridmapper['CH'] = "Chasm"
legend_gridmapper['ri'] = "river"
legend_gridmapper['br'] = "bridge"
legend_gridmapper['bo'] = "boat - opposide side"
legend_gridmapper['bn'] = "boat - near side"
legend_gridmapper['L'] = "Lake"
legend_gridmapper['P'] = "Pool"
legend_gridmapper['W'] = "Well"
legend_gridmapper['S'] = "Shaft"
legend_gridmapper['d'] = "door"
legend_gridmapper[':'] = "direction of Door"
legend_gridmapper['wm'] = "Wandering Monster"
legend_gridmapper['sd'] = "Secret Door"
legend_gridmapper['st'] = "Stairs"
legend_gridmapper['sn'] = "Stairs dead end"
legend_gridmapper['ch'] = "Chute"
legend_gridmapper['cm'] = "Chimney"
legend_gridmapper['td'] = "Trapdoor"
legend_gridmapper['pi'] = "Pit Trap"
legend_gridmapper['pt'] = "Pit Trap: Secret Door"
legend_gridmapper['ps'] = "Pit Trap: Spikes"
legend_gridmapper['pc'] = "Pit Trap: Crushing Walls"
legend_gridmapper['el'] = "Elevator Trap"
legend_gridmapper['ar'] = "Arrow Trap"
legend_gridmapper['sp'] = "Spear Trap"
legend_gridmapper['df'] = "Door Falls Trap"
legend_gridmapper['sf'] = "Stone Falls Trap"
legend_gridmapper['gs'] = "Gas Trap"
legend_gridmapper['bw'] = "Blocked Wall Trap"
legend_gridmapper['ol'] = "Oil Trap"
legend_gridmapper['m'] = "Monster"
legend_gridmapper['t'] = "Treasure"
legend_gridmapper['c'] = "Treasure: Copper"  
legend_gridmapper['s'] = "Treasure: Silver"
legend_gridmapper['e'] = "Treasure: Electrum"
legend_gridmapper['g'] = "Treasure: Gold"
legend_gridmapper['p'] = "Treasure: Platinum"
legend_gridmapper['G'] = "Treasure: Gems"
legend_gridmapper['j'] = "Treasure: Jewellery"
legend_gridmapper['M'] = "Treasure: Magic"

background_dict = {}
background_dict['black'] = 'nothing'
background_dict['green'] = 'outside entrance'
background_dict['blue'] = 'water'
background_dict['red'] = 'bad_things'
background_dict['white'] = 'corridor/passage'
background_dict['brown'] = 'dead end'

legend_gridmapper =  {}
for key in legend_gridmapper:
    legend_gridmapper[key] = ''

legend_gridmapper['B'] = "pvvvv"
legend_gridmapper['O'] = "m"
legend_gridmapper['C'] = "f"
legend_gridmapper['R'] = "fQ"
legend_gridmapper['D'] = "gS"
legend_gridmapper['CH'] = "n"
legend_gridmapper['ri'] = "fVVB"
legend_gridmapper['br'] = "bridge"
legend_gridmapper['bo'] = "boat - opposide side"
legend_gridmapper['bn'] = "boat - near side"
legend_gridmapper['L'] = "fvvD"
legend_gridmapper['P'] = "fvvB"
legend_gridmapper['W'] = "bvB"
legend_gridmapper['S'] = "bvv"
legend_gridmapper['d'] = "d"
legend_gridmapper[':'] = "direction of Door"
legend_gridmapper['wm'] = "fE"
legend_gridmapper['sd'] = "dv"
legend_gridmapper['st'] = "oE"
legend_gridmapper['sn'] = "ovE"
legend_gridmapper['ch'] = "Chute"
legend_gridmapper['cm'] = "Chimney"
legend_gridmapper['td'] = "tvvvE"
legend_gridmapper['pi'] = "tvE"
legend_gridmapper['pt'] = "tvE"
legend_gridmapper['ps'] = "tvE"
legend_gridmapper['pc'] = "tvE"
legend_gridmapper['el'] = "svE"
legend_gridmapper['ar'] = "tvvvvvvE"
legend_gridmapper['sp'] = "tvvvvvvE"
legend_gridmapper['df'] = "dvvvvvE"
legend_gridmapper['sf'] = "tvvvvvvE"
legend_gridmapper['gs'] = "tvvvvvvE"
legend_gridmapper['bw'] = "wE"
legend_gridmapper['ol'] = "tvvvvvvE"
legend_gridmapper['m'] = "fE"
legend_gridmapper['t'] = "cA"
legend_gridmapper['c'] = "cA"  
legend_gridmapper['s'] = "cA"
legend_gridmapper['e'] = "cA"
legend_gridmapper['g'] = "cA"
legend_gridmapper['p'] = "cA"
legend_gridmapper['G'] = "cA"
legend_gridmapper['j'] = "cA"
legend_gridmapper['M'] = "cA"

testt = '''<table><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="green_background">O</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td>C</td><td>C</td><td>C</td><td class="red_background">pt</td><td>C</td><td>C</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="red_background">wm</td><td class="gray_background">R2</td><td class="gray_background">R2</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="red_background">td</td><td class="gray_background" style="color:#FFD700">R2g</td><td class="gray_background">R2</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td>C</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR><TR><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td><td class="black_background">B</td></TR></table>'''
testt = testt.replace('<TR>','')
testt = testt.replace('<table>','')
testt = testt.replace(r'</table>','')
testlist = testt.split(r'</TR>')
print(testlist)

striplist = []
tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

if 1 == 1:
    #tag_re = re.compile(r'<[^>]+') 
    print(tag_re)
    #result = pattern.sub('',text)  
    for t in testlist:
        no_tags = tag_re.sub(' ', t)
        
        tag_list = no_tags.split()
        new_list = []
        for tl in tag_list:
            newtl = legend_gridmapper[tl]
            new_list.append(tol)
        
        striplist.append(new_list)

    print(striplist)