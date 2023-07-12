print("Welcom to the tip calculator")
total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15?")
number_of_people = input("how many people to split the bill? ")

total = int(total_bill)
per = int(percentage)
nop = int(number_of_people)


tip = (total * per) / 100
contry = total/nop

print(f"The total bill is ${total} and the tip will be ${tip}.\nThe number of people to split the bill is {nop} and contry will be ${contry} per person")