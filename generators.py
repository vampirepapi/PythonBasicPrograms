# for generating number from 0 to 5 only even
def function():
    counter = 0
    while counter <6:
        if counter % 2 ==0:
          yield counter
        counter +=1


for x in function():
    print(x)
# now for generating even numbers in list form
def even(z):
    for i in range(z):
        if i%2==0:
            yield i

print(list(even(20)))
