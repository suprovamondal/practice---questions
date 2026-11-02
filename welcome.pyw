# Topics:
# 1. Variables
# 2. Data Types
# 3. User Input
# 4. Type Casting
# 5. Operators
# 6. Strings
# 7. String Methods
# 8. f-Strings
# 9. Docstrings
# ============================================================


# ============================================================
# PART 1 - VARIABLES
# ============================================================

# PROBLEM 1
# Create variables for your name, age and city.
# Print all three values.


# PROBLEM 2
# Create a variable called score and store 95 in it.
# Print the score.
# Then change the score to 100 and print it again.


# PROBLEM 3
# Create variables:
#
# first_name = "Rahul"
# last_name = "Sharma"
#
# Print both values.


# PROBLEM 4
# Which of these are valid variable names?
#
# student_name
# student1
# 1student
# student-name
# _student

# ===========================================================================================
# SOLUTION 1
# =============================================================================================
# Name = "Suprova"
# Age = 26
# City = "Kolkata"

# print(f"My name is {Name} , I am {Age} old , born and brought up in {City}...")

# ============================================================================================
# SOLUTION 2
# ============================================================================================

# score = 95

# def change_score():
#     global score
#     print(f"My old score is {score}")

#     score = score +5
#     new_score = score
#     return new_score


# new_score = change_score()

# print(f"My new score is {new_score}")

#===========================================================================================================
# SOLUTION 3
#============================================================================================================

# first_name = "Suprova"
# last_name = "Mondal"

# print(f"My Name Is {first_name} {last_name}")

#=================================================================================================================
# SOLUTION 4
#======================================================================================================================

#Which of these are valid variable names?
#
# student_name
# student1
# 1student
# student-name
# _student

#THE ANSWER IS ---->>  student_name , student1 , _student


# ============================================================
# PART 2 - DATA TYPES
# ============================================================

# PROBLEM 1
# Create one variable of each type:
#
# string
# integer
# float
# boolean
#
# Print the value and its type.


# PROBLEM 2
# What is the data type of each?
#
# "25"
# 25
# 25.0
# True


# PROBLEM 3
# Create:
#
# age = 21
# age_text = "21"
#
# Print the type of both variables.


# PROBLEM 4
# Predict the output:
#
# print(type("100"))
# print(type(100))
# print(type(100.0))
# print(type(False))

#===========================================================================================
#  SOLUTION 1
#===========================================================================================

# my_name = "Suprova"
# my_age = 26
# my_height = 5.0
# does_i_like_python = True

# print(type(my_name))
# print(type(my_age))
# print(type(my_height))
# print(type(does_i_like_python))

# print(f"My name is {my_name} , I am {my_age} old , my height is {my_height} and it is {does_i_like_python} that I like python...")

#============================================================================================================================================
#  SOLUTION 2
#===============================================================================================================================================

# What is the data type of each?
#
# "25" -----> str
# 25 ------> Int
# 25.0 ------------> Float
# True -------> Bool

# str = "25"

# int = 25

# float = 25.0

# bool = True


# print(f"The data type of {str} is {type(str)}") # Class string

# print(f"The data type of {int} is {type(int)}") # Class Integer

# print(f"The data type of {float} is {type(float)}") # Class Float

# print(f"The data type of {bool} is {type(bool)}")   # Class Boolean

#===========================================================================================================================

# SOLUTION 3
#===========================================================================================================================

# age = 26
# age_text = "26"

# print(f"My Age Is {age} and it is  {type(age)}") # Class Integer

# print(f"My Age Is also  {age_text} but it is {type(age_text)}") # Class String


#====================================================================================================================================
# SOLUTION 4 
#=======================================================================================================================================

# Price = "100"
# print(type("100")) #----> Class String

# Value = 100
# print(type(100)) #------------------->> Class Integer

# Cost = 100.0
# print(type(100.0)) #------------->> Class Float

# Available = False
# print(type(False)) #------------------------->> Class Boolean


# ============================================================
# PART 3 - USER INPUT
# ============================================================

# PROBLEM 1
# Ask the user for their name and print:
#
# Hello Rahul
#
# where Rahul is whatever name the user enters.


# PROBLEM 2
# Ask the user for their city.
# Print:
#
# You live in Delhi
#
# using the city entered by the user.


# PROBLEM 3
# Ask the user for their favourite programming language.
# Print the answer.


# PROBLEM 4
# Ask the user for their name and age.
# Print both values.
#
# Do not perform any calculation yet.

#==========================================================================================================
# SOLUTION 1 
#==========================================================================================================

# name = input("Enter Your Name:   ")

