#lamdas are function without any names and return statement

#if we have to calculate the sqr of a number
#by normal function
def square(y):
     return y**2
print(square(10))

#now by using lambdas


result = (lambda x : x**2)(x=int(input("enter a number")))
print(result)