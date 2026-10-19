# #conditoional statament

# age=int(input("Enter your age: "))
# if age<17:
#     print("your are minor")
# elif age>79:
#     print("you are oldage ")
# else:
#     print("you are adult")


mark1=int(input("enter your first book numbers"))
mark2=int(input("enter your second book numbers"))
mark3=int(input("enter your third book numbers"))

percentage=((mark1+mark2+mark3)/300)*100

print(f"your percentage is {int(percentage)}%")

if percentage>=80:
    print("you got A grade.")
elif percentage>=70:
    print("you got B grade.")
elif percentage>=60:
    print("you got C grade.")
elif percentage>=50:
    print("you got D grade.")
else:
    print("you got f grade.")