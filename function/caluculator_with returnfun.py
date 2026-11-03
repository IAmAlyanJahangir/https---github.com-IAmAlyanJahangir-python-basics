def adding(a,c):
    return a+c
def subtract(a,b):
    return a-b
def multiple(a,b):
    return a*b
def devision(a,b):
    return a/b

print("wellcome to the calculator everyone")
def input(a,b,c):
    if b=="+":
        d=adding(a,c)
        print(d)
    elif b=="-":
        d=subtract(a,c)
        print(d)
    elif b=="*":
        d=multiple(a,c)
        print(d)
    elif b=="/":
        d=devision(a,c)
        print(d)
    else:
        print("Wrong my fiend")
  
  
a=int(input("enter one number: "))
b=input("enter the operator +-*/: ")
c=int(input("enter second number: "))
input(a,b,c)