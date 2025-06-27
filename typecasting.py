#typecasting = the process of converting variables from one data type into another str(),int(),float(),bool()

name="tasmiya taj"
age=25
gpa=9.6
is_student=True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


#conversion
# gpa=int(gpa)
# print(gpa)

# age=float(age)
# print(age)

# age=str(age)# remain same
# print(age)

age=str(age)
age += "1"
print(age)

name=bool(name)
print(name)