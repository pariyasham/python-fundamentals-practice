# Write a program that takes a date in standard format from the user and prints how many days have passed since your birthday until that date.


birthdate = "1385/10/16"
date = input("Enter Your Date(Format: 1403/10/03): ")
convert = ((int(date.split("/")[0]) - int(birthdate.split("/")[0])) * 365) + ((int(date.split("/")[1]) - int(birthdate.split("/")[1])) * 30) + (int(date.split("/")[2]) - int(birthdate.split("/")[2]))
print(f"• Days passed: {convert}")