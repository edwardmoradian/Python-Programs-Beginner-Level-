# Author:  Edward Moradian
# Check for your weight health by BMI

StringInputHeight = input("Enter your height in inches: ")
Height = float(StringInputHeight)

StringInputWeight = input("Enter your weight in pounds: ")
Weight = float(StringInputWeight)

BMI = Weight * 703/Height**2

print("\nYour BMI: " + format(BMI, ".2f"))

if BMI >= 18.5 and BMI <= 25:
    print("You're at an optimal weight.")
elif BMI < 18.5:
    print("You're underweight!")
else:
    print("You're overweight!")
