## Lists
skills = ["Minicomputer", "SuperComputer", "Notebook"]
 
print(skills[2]) 
 
skills[0] = "Laptop"
skills.append("Desktop")
skills.remove("Notebook")
print(skills) 
skills.insert(1,"Mobile Phone")
skills.extend(["Tablet","Iphone"])
print(skills)
##sorted Lists
num = ["Hamza","Ali","Naeema"]
sorted_num = sorted(num)
print(sorted_num)

##Tuples
num = (1,2,3,4)
print(num[3])
print("Length:",len(num))
print(num.count(1))
print(num.index(3))

#sets
Names = {"Hamza", "Ali", "Zahid"}
Names.add("Sajid")
print(Names)
Names.remove("Ali")


## Dictionaries
student = {
    "ID": "1234",
    "RollNo": 13,
    "gpa": 4
} 
print(student.get("gpa"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"ID":"678"})
print(student)
