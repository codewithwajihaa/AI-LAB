# LAB 4
#  TASK 1 Check if a number is even or odd

number = int(input("Enter a number to check if it's even or odd: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# Lab Task 2: Simple ATM Machine

correct_pin = 1234
balance = 1000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    print("PIN Verified!")
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            print(f"Your current balance is: {balance}")
        elif choice == 2:
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"You have successfully withdrawn {withdraw_amount}. Remaining balance: {balance}")
            else:
                print("Insufficient balance!")
        elif choice == 3:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
else:
    print("Incorrect PIN. Terminating program.")



# Lab Task 3: Login System with Logical Operators
correct_username = "admin"
correct_password = 12345

username = input("Enter username: ")
password = int(input("Enter password: "))

if username == correct_username and password == correct_password:
    print("Login Successful!")
elif username != correct_username and password != correct_password:
    print("Incorrect username and password")
elif username != correct_username:
    print("Incorrect username")
elif password != correct_password:
    print("Incorrect password")
