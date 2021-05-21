class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
p1=person("james","parker")
p1.printname()
#create a child class...using pass keyword 
class student(person):
    pass
x=student("robin","sharma")
x.printname()
