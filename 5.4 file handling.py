'''
file = open("demo.txt", 'r')
#for reading into file

content=file.read()

#if we want to read only 10 bytes of the demo.txt simply put 10 in the brackets

#content=file.read(10)

#now if we want to read the first line only

#content=file.readline()

print(content)
file.close()
'''

#now if we want to write to the file then read it


file=open("demo.txt", 'w')
file.write('this is going to add in my demo txt file')
file.close()

file=open("demo.txt", 'r')
content=file.read()
print(content)
file.close()
#for appending we simply put a in place of w
file=open("demo.txt", 'a')
file.write('this is new line')
file.close()


#writing new thing causing previous written files to disappear so we will use new function APPEND  which will add new texts




