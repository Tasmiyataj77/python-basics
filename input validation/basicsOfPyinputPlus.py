import pyinputplus as pyip
# response=pyip.inputNum('enter a number: ')
# print(response)


#----->The min, max, greaterThan, and lessThan Keyword Arguments<-----
# response=pyip.inputNum('enter a number: ',min=4)
# print(response)

# response=pyip.inputNum('enter a number: ',greaterThan=4)
# print(response)

# response = pyip.inputNum('>', min=4, lessThan=6)
# print(response)


#------>The blank Keyword Argument<-------
# response = pyip.inputNum('Enter num: ')
# print(response)

# response = pyip.inputNum(blank=True)
# print(response)




#------>The limit, timeout, and default Keyword Arguments<-----
# response = pyip.inputNum(limit=2)
# print(response)

# response = pyip.inputNum(timeout=10)
# print(response)

# response = pyip.inputNum(limit=2, default='N/A')
# print(response)



#-------->The allowRegexes and blockRegexes Keyword Arguments<------
# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# print(response)


# response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
# print(response)

# response = pyip.inputNum(blockRegexes=[r'[02468]$'])
# print(response)

response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(response)
