#example for nested if else 
height = int(input("Enter your height in cm "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5.")
    elif age <= 18:
        print("You have to pay $7")
    else:
        print("You have to pay $12.")
else:
    print("Sorry, you can not ride the rollercoaster")