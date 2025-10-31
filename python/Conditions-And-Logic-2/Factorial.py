# Factorial

def factorial(number):
    if number < 0:
        return "Only Positive Number"
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

number = int(input("Enter A Number: "))
print(f"{number}! = {factorial(number)}")