# print(f" Hello {name} , Welcome Abroad...")

#==============================================================================================================
# SOLUTION 2 
#==============================================================================================================

# city = input("Enter Your City:   ")

# print(f" You live in {city} , did you born and brought up in {city}...")

#====================================================================================================================
# SOLUTION 3
#====================================================================================================================

# language = input("Enter Your Favourite Programming Language:   ")

# print(f"Your Favourite Programming Language is {language} , I like {language} too...")

#=========================================================================================================================
# SOLUTION 4
#============================================================================================================================

# name = input("Enter Your Name:   ")
# age = input("Enter Your Age:  ")

# print(f"Hi, I am {name} , and I'm {age} years old , Thank You.......#
#=======================================================================================================================================

# ============================================================
# PART 4 - TYPE CASTING
# ============================================================

# PROBLEM 1
# Convert the string "25" into an integer.
# Print the value and its type.


# PROBLEM 2
# Convert the string "99.50" into a float.
# Print the value and its type.


# PROBLEM 3
# Ask the user for their age.
# Convert the input into an integer.
# Print their age next year.


# PROBLEM 4
# Ask the user for two numbers.
# Convert both inputs into integers.
# Print their sum.


# PROBLEM 5
# What is wrong with this code?
#
# age = input("Enter your age: ")
# print(age + 1)
#
# Fix it.
#==================================================================================================================================

# SOLUTION 1
#==================================================================================================================================

# age = "25"
# print(type(age)) # Class String

# print(int(age))
# print(type(int(age))) # Class Integer

#==================================================================================================================================

# SOLUTION 2
#==================================================================================================================================

# Value = "99.50"
# print(type(Value)) #---------->> String

# print(float(Value)) #-------------->> 99.50

# print(type(float(Value))) # ---------------->> Float

#==================================================================================================================================

# SOLUTION 3
#==================================================================================================================================

# age = int(input("Enter your age here:  "))

# new_age = 1 + age

# print (f"I am {age} , next year i will be {new_age} years old... ")

#==================================================================================================================================

# SOLUTION 4
#==================================================================================================================================

# num1 = int(input("Enter your number 1 :  "))
# num2 = int(input("Enter your number 2 :  "))

# print(f" Here Is Your First Number {num1} and Second Number  {num2} ")

#====================================================================================================================================
# SOLUTION 5
#====================================================================================================================================


# What is wrong with this code?

# age = input("Enter your age: ")
# print(age + 1)

# ANSWER ---------->> print (age + 1) is trying to add an integer (1) to a string (age), which will result in a TypeError. To fix it, we need to convert the input to an integer before performing the addition.

# Solve

# age = int(input("Enter Your Age:  "))

# print(age + 1)

# ============================================================
# PART 5 - OPERATORS
# ============================================================

# PROBLEM 1
# Create two numbers:
#
# a = 20
# b = 6
#
# Print their:
# addition
# subtraction
# multiplication
# division
# remainder


# PROBLEM 2
# Predict the output:
#
# print(10 > 5)
# print(10 == 5)
# print(10 != 5)


# PROBLEM 3
# Ask the user for two numbers and print:
#
# Sum
# Difference
# Product


# PROBLEM 4
# Create:
#
# age = 20
#
# Check using comparison operators whether:
# age is greater than 18
# age is equal to 18


# PROBLEM 5
# Predict the output:
#
# print(True and False)
# print(True or False)
# print(not True)

#====================================================================================================================================
# SOLUTION 1
#====================================================================================================================================

# a = 20
# b = 6 

# def add():
#     return a + b

# print("Addition:" , a +b) #------------------->> 26

# def subtraction():
#     return a - b

# print("Substraction:" , a - b) # ------------------->> 14


# def multiplication():
#     return a * b
# print("Multiplication:", a * b) #---------------------->> 120

# def divide():
#     return a/b

# print("Division:" , a/b) #----------------------->> 3.34

# def remainder():
#     return a%b

# print("Remainder:", a%b) #--------------------->> 2

#====================================================================================================================================
# SOLUTION 2
#====================================================================================================================================

# print(10 > 5) # ------------->> True
# print(10 == 5) # ----------------->> False
# print(10 != 5) # -------------->> True

#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================

# user1 = int(input("Enter Your Number:  "))

# user2 = int(input("Enter Your Number:  "))

# print(f" Sum of Numbers: {user1 + user2}") # Sum Of Two Number 

# print(f" Difference of Numbers: {user1 - user2}") # Difference Between Two Number

# print(f" Product of Numbers: {user1 * user2}") # Product of Two Number

#====================================================================================================================================
# SOLUTION 4
#====================================================================================================================================

