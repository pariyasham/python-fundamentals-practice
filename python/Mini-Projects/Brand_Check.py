# A person wants to eat an ice cream they bought from a store.
# The brand name of the ice cream is given as a string of lowercase letters.
# The ice cream is considered safe if the brand name does NOT contain the letter 'm'.
# Write a program to determine whether the ice cream is safe to eat.

brand_name = input("Enter Brand's Name: ").lower()
abalfazl = True
for char in brand_name:
    if char == "m":
        abalfazl = False

if abalfazl == True:
    print("Yes")
else:
    print("No No No")