# In this program, we consider three specific pilgrimage trips:
# 1) Mecca (Hajj) → Title: "Haji"
# 2) Karbala → Title: "Karbalaee"
# 3) Mashhad → Title: "Mashti"
#
# The input is a 3-character string consisting of 'Y' (yes) and 'N' (no),
# indicating whether the person has taken each of the trips, *in this exact order*:
# [Mecca, Karbala, Mashhad]
#
# Example:
# Input: Y N Y → The person has been to Mecca and Mashhad.
#
# Title priority if multiple trips have been taken:
# Haji (Mecca) > Karbalaee (Karbala) > Mashti (Mashhad)
#
# If no trip has been taken at all, the title is: "Agha" (similar to "Sir").



# ---------------- WITHOUT LOOP ----------------
nickname = input("Enter trip history (Y/N for Mecca, Karbala, Mashhad): ")

if nickname[0] == "Y":
    print("Title: Haji (Visited Mecca)")
elif nickname[1] == "Y":
    print("Title: Karbalaee (Visited Karbala)")
elif nickname[2] == "Y":
    print("Title: Mashti (Visited Mashhad)")
else:
    print("Title: Agha (No pilgrimage trip taken)")


# ---------------- WITH LOOP ----------------
values = input("Enter trip history again (Y/N for Mecca, Karbala, Mashhad): ")
titles = ["Haji (Visited Mecca)", "Karbalaee (Visited Karbala)", "Mashti (Visited Mashhad)"]

for i in range(len(values)):
    if values[i] == "Y":
        print(f"Title: {titles[i]}")
        break
else:
    print("Title: Agha (No pilgrimage trip taken)")