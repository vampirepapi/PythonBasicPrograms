class students:                         #defining class
    def __init__(self,name,contact):    #defining sttributes
        self.name = name
        self.contact = contact

    def getdata(self):                 #defining methods for taking input
        print('Accepting Values!')
        self.name = input('Enter Name ')
        self.contact = input('Enter Contact No: ')


    def putdata(self):                 #defining another method for printing out the values
        print('The Names Is - '+ self.name,'\nThe Contact No:is - '+self.contact)


john = students('none',0)              #defining class and it is must to have something in students("name",0)in class
john.getdata()
john.putdata()

