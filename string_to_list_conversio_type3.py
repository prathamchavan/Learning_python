#list of the strings to the list of list 

string1 = "Show me the heart unfettered by foolish dreams and I'll show you a happy man"

string1=string1.split()

#applying list method to the individual elements of the list string1
list1= list(map(list,string1))

#printing the resultant of list 
print("Converted the list of the character list: \n", list1)