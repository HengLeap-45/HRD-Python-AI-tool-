print("===== ATM simulator =====")
balance = 1000.00
attempts = 3 
# PIN 
while attempts > 0 : 
   pin = input("Enter your PIN : ")
   if pin == "1234" :
        print("Login success")
        break
   attempts -= 1 
   if attempts > 0 : 
    print(f"INCORRECT PIN , {attempts} attempt(s) remaining") 
   else :
    print("account locked") 
    exit() 

# MENU 
while True :
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ") 
    if choice == 1 :
        amount = float(input("Enter your amount to deposit : "))
        if amount > 0 : 
            balance = balance + amount 
            print(f"Deposit ${amount:.2f}. New balance: ${balance:.2f}")
        else : 
            print("Invalid")
    elif choice == 2 :
        amount = input("Enter amout to withdraw :")
        if amount <= 0 :
            print("amount must be greater than 0")
        elif amount > balance : 
            print(f"Withdrew $ {balance:.2f}")
        else :
            balance = balance - amount 
            print(f"Withdrew $ {balance:.2f} . New balance $ {amount:.2f}")
    elif choice == 3 :
        
    
        
    
    
    