BMI = 0
a = float(input("Enter your height : "))
b = float(input("Enter your weight : "))
BMI = BMI + b/(a**2)
print(BMI)
if BMI <=18.5:
  print("You are underweight")
elif BMI <=24.9:
  print("You have an healthy weight")
elif BMI <=29.9:
  print("You are overweight")
else:
  print("You are obese")
