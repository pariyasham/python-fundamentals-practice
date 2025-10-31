# Write a program that receives, in three separate lines, the number of hamburgers,
# the number of fries, and the number of drinks from the user.
# Then calculate and display the receipt and the final total amount.

cola_price = 1
french_fries_price = 3
hamburger_price = 5

hamburger = eval(input("Enter Count of Hamburgers: "))
french_fries = eval(input("Enter Count of French-Fries: "))
cola = eval(input("Enter Count of Colas: "))

total_price = (french_fries_price * french_fries) + (hamburger * hamburger_price) + (cola * cola_price)
discount = total_price * (10 / 100)

print("\n\n\nINVOICE")
print(f"\t• Hamburgers: {hamburger} -> {hamburger * hamburger_price}$")
print(f"\t• French-Fries: {french_fries} -> {french_fries * french_fries_price}$")
print(f"\t• Drink: {cola} -> {cola * cola_price}$")
print(f"\t• Total: {total_price}$")
print(f"\t• Discount: {discount}$")
print(f"\t• Pay: {total_price - discount}$")