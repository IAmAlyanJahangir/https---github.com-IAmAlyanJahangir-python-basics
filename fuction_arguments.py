
# # print("-----------------------------default argument----------------------")
# # #default argument
# # def greeting(name ="bro"):
# #     print("hello "+name+" !")
# # greeting()
# # greeting("kaleem")

# # print("-----------------------------Keyword argument----------------------")
# # # keyword argument
# # def div(a,b):
# #     return a/b

# # result = div(10,5)
# # print(result)

# # result2 = div(b=10,a=5)
# # print(result2)



# print("-----------------------------abitrary argument----------------------")

# print("-----------------------------abitrary positional argument----------------------")
# print("\t \tit s like a tuple to store values\n")
# def add(*args):
#     return sum(args)

# op=add(22,44,66,78)
# print(op)




print("-----------------------------abitrary keyword argument----------------------")
print("\t \tit s like a dictionary to store values\n")

def details(**fname):
    for key, value in fname.items():
        print(f"{key}:{value}")


details(name ="alyan",age=12)