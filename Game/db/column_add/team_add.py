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

team_names=["Blue Kings", "Morbid", "Dove", "Striders", "Owls"\
            ,"Hax","Warriors", "Unicorns", "Metalheads", "Lars"]

conn = psycopg2.connect("dbname=majortactics user=postgres password="+os.getenv("PASSWORD"))

# Open a cursor to perform database operations
cur = conn.cursor()
    
for i in range(10):
    # Execute a commande
    cur.execute("INSERT INTO team_data (name, unity, map_skill, expenses, strat, manager_id) VALUES (%s, %s, %s, %s, %s, %s)",(team_names[i], 1,0,0,0,i+1))

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close() 