# importing a module and module like random here
import random

# here applying for loop in range = 5 i.e it will print 5 time the result
for x in range(5):

    # Now calling a random module like randint here
    # now have to store that result somewhere so a result variable is decleared to store the random values
    result = random.randint(1, 8)

    print(result)
