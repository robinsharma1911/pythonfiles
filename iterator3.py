#stop iteration in the programs... stop after 20 iteration
class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass = mynumber()
myiter = iter(myclass)
for x in myiter:
    print(x)