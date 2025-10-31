# Receive a Gregorian year from the user and determine whether it is a leap year or not.

year = eval(input("Enter the Year: "))

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print("Yes!")
else:
    print("No!")