# assignment 4


# 1 limit the decimal place to 2 digits using format method and print result, for the varable  pi=3.14159265359

pi = 3.14159265359

# print(round(pi,2))    #usinground function
print("value of pi is {}".format(pi))
print("value of pi is {:.2f}".format(pi))  #.format method to limit decimal place to 2 digits
print(f"{pi:.2f}")                #f-string method to limit decimal place to 2 digits



# 2. Extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course", slice characters from index 2 to 8, skipping every other char.


my_string = "Python Course"

print(my_string[2:8:2])  #slicing from index 2 to 8 with a step of 2



#3. Slice to get only the middle character(s): For my_name = "Alyan", use slicing to extract the middle character(s).

my_name = "Alyan"
my_name2="MAlyan"

def mid_term(word):
    middle=int(len(word)/2 )
    if len(word)%2==0:
        return word[middle-1:middle+1]
    else:
        return word[middle] 

print(mid_term(my_name))  #for odd length string
print(mid_term(my_name2)) #for even length string


# 4. Remove the first 3 and last 3 characters: Given my_string = "Regression Analysis", remove the first 3 and last 3 characters.

my_first_string = "Regression Analysis"

print(my_first_string[3:-3]) #removing first 3 and last 3 characters using slicing





#5. Get the substring that starts 4 characters from the end to the last character: For my_string = "Classification", slice the string starting from the 4th character from the end to the last character.
my_string = "Classification"
print(my_string[-4:])  # getting the last 4 characters


#6. How to Reverse a String Using Python String Methods?

word="python"
print(word[::-1])



#7. Write a Python function to check if a string is a palindrome using string methods.

my_word="madam"

def is_palindrome(word):
    if word==word[::-1]:
        print(f"The {word} is a palindrome")
    else:
        print(f"The {word} is not a palindrome")

print(is_palindrome(my_word))  #checking if the word is palindrome or not