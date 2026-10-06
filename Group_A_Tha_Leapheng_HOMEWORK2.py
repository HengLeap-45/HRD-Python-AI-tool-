print("----- ATM Simulator -----") 

UserPIN=int(input("ENTER YOUR 4-DIGIT PIN : "))
if UserPIN==1234:
    print("Login successfully!")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
else:
    print("Incorrect PIN. 2 attempt(s) remaining.")
User_choice = input("ENTER YOUR CHOICE : ")
if User_choice=="1" :
    user_input = float(input("Enter the amount to deposit : "))
    print("Deposit  $500.00 . ", "New deposit : ", user_input ,"$")
    
    
