

wm_dict = monster_tables(wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['level'])

wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['type'] = wm_dict['name']
wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['No'] = wm_dict['no']
#wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['wm_dict'] = wm_dict

checkdragon = False

for cd in [r':young',r':sub',r':adult',r':old',r':very',r':ancient','Tiamat','Bahamut',':2-']:
    if cd in wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['type']:
        checkdragon = True
print("checking dragon", checkdragon)

#wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['checkdrg'] = checkdragon

if 'Subtable' not in wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['type']:
    if not checkdragon:
        print("WM_DATA1st NoSubtable - monster")
        #print(all_d)
        wm_data = all_d[wm_dict['name'].lower()]
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['XP'] = wm_data['XPtotal']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['lair'] = wm_data['lair']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_individual'] = wm_data['treasure_individual']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_lair'] = wm_data['treasure_lair']

        print("WM_DATA",wm_data)
        wandering_monster_subtable.append('monster')
        print("WM_DICTNAME",wm_dict['name'])
    else:
        print(wm_dict)
        print("DragonSubtable")
        print("DRAGON WM_DICT:",wm_dict)
        #type ok above already
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['No'] = int(wm_dict['no'][0])

        dname = wm_dict['details']['name'].split(':')[0]
        print("Dragon dname", dname)
        wm_data = dragon_d[dname]
        print("Dragon WM Data", wm_data)
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['lair'] = wm_data['lair']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_individual'] = wm_data['treasure_individual']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_lair'] = wm_data['treasure_lair']

        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['XP'] = xp_d[wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['level']]
        print("DragonSubtableWM:",wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord])
        wandering_monster_subtable.append('dragon')

if 'HumanSubtable' in wm_dict['name']:
    print("HumanSubtable from wm")
    wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['type'] = wm_dict['details'][0]
    wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['No'] = wm_dict['details'][1]

    if 'Character' not in wm_dict['details']:
        wm_data = human_d['human-' + wm_dict['details'][0].lower()]
        print("WM_DATA",wm_data)
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['XP'] = wm_data['XPtotal']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['lair'] = wm_data['lair']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_individual'] = wm_data['treasure_individual']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_lair'] = wm_data['treasure_lair']

        print("human subtable check wmdict details:",wm_dict['details'])
    if 'Character' in wm_dict['details']:
        print("HumanSubtable-Character - implementing")
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['type'] = wm_dict['details']
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['No'] = 9                

        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['lair'] = '0%'
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_individual'] = [] #have to work out
        wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_lair'] = [] #have to work out
        print(wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord])
        wandering_monster_subtable.append('human-character')
    else:
        print("HumanSubtable-second branch basic human")
        print("WM_DATA",wm_data)
        print(wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord])
        wandering_monster_subtable.append('human')
    print("IN HUMAN")

if 'CharacterSubtable' in wm_dict['name']:
    print("CharacterSubtable") #this works
    wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['type'] = wm_dict['details']
    wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['No'] = 9
    
    wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['lair'] = '0%'
    wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_individual'] = [] #have to work out
    wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord]['treasure_lair'] = [] #have to work out

    #print("character quitting")
    print("CharacterSubtableWM:", wandering_monster_stack[wandering_monster_stack['key_count']][wm_coord])
    wandering_monster_subtable.append('character')

