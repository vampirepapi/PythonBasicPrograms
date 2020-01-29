w = float(input("enter weight"))
h = float(input("enter height"))

'''bmi = (w/h**2)
print(bmi)'''



'''def bmi(w,h):
    print(w/h**2)
bmi(w,h)'''


'''def bmi(w,h):
    return w/(pow(h,2))

result =  bmi(w, h)

print(result)'''


def bmi(w,h):
    return w/h**2

result =  bmi(w, h)

print(result)