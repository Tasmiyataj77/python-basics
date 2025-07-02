# import re
# phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
# print(mo.group())
# areaCode,mainNumber=mo.group(1),mo.group(2)
# print(areaCode)
# print(mainNumber)


#if u want parenthesis use this code 
import re
phoneNumRegex=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))




