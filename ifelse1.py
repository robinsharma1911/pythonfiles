#short hand if statement
a=10
b=10
if b>a: print("b is greater")
#short hand if else
print("b is greater") if b>a else print("a is greater")

#Ternary operator and conditional expressions
#one line ifelse if statement with three conditions
print("a is greater") if a>b else print("a is equal to b") if a==b else print("b is greater")

#nested if :-if statements inside if statements
x=10
if x>=10:
    print("above ten")
    if x>=20:
        print("above twenty")
        if x>40:
            print("above forty")
        else:
            print("x is less than forty and greater than twenty")
else:
    print("x is less than ten")