# age = 20

# print(age >= 18) #---->> True

#====================================================================================================================================
# SOLUTION 5
#====================================================================================================================================

# print(True and False) #------------------>> False

# print(True or False) # ---------------->> True 

# print(not True) # ------------------->> False

# ============================================================
# PART 6 - STRINGS
# ============================================================

# PROBLEM 1
# Create:
#
# word = "Python"
#
# Print the first character.


# PROBLEM 2
# Print the last character of:
#
# word = "Python"


# PROBLEM 3
# Print "Pyt" from the word "Python" using slicing.


# PROBLEM 4
# What is the output?
#
# text = "Python"
# print(text[0])
# print(text[-1])
# print(text[1:4])


# PROBLEM 5
# Create a string containing your full name.
# Print the first character and last character.

#====================================================================================================================================
# SOLUTION 1
#====================================================================================================================================

# word = "Python"

# print(word[0]) # ------------->> "P"


#====================================================================================================================================
# SOLUTION 2
#====================================================================================================================================

# word = "Python"

# print(word[1]) #--------------------------->> "y"


#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================

# word = "Python"

# print(word[0:3]) # ------------------------->> slicing return "Pyt"

#====================================================================================================================================
# SOLUTION 4
#====================================================================================================================================

# text = "Python"

# print(text[0]) #------------------------>> "P"

# print(text[-1]) #-------------------------->> "n"

# print(text[1:4]) #----------------------->> "yth"

#====================================================================================================================================
# SOLUTION 5
#====================================================================================================================================

# name = "Suprova Mondal"

# print(name[0]) #------------------------------->> "S" 
# print(name[-1]) #------------------------------------->> "l"

# ============================================================
# PART 7 - STRING METHODS
# ============================================================

# PROBLEM 1
# Convert this string to uppercase:
#
# text = "python is easy"


# PROBLEM 2
# Convert this string to lowercase:
#
# text = "PYTHON IS POWERFUL"


# PROBLEM 3
# Convert this string into title case:
#
# text = "learning generative ai"


# PROBLEM 4
# Remove the extra spaces from:
#
# text = "   hello python   "


# PROBLEM 5
# Replace "Java" with "Python":
#
# text = "I am learning Java"

#====================================================================================================================================
# SOLUTION 1
#====================================================================================================================================

# text = "python is easy"

# print(text.upper()) #----->> "PYTHON IS EASY"

#====================================================================================================================================
# SOLUTION 2
#====================================================================================================================================
# text = "PYTHON IS POWERFUL"

# print(text.lower()) #----->> "pytthon is powerful"

#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================

# text = "learning generative ai"

# print(text.title()) #----->> "Learning Generative Ai"

#====================================================================================================================================
# SOLUTION 4
#====================================================================================================================================

# text = "   hello python   "

# print(text.strip()) #----->> "hello python"


#====================================================================================================================================
# SOLUTION 5
#====================================================================================================================================

# text = "I am learning Java"

# print(text.replace("Java","Python"))

# ============================================================
# PART 8 - f-STRINGS
# ============================================================

# PROBLEM 1
# Create:
#
# name = "Rahul"
# age = 21
#
# Print:
#
# My name is Rahul and I am 21 years old.
#
# Use an f-string.


# PROBLEM 2
# Create variables for:
#
# name
# city
# course
#
# Print all three using ONE f-string.


# PROBLEM 3
# Create:
#
# a = 10
# b = 20
#
# Use an f-string to print:
#
# The sum of 10 and 20 is 30.


# PROBLEM 4
# Ask the user for their name and age.
# Convert age to an integer.
# Use an f-string to print:
#
# Hello Rahul, you are 21 years old.


# PROBLEM 5
# Create:
#
# price = 99.5678
#
# Use an f-string to print the price with exactly
# two decimal places.

#====================================================================================================================================
# SOLUTION 1
#====================================================================================================================================
# name = "Suprova"
# age = 26

# print(f"Hello, My Name is {name}, I'm {age} years old.")

#====================================================================================================================================
# SOLUTION 2
#====================================================================================================================================
# name = "Suprova"
# city = "Kolkata"
# course = "Gen AI"

# print(f"Hi, My Name is {name}, from {city} , and I'm Learning {course}..")


#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================
# a = 10
# b = 20


# print(f"The sum of {a} and {b} is {a+b}.")

#====================================================================================================================================
# SOLUTION 4
#====================================================================================================================================
# my_name = input("Enter Your Name:  ")
# my_age = int(input("Enter Your age:  "))

# print(f"Hi Dear {my_name}, You are {my_age} years old.. ")



