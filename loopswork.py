for i in range(1,10):
    print(i)


time=int(input("Enter the number of times you want to loop: "))

for i in range(time):
    a= int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    c= input("Enter your operation: ")
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
