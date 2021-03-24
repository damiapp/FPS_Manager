import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import psycopg2
import Player
import json

conn = psycopg2.connect("dbname=majortactics user=postgres password=sinisa71 ")

cur = conn.cursor()


with open('db/data.txt') as json_file:
    data = json.load(json_file)

for p in data['Players']:
    #if player exist then not insert Todo!
    cur.execute("INSERT INTO player_data (talent, map_skill, weapon_skill, utility_usage, game_sense, communication, mood, motivation, alive, nationality, name, surname, age, cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(p['talent'], p['map_skill'], p['weapon_skill'], p['utility_usage'], p['game_sense'], p['communication'], p['mood'], p['motivation'], p['alive'], p['nationality'], p['name'], p['surname'], p['age'], p['cost']))

# Query the database and obtain data as Python objects
#cur.execute("SELECT * FROM player_data;")
#cur.fetchone()

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()