# Write a program that defines four variables to store:
# first name, last name, age, and height.
# Then print the data type of each variable in the output.

print("Enter the following information about yourself")
first_name = input("• First Name: ")
last_name = input("• Last Name: ")
age = eval(input("• Age: "))
height = eval(input("• Height(m): "))

print(f"Entered types -> First Name: {type(first_name).__name__}, Last Name: {type(last_name).__name__}, Age: {type(age).__name__}, Height: {type(height).__name__}")