# converts information in databases/csv files to sqlite tables 

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="databases/data.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
print("sucessfully connected to sqlite")

#==========================================================

# CODE TO POPULATE THE pokemon db CONTAINING pokemon.csv DATA

c.execute('DROP TABLE IF EXISTS pokemon')
c.execute('''CREATE TABLE pokemon(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type1 TEXT,
    type2 TEXT,
    total INTEGER,
    health INTEGER,
    p_atk INTEGER,
    sp_atk INTEGER,
    p_def INTEGER,
    sp_def INTEGER,
    speed INTEGER)
    ''')
with open('databases/pokemon.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)
    for row in myCSVReader:
        name = row.get("Name")
        type1 = row.get("Type 1")
        type2 = row.get("Type 2")
        health = row.get("HP")
        p_atk = row.get("Attack")
        sp_atk = row.get("sp_atk")
        p_def = row.get("p_def")
        sp_def = row.get("sp_def")
        speed = row.get("speed")
        c.execute("INSERT INTO pokemon (name, type, health, p_atk, sp_atk, p_def, sp_def, speed) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
          (name, type, health, p_atk, sp_atk, p_def, sp_def, speed))

# CODE TO POPULATE THE moves db CONTAINING moves.csv DATA

c.execute('DROP TABLE IF EXISTS moves')
c.execute('''CREATE TABLE moves(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    description TEXT,
    damage INTEGER,
    accuracy INTEGER,
    turns INTEGER)
    ''')
with open('databases/moves.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)
    for row in myCSVReader:
        name = row.get("name")
        type = row.get("type")
        description = row.get("description")
        damage = row.get("damage")
        accuracy = row.get("accuracy")
        turns = row.get("turns")
        c.execute("INSERT INTO moves (name, type, description, damage, accuracy, turns) VALUES (?, ?, ?, ?, ?, ?)",
          (name, type, description, damage, accuracy, turns))

# CODE TO POPULATE THE types db CONTAINING types.csv DATA

c.execute('DROP TABLE IF EXISTS types')
c.execute('''CREATE TABLE types(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    weakAgainst TEXT,
    strongAgainst TEXT,
    notEffective TEXT)
    ''')
#==========================================================

#print the pokemon SQLite table
command = "SELECT * FROM pokemon;"
print("\n Pokemon:")
for row in c.execute(command):
    print(row)

#print the moves SQLite table
command = "SELECT * FROM moves;"
print("\n Moves:")
for row in c.execute(command):
    print(row)

db.commit() #save changes
db.close()
