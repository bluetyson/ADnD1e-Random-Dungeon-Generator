
def monster_subtables_wet(m_dict, wet_dict)

    if 'HumanSubtable' in m_dict['name']:
        wet_dict['monster_details']['type'] = m_dict['details'][0]
        wet_dict['monster_details']['No'] = m_dict['details'][1]

        if 'Character' in m_dict['details']:
            wet_dict['monster_details']['type']  = m_dict['details']
            wet_dict['monster_details']['No'] = 9
            wet_dict['monster_details']['lair'] = '0%'
            wet_dict['monster_details']['treasure_individual'] = []
            wet_dict['monster_details']['treasure_lair'] = []
        else:
            m_data = human_d['human-' + m_dict['details'][0].lower()]                
            wet_dict['monster_details']['XP'] = m_data['XPtotal']
            wet_dict['monster_details']['lair'] = m_data['lair']
            wet_dict['monster_details']['treasure_individual'] = m_data['treasure_individual']
            wet_dict['monster_details']['treasure_lair'] = m_data['treasure_lair']

    elif 'CharacterSubtable' in m_dict['name']:
        wet_dict['monster_details']['type']  = m_dict['details']
        wet_dict['monster_details']['No'] = 9
        wet_dict['monster_details']['lair'] = '0%'
        wet_dict['monster_details']['treasure_individual'] = []
        wet_dict['monster_details']['treasure_lair'] = []

    #elif 'DragonSubtable' in m_dict['name']:
    elif 'Dragon' in m_dict['name']:            
        wet_dict['monster_details']['type']  = m_dict['details']['name']
        wet_dict['monster_details']['No'] = int(m_dict['no'][0])

        dname = m_dict['name'].split(':')[0]
        
        m_data = dragon_d[dname.replace('Dragon-','')]
        if VERBOSITY:
            print("Dragon dname", dname)
            print("Dragon M Data", m_data)
        wet_dict['monster_details']['lair'] = m_data['lair']
        wet_dict['monster_details']['treasure_individual'] = m_data['treasure_individual']
        wet_dict['monster_details']['treasure_lair'] = m_data['treasure_lair']
        wet_dict['monster_details']['XP'] = xp_d[wet_dict['monster_details']['level']]

    else:
        ##monsters
        if 'NO-ENCOUNTER' not in wet_dict['monster_details']['type']:
            m_data = all_d[wet_dict['monster_details']['type'].lower()]
            if VERBOSITY:
                print(m_data)
            wet_dict['monster_details']['XP'] = m_data['XPtotal']
            wet_dict['monster_details']['lair'] = m_data['lair']
            wet_dict['monster_details']['treasure_individual'] = m_data['treasure_individual']
            wet_dict['monster_details']['treasure_lair'] = m_data['treasure_lair']
        else: #dummy, nothing of interest
            wet_dict['monster_details']['lair'] = '0%'
            wet_dict['monster_details']['treasure_individual'] = []
            wet_dict['monster_details']['treasure_lair'] = []

    if VERBOSITY:
        print("CHECKSD FOR MONSTER CHARACTERS AFTER:",wet_dict['monster_details']['level'])
        print("CHECKSD FOR MONSTER CHARACTERS AFTER:",wet_dict['monster_details']['type'])

    return wet_dict
