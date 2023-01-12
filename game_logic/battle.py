import sqlite3   #enable control of an sqlite database

DB_FILE="databases\data.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()   

# performs attack and calculates damage taken by defender
def atk (move, p1, p2):
    # command to select the description, damage, accuracy and turns of the move
    command0 = "SELECT description,damage,accuracy,turns FROM moves WHERE name = ?" (move) 
    data = c.execute(command0)
    print(data)
    # command to select the related attack of the attack of p1
    # command1 = "SELECT p_def,sp_def FROM pokemon WHERE name = 'p2'" 

    # command to select the related defence of the attack of p2
    # command2 = "SELECT p_def,sp_def FROM pokemon WHERE name = 'p2'" 

    # calculates if the attack succeeds
    
        # if true, calculates the damage taken by p2 and prints + returns the value

        # if false, prints + returns the damage taken   

    return(100)

# returns true if the mon is alive, false otherwise
def isAlive (mon, health):
    if (health <= 0):
        print(mon + " has fainted!")
        return False
    else:
        return True

# returns 0 if p1 is faster than p2, if equal random, else returns p2
def goesFirst(p1,p2):
    # command to retrieve speed of p1 
    # command0 = "SELECT speed FROM pokemon WHERE name = ''" 

    # command to retrieve speed of p2
    # command1 = "SELECT speed FROM pokemon WHERE name = ''" 

    # compares the speed of both mons
        # if (p1 > p2): return(0)

        # elif (p1 == p2): return(random.randint(0, 1))
        
        # else return(1) 
    print("def")


# returns 0 if move is not effective, 0.5 if move is less effective, 1 if normal effective, and 2 otherwise
def effective(typeM, typeP):
    print("effective")
