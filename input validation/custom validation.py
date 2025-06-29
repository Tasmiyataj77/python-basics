import pyinputplus as pyip
#Passing a Custom Validation Function to inputCustom()
def addsUpToTen(numbers):
    numbersList=list(numbers)
    for i,digit in enumerate(numbersList):
        numbersList[i]=int(digit)
    if sum(numbersList)!=10:
        raise Exception('The digits must add up to 10, not %s.' % 
(sum(numbersList)))
     
        return int(numbers) # Return an int form of numbers. 
print(response=pyip.inputCustom(addsUpToTen))