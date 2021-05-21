class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
p1=person("james","parker")
p1.printname()
#create a child class...using _init_() and super()
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        #add properties.....
        self.year=2019
x=student("robin","sharma")
x.printname()
print(x.year)
