file=open("demo.txt", 'w')
file.write('om namah shivaay')
file.close()

file=open("demo.txt", 'r')
result=file.read()
print(result)
file.close()

file=open("demo.txt", 'a')
file.write('\n har har mahadev')
file.close()