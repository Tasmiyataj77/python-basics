#Phone Number and Email Address Extractor
import pyperclip, re

#Step 1: Create a Regex for Phone Numbers
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)?  #separator
    (\d{3})   #first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

#Step 2: Create a Regex for Email Addresses
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @    # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
)''',re.VERBOSE)


#Step 3: Find All Matches in the Clipboard Text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1] or '', groups[3], groups[5]])
    if groups[8] :
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
    
#Step 4: Join the Matches into a String for the Clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')