try:
    a=8
    #if we change the value of b other than 0 then il will give our excepted result
    b=0
    print(a/b)
except ZeroDivisionError:
    print("There Is ZeroDivisionError")

#now, if we want to execute our further piece of code to run we use FINALLY BLOCK

finally:
    print("This will be executed no matter if exception is going to come or not")