import psycopg2
import os
from dotenv import load_dotenv
import names
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
    
for i in range(10):
    # Execute a commande
    name=names.get_full_name()
    cur.execute("INSERT INTO manager_data (budget, expenses, name) VALUES (%s, %s, %s)",(100000,0,name))

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close() 