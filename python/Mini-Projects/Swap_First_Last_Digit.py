# Write a program that takes a number as input, swaps the first and last digits,
# and prints the new number as output.
# It is guaranteed that the number is positive and has between 2 and 6 digits.

num = input("Enter a number: ")

if len(num) != 2:
    result = num[-1] + num[1:-1:1] + num[0] 
else:
    result = num[-1] + num[0] 

print(result)