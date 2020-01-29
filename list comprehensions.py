'''
lit comprehensions come in handy if we want to create list with certain conditions
like list with sqr of number
'''

#if we want list with sqr of numbers from 1 to 6
list =  [x**2 for x in range(1,7)]
print(list)

#if we want only even sqr
lists =  [x**2 for x in range(77,100) if x**2%2==0]
print(lists)