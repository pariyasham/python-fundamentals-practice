# A health label on a product is considered *dangerous* if at least one of the following conditions is true:
# 1) At least three of the five indicators are Red.
# 2) At least two are Red AND at least two are Yellow.
# 3) All indicators are either Red or Yellow (no Green present).
#
# An image processing engineer has written a program that converts the label colors into a 5-character string,
# where each character represents the first letter of a color in English:
# 'R' = Red, 'Y' = Yellow, 'G' = Green.
#
# Your task: Write a program that takes this 5-character string as input and determines whether the product is "Healthy" or "Dangerous" based on the rules above.

health_sticker = input("Enter values: ").lower()

counter_red = 0
counter_yellow = 0 
dangerous = False

for char in health_sticker:
    if char == "y":
        counter_yellow += 1
    elif char == "r":
        counter_red += 1

if (counter_red >= 3) or (counter_red >= 2 and counter_yellow >= 2) or (counter_yellow == 5) or (counter_red == 5):
    dangerous = True

if dangerous:
    print("\nDANGEROUS!")
else:
    print("\nSAFE!")