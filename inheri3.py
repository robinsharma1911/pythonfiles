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
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        #add a year parameter and pass the correct year when creating object...
        self.graduationyear=year
x=student("robin","sharma",2019)
x.printname()
print(x.graduationyear)