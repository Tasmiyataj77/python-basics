from pathlib import Path
print(Path('spam','bacon','eggs'))
print(str(Path('spam', 'bacon', 'eggs')))


myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))
    


#Using the / Operator to Join Paths
print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))


homeFolder = r'C:\Users\Al'
subFolder = 'spam'
print(homeFolder + '\\' + subFolder)
print('\\'.join([homeFolder, subFolder]))

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
print(homeFolder / subFolder)
print(str(homeFolder / subFolder))