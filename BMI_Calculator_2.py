weight = input("Please input your weight in kilogram: ")
print((weight))
height = input("Please input your height in meters: ")
print((height))

#using an exponent operator
BMI = int(weight) / float(height)**2

print(round(BMI))

if BMI <= 18.5:
    print("You are underweight.")
elif 18.5 < BMI <= 25:
    print("You are normal weight.")
elif 25 < BMI <= 30: 
    print("You are obese.")
else:
    print("You are clinically obese.")