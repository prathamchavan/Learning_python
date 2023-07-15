# A string consisting of integers to a list of integers

#string with integers seperated by spaces
string1 = "1 2 3 4 5 6 7 8"
print(string1)

#converting the string into the list of the strings
list1 = list(string1.split())
print("Converted string to list :",list1)

#typecasting the individual elements of the string list into integer using the map() method
list2 = list(map(int,list1))
print("List of the integers: ",list2)

print(type())