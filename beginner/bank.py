class Checking_Account:
    def __init__(self, CheckingBalance, CheckingNumber,):
     self.CheckingBalance = CheckingBalance
     self.CheckingNumber = CheckingNumber

class Savings_Account:
    def __init__(self, SavingsBalance, SavingsNumber):
     self.SavingsBalance =float(SavingsBalance)
     self.SavingsNumber = SavingsNumber

class Userinfo:
   def __init__(self, username, password):
    self.username = username
    self.password = password

def savingsadd(x,y):
  return x+y

def checkingadd(x,y):
  return x+y
  
  
def savingsminus(x,y):
  return x-y

def checkingminus(x,y):
  return x-y

username = input("Enter your username: ")
password = input("Enter your password: ")
print("Username is now: " + username)
print("Password is now: " + password)




SavingsBalance = input("How much do you want to deposit in your savings account? ")
CheckingBalance = input("How much do you want to deposit in your checkings account? ")
print("Savings Account Balance is now: " + SavingsBalance)
print("Checking Account Balance is now: " + CheckingBalance)

i  = 1
while (i < 6):
  print("1. Check Account Balance")
  print("2. Deposit money")
  print("3. Withdraw money")
  print("4. Finish Actions")
  
  ChoiceSelection = input("Please select a number corosponding to your selection:")
  if ChoiceSelection == '1':
    print("\n")
    print("Your Savings Account Balance is: " + SavingsBalance)
    print("Your Checkings Account Balance is: " + CheckingBalance)
    print("\n")


  elif ChoiceSelection == '2':
    y = input("How much would you like to deposit into your Savings account?")
    SavingsBalance = savingsadd(int(SavingsBalance),int(y))
    print("\n")
    print("Your savings Balance is now: " + str (SavingsBalance))
    print("\n")
    y = input("How much would you like to deposit into your Checking account? ")
    CheckingBalance = checkingadd(int(CheckingBalance),int(y))
    print("\n")
    print("Your Checking Balance is now: " + str (CheckingBalance))
    print("\n")
    
  elif ChoiceSelection == '3':
    y = input("How much would you like to withdraw out of your Savings account?")
    SavingsBalance = savingsminus(int(SavingsBalance),int(y))
    print("\n")
    print("Your savings Balance is now: " + str (SavingsBalance))
    print("\n")
    y = input("How much would you like to withdraw out of your Checking account? ")
    CheckingBalance = checkingminus(int(CheckingBalance),int(y))
    print("\n")
    print("Your Checking Balance is now: " + str (CheckingBalance))
    print("\n")
  
  elif ChoiceSelection == '4':
    i=6


