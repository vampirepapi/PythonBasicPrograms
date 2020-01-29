a = int(input('enter a value'))
b = int(input('enter a value'))


def add(a, b):
    # c=a+b   old methodology
    return a+b


def square(c):
    return c*c


result = square(add(a, b))

print(result)