print("Welcome to the python pizza deleveries")
size = input("What size pizza do you want? S,M, or L ")
add_pepperoni = input("Do you want to pepperoni? Y or N ")
extra_cheeze = input("Do you want extra cheese? Y or N ")


bill = 0 

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25


if add_pepperoni == "Y": 
    if size == 'S':
        bill += 2
    else:
        bill += 3
else: 
    bill += 0


if extra_cheeze == "Y":
    bill += 1
else:
    bill += 0


print(bill)
