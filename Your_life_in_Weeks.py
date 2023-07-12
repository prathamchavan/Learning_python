age = input("What is your current age? ")
print(age)

num = int(age)

years = 90 - num
days = years * 365
week = years * 52
months = years * 12

print(f"The number of years remaining is {years}.\nThe number of weeks remainig are {week}. \nThe number months remaining are {months}." )