#====================================================================================================================================
# SOLUTION 5
#====================================================================================================================================
# price = 99.5678

# print(f"My Value: {price:.2f}") #--------->> 99.57

# ============================================================
# PART 9 - DOCSTRINGS
# ============================================================

# PROBLEM 1
# Create a function called greet().
# Add a docstring that says:
#
# "Display a greeting message."


# PROBLEM 2
# Create a function called show_course().
# Add a docstring describing what the function does.
# Print "Welcome to the GenAI course!" inside it.


# PROBLEM 3
# What is the purpose of a docstring?
# Explain in your own words.


# PROBLEM 4
# What will this print?
#
# def greet():
#     """Display a greeting."""
#     print("Hello")
#
# print(greet.__doc__)

#====================================================================================================================================
# SOLUTION 1
#====================================================================================================================================

# def greet():
#     """Display a greeting message."""
#     print("Hello")

# greet()


#====================================================================================================================================
# SOLUTION 2
#====================================================================================================================================

# def show_course():
#     """Docstring describes What function does"""
#     print("Welcome to the Gen AI Coourse")

# show_course()

#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================
#What is the purpose of a docstring?

# A Docstring documentation Python Can read , also it is a short note inside a function that explains what the function does. 
# It is used to provide information about the function's purpose, parameters, and return values. 
# It helps other developers understand the code better and serves as a reference for future use.


#====================================================================================================================================
# SOLUTION 4
#====================================================================================================================================
# def greet():
#     """Display a greeting."""
#     print("Hello")

# print(greet.__doc__) #----------->> Display a greeting



# ============================================================
# PART 10 - MIXED LOGIC-BUILDING PRACTICE
# ============================================================

# PROBLEM 1
# Create a program that asks the user for:
#
# Name
# Age
# City
#
# Then display a profile using an f-string.


# PROBLEM 2
# Ask the user for two numbers.
# Display:
#
# First number
# Second number
# Sum
# Difference
# Product


# PROBLEM 3
# Ask the user to enter a sentence.
# Display:
#
# Original sentence
# Uppercase sentence
# Lowercase sentence
# Number of words
#
# Hint:
# split() can help you get the words.


# PROBLEM 4
# Ask the user for their name.
# Remove any unnecessary spaces using strip().
# Convert the name to title case.
# Display a welcome message using an f-string.


# PROBLEM 5
# Build a simple "Student Profile" program using:
#
# input()
# int()
# variables
# string methods
# f-strings
#
# Ask for:
# Name
# Age
# City
# Course
#
# Display a clean profile.

#====================================================================================================================================
# SOLUTION 1
#====================================================================================================================================
# name = input("Enter Your Name:  ")

# age = int(input("Enter Your Age:  "))

# city = input("Enter Your City:  ")

# print(f"Hi, I am {name},{age} years old and belongs from {city},Thank you!")

#====================================================================================================================================
# SOLUTION 2
#====================================================================================================================================

# num1 = int(input("Enter Your First Number:  "))
# num2 = int(input("Enter Your Second Number:  "))

# print(f"First Number: {num1}")
# print(f"Second Number: {num2}")
# print(f"Sum: {num1 + num2}")
# print(f"Difference: {num1 - num2}")
# print(f"Product: {num1 * num2}")


#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================
# my_sentence = input("Enter Your Sentence:  ")

# print(f"Original Sentence: {my_sentence}")
# print(f"Uppercase Sentence: {my_sentence.upper()}")
# print(f"Lowercase Sentence: {my_sentence.lower()}")
# print(f"Number of Words: {len(my_sentence.split())}")


#====================================================================================================================================
# SOLUTION 4
#====================================================================================================================================
# name = input("Enter Your Name:  ")
# name = name.strip() #--------->> Removes Extra Spaces From The Name

# name = name.title() # ------------->> Converts The Name Into Title Case

# print(f"Welcome, {name}!") #---------->> Welcome Message With Name In Title Case

#====================================================================================================================================
# SOLUTION 5
#====================================================================================================================================

#=============== Student Profile Program =====================

name = input("Enter Your Name:  ")
age = int(input("Enter Your Age:  "))
city = input("Enter Your City:  ")
course = input("Enter Your Course:  ")

name = name.strip().title() # Remove Extra Spaces and Convert to Title Case

city = city.strip().title() # Remove Extra Spaces and Convert to Title Case

course = course.strip().title() # Remove Extra Spaces and Convert to Title Case

print("\n--- Student Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Course: {course}")
print("-----------------------")




#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================





#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================






#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================








#====================================================================================================================================
# SOLUTION 3
#====================================================================================================================================