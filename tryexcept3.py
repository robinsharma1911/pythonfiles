#first
#raise an exception... raise keyword
#raise an error and stop the progrma if x is lower than 0
'''
x = -1
if x<0:
    raise Exception("sorry,no number below zero")
'''


#second

#raise an TypeError(keyword) is x is not an integer  
y="hello"
if not type(y) is int:
    raise TypeError("only integers are allowed")