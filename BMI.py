height = float(input("Enter your Height in meters"))
weight = int(input("Enter your weight in kilos"))
BMI = weight/(height*height)
print("BMI is", BMI)
if BMI<=18:
    print("You are underweight")
elif 18 < BMI <= 25:
    print("You are normal")
elif 25< BMI <=35:
    print("You are overweight")
else:
    print("You are Obese")