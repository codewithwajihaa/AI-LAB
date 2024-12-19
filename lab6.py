# Task 1: Sum of Digits of a Number

def sum_of_digits(number):
    total = 0
    for digit in str(number):
        if digit != '-':  # Ignore the negative sign
            total += int(digit)
    return total

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))


# Task 2: Count Words in a Sentence

def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return len(words)

sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))



# Task 3:Check if a Number is Even or Odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print("The number is", is_even_or_odd(num))


