#    Question 1	# Write programs for the different type string “”,’’,””””””
# Using single quotes
string1 = 'This is a string with single quotes'

# Using double quotes
string2 = "This is a string with double quotes"

# Using triple quotes for multi-line strings
string3 = """This is a
multi-line string
using triple double quotes"""

# Using triple single quotes for multi-line strings
string4 = '''This is another
multi-line string
using triple single quotes'''


print(string1)
print(string2)
print(string3)
print(string4)


# QUESTION 2 	Make a calculator using the operands in the clasS
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Example usage
calc = Calculator()
print("Addition:", calc.add(5, 3))        # Output: 8
print("Subtraction:", calc.subtract(5, 3)) # Output: 2
print("Multiplication:", calc.multiply(5, 3)) # Output: 15
print("Division:", calc.divide(5, 3))      # Output: 1.666...



# QUESTION 3 	Make program to see if value is true of false.

value = input("Enter a value: ")  
is_true = bool(value)

print("The value is", is_true)

