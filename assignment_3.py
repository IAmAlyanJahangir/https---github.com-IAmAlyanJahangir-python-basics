# expected output and reason


# value=None
# if value:
#     print("valuer is true")
# else:
#     print("valuer is false")


# check leap year on user input

year=int(input("Enter the year for checking the year is leap or not:  "))
leap=year%4
if leap==0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is a normal year.")