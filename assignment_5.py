
# # print("Alyan",end="  ")
# # print("Jahangir")
# # # print loop value in same line
# # i=1
# # while i<4:
# #     print(f"Hello Alyan",i,end=" ")
# #     i+=1


# # # star pattern
# # # using nestedloop
# # n=5
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print("*",end=" ")
# #     print()


# # # using singleloop
# # n=5
# # for i in range(1,n+1):
# #     print("*"*i)

# # inverted triagle
# # using nestedloop
# # n=5
# # for i in range(n,0,-1):
# #     for j in range(1,i+1):
# #         print("*",end=" ")
# #     print()


# # # single loop
# # for i in range(n,0,-1):
# #     print("*"* i)

# # parmid pattern
# n=5

# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"* (2*i-1))



# # factorial of a number
# def factorial(n):
#     result=1
#     while n>0:
#         result*=n
#         n-=1
#     return result
# value=int(input("Enter a number to find factorial: "))
# print(f"factorial of {value}",factorial(value))


# # count vowels in string 
# my_string=input("Enter a string: ")
# # vowels="aeiouAEIOU"
# count=0

# for char in my_string:
#     if char.lower() in vowels:
#         count+=1

# print(f"Number of vowels in the string: {count}")


# # finding longest word in string using for loop
# sentence = input("Enter a sentence: ")
# word=sentence.split()
# longest_word=""

# for word in word:
#     if len(word)>len(longest_word):
#         longest_word=word
# print(f"the longest world is:",longest_word)



# # dowhile loop in python

# while True:
#     num = int(input("Enter a number (0 to exit): "))
#     if num >10:
#         print(f"valid number enteres{num}")
#         break
#     else:
#         print("invalid! number is not greater than 10")


# fibonacci sequence

def fibonacci(n):
    a,b=0,1
    count=0
    while count >n:
        print(a)
        a,b=b,a+b
        count=+1

fibonacci(5)