print("----- ATM Simulator -----")
balance = 1000.00     
attempts = 3           

while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")
    if pin == "1234":                  
        print("Login successful!")
        break                          
    attempts -= 1                      
    if attempts > 0:
        print(f"Incorrect PIN. {attempts} attempt(s) remaining.")
    else:
        print("Incorrect PIN. Account locked.")
        exit()                         

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":                  
        amount = float(input("Amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
        else:
            print("Amount must be greater than 0.")

    elif choice == "2":               
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > balance:         
            print(f"Insufficient funds. Your balance is ${balance:.2f}")
        else:
            balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")

    elif choice == "3":                
        print(f"Current balance: ${balance:.2f}")

    elif choice == "4":                
        print("\n--- Session Complete ---")
        print(f"Final balance: ${balance:.2f}")
        break

    else:
        print("Invalid option. Please choose 1-4.")