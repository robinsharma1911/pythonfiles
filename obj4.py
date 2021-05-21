#object methods....
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello my name is "+self.name)
p1=person("robin",21)
p1.myfunc()
#modify object properties...
p1.age=18
print(p1.age)
#delete object properties...using del keyword
del p1.age
print(p1.age)
#del the object using del keyword...
del p1
print(p1.name)

#pass statement...
class myclass:
    pass