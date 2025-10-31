# Write a program that receives your birth year and month as a single input,
# then separates the month from the year and prints both values.

year_month = input("Enter Your Birthyear & Birthmonth(Example: 8516): ")

year = year_month[0:2]
month = year_month[2:]

print(f"• Year: {year}")
print(f"• Month: {month}")