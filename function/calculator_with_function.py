def adding(a,c):
    print(f"the Sum is: {a+c}")
def subtract(a,b):
    print(f"the Subtraction is: {a-b}")
def multiple(a,b):
    print(f"the multiplication is: {a*b}")
def devision(a,b):
    print(f"the division is: {a/b}")


print("wellcome to the calculator everyone")

a=int(input("enter one number: "))
b=input("enter the operator +-*/: ")
c=int(input("enter second number: "))

if b=="+":
    print(f"{adding(a,c)}")
elif b=="-":
    print(f"{subtract(a,c)}")
elif b=="*":
    print(f"{multiple(a,c)}")
elif b=="/":
    print(f"{devision(a,c)}")
else:
    print("Wrong my fiend")
 