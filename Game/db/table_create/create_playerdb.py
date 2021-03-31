import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


conn = psycopg2.connect("dbname=majortactics user=postgres password="+os.getenv("PASSWORD"))

cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE player_data (id serial PRIMARY KEY, talent decimal, map_skill decimal,\
     weapon_skill decimal, utility_usage decimal, game_sense decimal, communication decimal, mood decimal,\
          motivation decimal, alive boolean, nationality char(15), name char(20), surname char(20), age integer, \
              cost decimal,team_id serial, FOREIGN KEY (team_id) references team_data(id));")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
