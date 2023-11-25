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
  select = input("Please select a number corosponding to your selection:")
  if select == '1':
    listAllPlayers()


  elif select == '2':
    lookup = input("Enter the person you want to lookup:  ")
    seachPlayer(lookup)
    
  elif select == '3':
      query3 = "insert into haltonstats (id, first_name, last_name, playernumber, points) values (11, 'jolie', 'chen', 13, 0);"
      print("\n")
      print("record added successfully")
      print("\n")
  elif select == '4':
    i=6
    con.close()

# TASK 1,  Use a loop to keep this program running, until user pick exit
# TASK 2,  let User to add new player to database