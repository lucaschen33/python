from constants import *
from mysql import connector as c 


con = c.connect(host=host_name, user=user_name, password=user_pass, database=db_name)
# to search single player
def seachPlayer(firstname:any):
    con.connect()
    cursor = con.cursor()
    seachPlayer =queryone +"'" + lookup +"'"
    cursor.execute(seachPlayer)
    records = cursor.fetchall()
    if records:
        for row in records:
            print(row)       
    else:
        print("Player not found")
    cursor.close()
    con.close()


#add players

def addplayers(first_name, last_name, playernumber, points):
  con.connect()
  cursor = con.cursor()
  print(first_name, last_name, playernumber, points)
  adduser = "INSERT INTO jamie23to24 (first_name, last_name, playernumber, points) VALUES (%s,%s,%s,%s)"
  val = (first_name, last_name, playernumber, points)
  cursor.execute(adduser, val)
  con.commit()
  con.close()
  

# delete players

def deleteplayers():
  con.connect()
  cursor = con.cursor()
  deleteuser = "delete from jamie23to24 where id = %s"
  deleteval =(deleteid,)
  cursor.execute(deleteuser, deleteval)
  con.commit()
  con.close()
  



# to list all players
def listAllPlayers():
 con.connect()
 cursor = con.cursor()
 cursor.execute(queryall)
 records = cursor.fetchall()
 if records:
    for row in records:
        print(row)       
 else:
    print("Team dismissed!")
 cursor.close()
 con.close()




i  = 1
while (i < 6):
  print("1. List all players")
  print("2. Lookup a player")
  print("3. Add a player")
  print("4. Exit")
  print("5. Delete a player")
  print("6. List players by highest to lowest amount of points")
  select = input("Please select a number corosponding to your selection:")
  if select == '1':
    listAllPlayers()


  elif select == '2':
    lookup = input("Enter the person you want to lookup:  ")
    seachPlayer(lookup)
    
  elif select == '3':
      firstname = input("What is the first name?")
      lastname = input("What is the last name?")
      playernumber = input("What is the player number?")
      points = input("How many points did they score?")
      addplayers(firstname,lastname,playernumber,points)
      print("\n")
      print("record added successfully")
      print("\n")
  elif select == '4':
    i=6
    con.close()
    
  elif select == '5':
      deleteid = input("What is the player id of the player you would like to delete?")
      deleteplayers()

# TASK 1, Use a loop to keep this program running, until user pick exit
# TASK 2, let User to add new player to database

# Assignment weekend Nov 25-26
# TASK 3. New function to delete player
# TASK 4. List playr by POINTs rank 