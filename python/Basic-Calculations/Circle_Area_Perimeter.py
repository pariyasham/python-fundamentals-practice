# Write a program that receives the radius of a circle from the user,
# then calculates and prints the circumference and area of the circle.

import math
pi = math.pi

radius = eval(input("Enter Circle's Radius: "))

perimeter = radius * radius * pi
area = radius * 2 * pi

print(f"Area: {area:.2f}, Permiter: {perimeter:.2f}")