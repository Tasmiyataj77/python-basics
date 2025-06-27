print('entre your value')
name=input()
print('year of birth')
b_year=int(input())
print('current year')
c_year=int(input())
age= c_year-b_year
if age>60:
    print('you are senior citzen')
else:
    print('you are not senior citizen')