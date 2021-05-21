class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
p1=person("james","parker")
p1.printname()
#create a child class...using _init_()
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
        print("name is " +self.firstname)
x=student("robin","sharma")
x.printname()
