# Project Title: Color Conversion (CMYK to RGB)
# Write a program that receives the values of C, M, Y, and K in four separate lines,
# and then converts and displays the corresponding RGB format in the output.

print("Enter the CMYK values that you want to convert to RGB in order:")
C = float(input("Enter C: "))
M = float(input("Enter M: "))
Y = float(input("Enter Y: "))
K = float(input("Enter L: "))

R = int(255 * (1 - C) * (1 - K))
G = int(255 * (1 - M) * (1 - K))
B = int(255 * (1 - Y) * (1 - K))
RGB = f"({R},{G},{B})"
print(RGB)