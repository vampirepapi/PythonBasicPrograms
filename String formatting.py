#string formatting is used to  join string to non string

# if we want to print date
numbers = [17,12,2019,2020]
newstring = 'Date:{0}/{1}/{2}'.format(numbers[0],numbers[1],numbers[2])
print(newstring)

# if we want to take data by input
z = '{x}/{y}'.format(x=input('enter x'), y=input('enter y'))
print(z)