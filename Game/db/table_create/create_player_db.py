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

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE team_data (id serial PRIMARY KEY, name char(10), unity decimal, map_skill decimal,\
      expenses decimal, strat decimal, manager_id serial, FOREIGN KEY (manager_id) references manager_data(id));")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close() 