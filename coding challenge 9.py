def student_discount(price):
    return (price - (price/10))
def additional_discount(newprice):
    return (newprice -(newprice / 20))
selling_price = 1000

print(additional_discount(student_discount(selling_price)))
