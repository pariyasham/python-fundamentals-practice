# BMI

weight = float(input("Enter your Weight(KG): "))
height = float(input("Enter your Height(M): "))

BMI = round(weight / (height**2), 2)

if(BMI < 18.5):
    print(f"BMI: {BMI} => Category: Underweight")
elif(BMI >= 18.5 and BMI <= 24.9):
    print(f"BMI: {BMI} => Category: Normal weight")
elif(BMI >= 25 and BMI <= 29.9):
    print(f"BMI: {BMI} => Category: Overweight")
elif(BMI >= 30 and BMI <= 34.9):
    print(f"BMI: {BMI} => Category: Obesity (Class 1)")
elif(BMI >= 35 and BMI <= 39.9):
    print(f"BMI: {BMI} => Category: Obesity (Class 2)")
elif(BMI >= 40):
    print(f"BMI: {BMI} => Category: Obesity (Class 3)")