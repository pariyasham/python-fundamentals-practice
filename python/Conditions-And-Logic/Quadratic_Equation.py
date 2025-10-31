# Write a program that receives the coefficients of a quadratic equation (a, b, c)
# from the user in three separate input lines.
# Then, based on the given values, calculate and display the solutions of the equation.

import math

a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

delta = (b**2) - (4*a*c)

if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2 * a)
    x2 = (-b - math.sqrt(delta))/(2 * a)
    print(f"x1: {x1}, x2: {x2}")
elif delta == 0:
    x = (-b) / (2 * a)
    print(f"x: {x}")
else:
    print("NO ANSWER!")