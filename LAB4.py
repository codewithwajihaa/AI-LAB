#  Question 1 -	Write a Python function to check if a number is even or odd.


number = 10  # Replace with any number to check
if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# Question 3 -	Write a Python function to find the maximum of three numbers.
a = 5
b = 12
c = 9

if a >= b and a >= c:
    max_value = a
elif b >= a and b >= c:
    max_value = b
else:
    max_value = c

print("The maximum number is:", max_value)






# QUESTION 2 -	Make starred shapes using Loops 
#  Pattern 1
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

    # Pattren 2
        
rows = 5
for i in range(rows):
    print("*" * rows)













