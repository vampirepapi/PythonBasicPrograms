'''
challenge :-
Write Python code which accepts name of a product and in turn returns their respective prices.
Make sure to use dictionaries to store products and their respective prices.
The dictionary should include at least 5 elements.
'''

products = {'book':30, 'pencil':10, 'pen':20, 'notebook':40, 'bag':400}
newproduct = input('enter a product:')

if(newproduct in products):
    print(products.get(newproduct))

else:
    print("404 Not Found")
