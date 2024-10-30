# the standard, built-in datatypes
# literals, or single values, OR expressions that evaluate to them
# IMMUTABLE by default

# bool. or boolean
# values: True or False
# immutable type (values cannot be changed, just re-referenced)

my_bool = True
my_bool = False # a re-assignment of the same reference, NOT a mutation of the value

# int. or integer/whole number value
# values: whole numbers, negative or positive, OR an expression that evaluates to a number
# immutable type (values cannot be changed, just re-referenced)

my_int = 1

# float. or floating-point/decimal number value
# values: whole numbers, negative or positive, with the dot character OR an expression that evaluates to a number
# immutable type (values cannot be changed, just re-referenced)

my_float = 1.0

# str (strings)
# values: any characters of zero or more
# immutable type
# single, double OR triple-quoted
# zero indexed (from first character)
# have a length property, obtained by using len()

my_str = "Hello"
first_character = my_str[0]
print(first_character)#H
print(len(my_str))#5
# print(my_str[5])#IndexError: string index out of range
# the problem here is although there are 5 elemnts in the string
# they are indexed 0-4

# string methods do not mutate originals
print(my_str.upper())
print(my_str)
# we may re-assign the reference to update as the new value
# but that does NOT mean the original has been mutated
# it has just had its refernce updated to point somewhere else
my_str = my_str.upper()
print(my_str)

# container types (for multiple VALUES)

# LIST LST() OR [] INSTANTIATED
# multiple values
# may be of same type but strictly do not have to be
# mutable by default
# commonly used for items of same type
my_list = ["bat", "ball", "gloves"]
print(my_list)
# access member read
print(my_list[0])
# update member
my_list[1] = "Cricket Ball"
print(my_list)
my_list.append("whites")#adds to end of list
print(my_list)
print(len(my_list))

# tuple
# a datatype that CANNOT have its elements re-assigned
my_tuple = ("bat", "ball", "gloves")#round brackets!
my_tuple = ("goal", "football", "boots")#round brackets!
# in Python any reference may be updated
# we redeclared my_tuple reference
# but we may not modify its elements
# my_tuple[0] = "Cricket bat" #TypeError: 'tuple' object does not support item assignment
print(my_tuple)
# my_tuple[0] = "Cricket bat" #TypeError: 'tuple' object does not support item assignment

# using tuples it may APPEAR that we can group related data together:
my_restaurant = ("The ultimate answer", 42)

# sets
# values: the elements can be of any type
# sets are NOT ORDERED
# sets may NOT contain duplicates
# set methods are powerful ways of examining sets and returning differences and similarities
my_set = {1,2,2,3,4,5,5}
print(my_set)#{1, 2, 3, 4, 5}
my_other_set = {"one", "two", "two", "forty-four", "ninety-one", "a-one"}
print(my_other_set)
# {'a-one', 'forty-four', 'ninety-one', 'two', 'one'}
# {'ninety-one', 'one', 'two', 'forty-four', 'a-one'}
# {'ninety-one', 'forty-four', 'two', 'one', 'a-one'}
my_varied_set = {"one", 1, True}
print(my_varied_set)#{1, 'one'}
my_varied_set_2 = {"one", 0, True}
print(my_varied_set_2)#{0, True, 'one'}
my_varied_set_3 = {"one", 0, False}
print(my_varied_set_3)#{0, 'one'}

print(bool(1))#True
print(bool(0))#False
print(bool([]))#False - empty containers are False in Python
print(bool([-1,2,3]))#True - containers with values are True

# dict (dictionary)
# values: key: value pairs
# keys: may be of any type but are commonly strings
# keys must be unique
# values: may be of any type and may be duplicated
# mutable
# note: a Python dict is NOT the same as an object, 
# even though they both print out with curly braces and key: value pairs !
# neither are dicts the same as sets, even though both are encoded with curly braces
# objects are made by classes
# the way we drill down into properties is different
# theoretically EVERYTHING is an object in Python

my_dict = {"name": "Fred", "age": 21, "employed" : True}
print(my_dict)

# None type
my_none = None
print(type(my_none))#<class 'NoneType'>
# means that the reference associated with it points nowhere
# if it did reference any of the other types, it doesn't any more
# null, in other languages
