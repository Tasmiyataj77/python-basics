str(29)
print(str(29))

print('i am '+str(29)+' years old')

print(str(0))

print( str(-3.14))



# def hello():
#   print('Howdy!')
#   print('Howdy!!!')
#   print('Hello there.')
# hello()
# hello()
# hello()


def spam():
  global eggs
  eggs = 'spam'
  
eggs = 'global'
spam()
print(eggs)
