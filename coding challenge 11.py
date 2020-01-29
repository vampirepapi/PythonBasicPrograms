def discount(x):
    return (x - (x//10))

newlist = [10,20,30,40,50]

result = list(map(discount,newlist))
print(result)