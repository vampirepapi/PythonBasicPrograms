#map is used to implement arithmetic function to the list

def add(x):
    return x+2

newlist = [10,20,30,40,50]

result = list(map(add,newlist))
print(result)

# implementing map with lambda

result1 = list(map(lambda y:y*2,newlist))
print(result1)