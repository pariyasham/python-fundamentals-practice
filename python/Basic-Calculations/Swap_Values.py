# Write a program that receives two numbers from the user,
# swaps their values, and then prints the result.

a = eval(input("Enter Value of A: "))
b = eval(input("Enter Value of B: "))

c = a
a = b 
b = c

print(f"\nResult:")
print(f"A = {a}, B = {b}")