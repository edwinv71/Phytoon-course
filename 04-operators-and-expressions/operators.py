# an expression involves operators (symbols that perform operations) 
# and operands (values that are transformed by the operator)
x = 1
x = x + 1
# the first line initialises x with a single value, 1
# the second line assigns x the result of an expression - itself plus 1
# the expression has an operator, +
# and two operands, x (again), and 1

# arithemetic operators
# +
# -
# *     - 2 squared is 2 * 2
# **    - 2 ** 3 is 2 cubed
# /
# %     - remainder, whole number division
# //    - quotient, whole number division

print(10 / 2)#5.0
print(10 % 2)#0

print(10/3)#3.3333333333333335
# promotion going on: result for division is a float if ints are input
# standard for floating-point arithmetic
# IEEE 754 since the 80s
# we should not use float values where accuracy is of primary concern!
print(f"formatted: {(10/3):.2f}")#3.33

# promotion
# the act of storing smaller datatypes in larger ones
print(10/3)#float result, int operands
print(9 + 2)#int result 11
print(9 + 2.0)#float result - promoted, 11.0

# non-numeric arithmetic
print("ho" * 3)
print("*" * 50)

# assignment operators
# = is single assignment
# += is compound assignment
# work for strings and numbers both

my_num = 1
my_num += 1
my_num += 1
print(my_num)

my_string = ""
my_string += "I "
my_string += "love "
my_string += "Python."
print(my_string)

# note this way of building strings is expensive in memory when long strings are involved
# other methods see https://www.tracedynamics.com/python-string-builder/

# walrus operator := asisgns and returns at the same time
# before walrus
x = 1
print(x)
# print(x = 2)#TypeError: 'x' is an invalid keyword argument for print()

# with walrus:
print(y := 2)#2 - assigns and returns in the same statement

my_nested_dict = {
    "name": "Alan",
    "languages": ("Python", "Java", "JavaScript")
}
print(my_nested_dict)
print(my_nested_dict["languages"])
print(my_nested_dict["languages"][0])
# my_nested_dict["languages"][0] = "CSS" #TypeError: 'tuple' object does not support item assignment
my_nested_dict["languages"] = "HTML"
print(my_nested_dict["languages"])

# /increment/decrement operators DO NOT EXIST IN PYTHON
# ++, --
# Guido applied anumber of optimisations when creating Python
# so we just say x = x + 1 or x += 1

# multiple assignment: not very Pythonesque
x = 1; y = 2; z = 3

#  a better way of initialiseng multiple avalues at onec
# that IS pythonesque:
x, y, z = 4, 5, 6
# equivalent in JS is destructuring

# dict
my_dict = {"name": "Alan", "age":21}
name, age = my_dict["name"], my_dict["age"]
# NOTE: square brackets notation for dict props

# list
my_nums = [1,2,3]
first, second, third = my_nums[0], my_nums[1], my_nums[2]
num1 = my_nums[0]
first_list, second_list, third_list = my_nums#see separate file


# assignment operator chaining (more specialised, avoid writing if possible)
x = 1
y = 1
# may be rewritten as this:
x = y = 1
print(x, y)

# comparison operators
# <         less than
# <=        less than or equal to
# >         greater than
# >=        greater than or equal to
# 3 >= 4      #order important
# !=        not equal to
# is        tests for IDENTITY: references the same object as

my_list = [1,2,3]
my_other_list = [1,2,3]
my_copied_list = my_list

print(my_list is my_other_list)#False
print(my_list is my_copied_list)#True

# the system Python uses to determine if two variables reference the same object is built-in function id()
print(id(my_list))          #4365156032
print(id(my_other_list))    #4364948672
print(id(my_copied_list))   #4365156032 same as my_list because they both reference same object

# because the copy copies the refernce it is called a SHALLOW copy
# the original may be mutated through the new reference
my_copied_list.append(4)
print(my_copied_list)       #[1, 2, 3, 4]
print(my_list)              #[1, 2, 3, 4]

import copy
my_deep_copied_list = copy.deepcopy(my_list)
my_deep_copied_list.append(5)
print(my_deep_copied_list)  #[1, 2, 3, 4, 5]
print(my_list)              #[1, 2, 3, 4] original unaffected
