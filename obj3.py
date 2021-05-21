#object methods....
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello my name is "+self.name)
p1=person("robin",21)
p1.myfunc()

#or..
class person:
    def __init__(myobj,name,age):
        myobj.name=name
        myobj.age=age
    def myfunc(abc):
        print("hello my name is "+abc.name)
p1=person("james",21)
p1.myfunc()
#same..self
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello my name is "+self.name)
p1=person("lokesh",21)
p1.myfunc()
