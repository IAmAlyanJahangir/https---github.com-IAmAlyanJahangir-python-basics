# # print number 1 to 3 for three times
# # for nested loops
# for num in range(3):
#     for i in range(1, 4):
#         print(i)
#     print("-----------")



# for num in range(3):
#     print(f"outher loop ",num+1)
#     for i in range(1, 4):
#         print(i)
#     print("-----------")


# # # while for loop iteration

# i=1

# while i<=3:
#     print(f"outer iteration is:",i)
#     for j in range(1, 4):
#         print(j)
#     print("-----------")
#     i+=1


# # print prime nuber between 2 to 10 range using nested loop
# for num in range(2, 11):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)



# homework in prinme number range is userinput and print prime number between that range using nested loop

a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))


for num in range(a, b+1):
    for i in range(a, num):
        if num % i == 0:
            break
    else:
        print(num)