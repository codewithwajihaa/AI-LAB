# 1. Print Numbers with Loops

for number in range(1, 11):
    print(number)

# 2. Calculate the Sum of Numbers

n = int(input("Enter a number: "))
sum_of_numbers = 0

for i in range(1, n + 1):
    sum_of_numbers += i

print(f"The sum of numbers from 1 to {n} is {sum_of_numbers}.")



# 3. Display a Star Pattern (Triangle Example)
rows = int(input("Enter the number of rows for the star pattern: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()


# 4. Find Even Numbers in a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the list are:")

for num in numbers:
    if num % 2 == 0:
        print(num)
