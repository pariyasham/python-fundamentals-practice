# Write a program that receives the hour and minute from the user in two separate lines,
# then calculates and prints the number of seconds that have passed since the beginning of the day.

while True:
    hour = eval(input("Enter Hour: "))
    if(hour < 0 or hour > 23):
        print("Wrong Value!")
    else:
        break

while True:
    miniutes = eval(input("Enter Minutes: "))
    if(miniutes < 0 or miniutes > 59):
        print("Wrong Value!")
    else:
        break

convert_hour = hour * 60 * 60
convert_miniute = miniutes * 60
result = convert_hour + convert_miniute

print(f"Result: {result}")