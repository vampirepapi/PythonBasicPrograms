a=int(input("enter a number"))
b=int(input("enter a number"))

try:
    def add(a,b):
        return a/b
    result=add(a,b)
    print(result)

except ZeroDivisionError:
    print('0 ')
    print('got ZDE ')
    print('assign true values')


