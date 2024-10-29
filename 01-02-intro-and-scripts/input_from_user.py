# variable declaration
# in Python there is NO keyword to declare a variable, apart from a couple of edge cases - TODO later (global and nonlocal)
# this means that a Python variable MUST be initialised with a value when first declared
# a variable's type can change during the application - any type, at any time

my_variable = 1 #declared my_variable name, assigned value 1: both operations together - INITIALISED

my_name = "Alan"

# my_name = "Alan Lavender"

# my_name = {"name": "Alan"}

# my_name = True

print(type(my_variable)) #<class 'int'>
print(type(my_name))#<class 'str'>

your_name = input("Enter your name:")
print(your_name)