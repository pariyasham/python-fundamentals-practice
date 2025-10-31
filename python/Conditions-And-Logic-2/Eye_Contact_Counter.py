# In a subway wagon, there are two rows of seats facing each other. Each row has 8 seats.
# Each seat is either empty or occupied by a person. 
# If a person is sitting in seat i in one row, they can only look directly at seat i in the opposite row.
# If that opposite seat is also occupied, then the two people make eye contact.
# You are given the seating arrangement, and your task is to calculate how many pairs of people are making eye contact.

eyes_1 = input("Enter First Row: ").split()
eyes_2 = input("Enter Second Row: ").split()

counter = 0
for i in range(8):
    if eyes_1[i] == "1" and eyes_2[i] == "1":
        counter += 1

print(f"Count: {counter}")