import psycopg2
from Player import Player
#Connect to an existing database
conn = psycopg2.connect("dbname=majortactics user=postgres password=sifra ")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE player_data (id serial PRIMARY KEY, talent decimal, map_skill decimal, weapon_skill decimal, utility_usage decimal, game_sense decimal, communication decimal, mood decimal, motivation decimal, alive boolean, nationality char(10), name char(10), surname char(10), age integer, cost decimal);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
t1=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Dami", "Kodan",25,10)
t2=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Veseli", "Ghost",24,10)
t3=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Suki", "Ljuba",24,10)
t4=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Dzoni", "Panzer",24,10)
t5=Player(0.8, 0.8, 0.8, 0.8, 0.82, 0.81, 0.82, 0.86, True, "Srbija", "Sile", "Gile",24,10)
t=[t1,t2,t3,t4,t5]
for p in t:
    cur.execute("INSERT INTO player_data (talent, map_skill, weapon_skill, utility_usage, game_sense, communication, mood, motivation, alive, nationality, name, surname, age, cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(p.talent, p.map_skill, p.weapon_skill, p.utility_usage, p.game_sense, p.communication, p.mood, p.motivation, p.alive, p.nationality, p.name, p.surname, p.age, p.cost))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM player_data;")
cur.fetchone()
#(1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()