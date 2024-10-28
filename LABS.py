    #   TASK 1
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# TASK 2
correct_pin = "1234"
balance = 1000

pin = input("Enter your PIN: ")

if pin == correct_pin:
    print("\nLogin successful! Please select an option:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print(f"Your balance is ${balance}.")
    
    elif choice == "2":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Transaction successful! Your new balance is ${balance}.")
        else:
            print("Insufficient balance.")
    
    else:
        print("Invalid choice.")

else:
    print("Incorrect PIN. Terminating the program.")


# TASK 3

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login Successful!")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")
