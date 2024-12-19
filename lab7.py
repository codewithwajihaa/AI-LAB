# Task 1: Draw a Square with Asterisks
def draw_square(side_length):
    for _ in range(side_length):  # Repeat for each side
        print("* " * side_length)  # Print the row with side_length asterisks

# Test the function
side = int(input("Enter the side length of the square: "))
draw_square(side)


# Task 2: Sum of Even Numbers in a List

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            total += num
    return total

# Test the function
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Sum of even numbers:", sum_even_numbers(nums))


# Task 3: Countdown to Zero
def countdown(number):
    while number >= 0:
        print(number)
        number -= 1  # Decrease the number by 1 each time

# Test the function
num = int(input("Enter a number to start the countdown: "))
countdown(num)
