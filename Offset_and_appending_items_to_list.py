#here we are going to understand the offset and
#appending items to the list

student_names = ["Samrat", "Ram", "Prathamesh", "Prithviraj", "Avdhoot"]
print(student_names)

print(student_names[0])
print(student_names[3])

print(student_names[-2])
print(student_names[-4])

student_names[-1] = "Akshay"
print(student_names)

student_names.append("Virat")
print(student_names)

student_names.extend(["Sumit, Rahul, Ananya, Ranbir"])
print(student_names)

print(student_names[2:5])

student_names.remove("Ram")
print(student_names)

print(student_names[:])
print(student_names)

print(student_names[:-1])
print(student_names[-1:])

print(student_names)
student_names.insert(5,'Abhi')
print(student_names)
