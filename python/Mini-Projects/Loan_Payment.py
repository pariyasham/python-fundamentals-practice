# Write a program that calculates and returns the monthly payment for a loan.

while True:
    inputs = input("Principal AnnualInterestRate Duration: ")
    try:
        principal, annual_interest_rate, duration = map(float, inputs.split())
        if (0 < principal and principal <= (10**9)) and (0 < annual_interest_rate and annual_interest_rate <= 30) and (1 <= duration <= 20):
            r = (annual_interest_rate / 100) / 12
            n = duration * 12
            monthlypayment = (principal * (r * (1+r)**n)) / (((1+r)**n) - 1)
            print(f"Monthly Payment: {monthlypayment:.6f}")
        else:
            print("Wrong Values! Please enter valid numbers.")

    except:
        print("Please enter the numbers in the correct format. Example format: 10 500 4")