# Write a program that takes a number from the user, reverses it, 
# and then prints the sum of the original number and its reversed form.
# (The reversed form of a number is the number written backwards.)

num = input("Enter a Number: ")
reversed_num = num[::-1]
print(f"• Reversed's Number: {reversed_num}")
sum = int(num) + int(reversed_num)
print(f"• sum => {num} + {reversed_num} = {sum}")