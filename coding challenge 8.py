"""
challenge :-
List out  all the odd numbers from 1 to 100 using lists in Python.
"""
new_list = list(range(1, 100))

for x in new_list:

    if x % 2 != 0:
        print (x)
