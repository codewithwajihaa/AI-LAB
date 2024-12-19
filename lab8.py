# Task 1: Car Class
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}, Mileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles
        print(f"The car has been driven {miles} miles. Total mileage: {self.mileage} miles.")

# Example usage
my_car = Car("Toyota", "Corolla", 2020, 15000)
my_car.display_info()
my_car.drive(200)
my_car.display_info()


# task # 2 Student Class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)
        print(f"Marks added: {marks}")

    def average_marks(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        return 0

    def display_info(self):
        avg_marks = self.average_marks()
        print(f"Student Info: Name: {self.name}, Age: {self.age}, Average Marks: {avg_marks:.2f}")

# Example usage
student = Student("Alice", 20)
student.add_marks([85, 90, 78])
student.display_info()

# Task 3: BankAccount Class

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

# Example usage
account = BankAccount("John Doe", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.display_balance()

 
