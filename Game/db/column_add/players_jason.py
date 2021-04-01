import json
import names
import random
data = {}
data['Players'] = []

for i in range(50):
    data['Players'].append({
        'talent':random.uniform(0.5,1),
        'map_skill':random.uniform(0.5,1), 
        'weapon_skill':random.uniform(0.5,1),
        'utility_usage':random.uniform(0.5,1), 
        'game_sense':random.uniform(0.5,1), 
        'communication':random.uniform(0.5,1), 
        'mood':random.uniform(0.5,1), 
        'motivation':random.uniform(0.5,1), 
        'alive':True, 
        'nationality':'Serbia', 
        'name':names.get_first_name(gender="male"), 
        'surname':names.get_last_name(), 
        'age':random.randint(18,31),
        'cost':random.randint(100000,300000),
        'team':None
    })

with open("Game/db/column_add/data.txt", 'w') as outfile:
    json.dump(data, outfile)