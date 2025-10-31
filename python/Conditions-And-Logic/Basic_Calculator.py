# Write a program that receives two numbers from the user,
# then receives a symbol that represents a mathematical operation
# ( + , - , * , / , or exponent ).
# Based on the operation provided, perform the corresponding calculation
# on the two numbers and display the result.

a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
symbol = input("Enter symbol: ")

match symbol:
    case "-":
        result = a - b
    case "+":
        result = a + b
    case "/":
        result = a / b
    case "*":
        result = a * b

print(f"{a} {symbol} {b} = {result}")