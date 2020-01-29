#filter function are used to filter the list with the proper mathematical function

newlist =[10,20,33,67,41]

result =list(filter(lambda x:x%2==0,newlist))
print(result)