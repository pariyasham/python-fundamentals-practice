# Get the speed from the user and display the result according to the rules:
# speed < 90        → "NO Ticket!"
# 91 ≤ speed ≤ 110  → "Small Ticket!"
# speed > 111       → "Big Ticket!"

speed = eval(input("Enter The Speed Number: "))

if speed <= 90:
    print("NO TICKET!")
elif speed >= 91 and speed<=110:
    print("SMALL TICKET!")
else:
    print("BIG TICKET!")