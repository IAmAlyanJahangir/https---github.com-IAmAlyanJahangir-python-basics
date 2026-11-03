
print("-----------------------------Formatted string----------------------")
print("\t \t Old style foratting  % operator\n")

name="Alyan Jahangir"
age=21
study="cs"

print("My name is %s and I am %d years old " %(name,age))
print("My name is %s and I am %d years old and I study %s" %(name,age,study))



print("-----------------------------Formatted string----------------------")
print("\t \t str.format method\n new and flexibe")


name="Alyan Jahangir"
age=21
print("My name is {} and I am {} year old".format(name,age))

# refernece variable by name and keyword
print("my name is {0} and i am {1} year old".format(name,age))
print("my name is {1} and i am {0} year old".format(name,age))

print("my name is {name} and i am {age} year old".format(name="kaleem",age=43))


print("-----------------------------Formatted string----------------------")
print("\t \t f-strings\nmost recent use ,concise and efficent way to format string")

name="Alyan Jahangir"
age=21

print(f"My name is {name} and I am {age} year old")


print("------------------------------string operator--------------")
a="hello"
b="world"

print(a+b) #concatenation
print(a*3) #multiple copies

print(r"hello\nhello")