# print("--------------------------String indexing--------------------------")

# name="alyan j"

 
# print(name[5])
# print(name[-5])


# print("--------------------------String slicing--------------------------")
# # syntax[start :end : step]

# name ="Alyan "
# #index 01234
# print(name[0:4])


# print(name[2:4])

print("--------------------------String method--------------------------")

name="hello,  alyanJahangir"
# 1.lenth method
print(len(name))

# 2 uppercase
print(name.upper())


# 3 lowerercase
print(name.lower())

# 4 countmethod

print(name.count("a"))
print(name.count("y"))

# 5 finding method
print(name.find("a"))

# 6 split

print(name.split( ))

# 7 replace

print(name.replace("hello,","hi"))

# 8 title method

print(name.title())

# 9 strip method

name1="    hello g  "
print(name1.strip())

# 10 join method
name2=("Alyan","is" ,"great")
print(" ".join(name2))
print("_______".join(name2))