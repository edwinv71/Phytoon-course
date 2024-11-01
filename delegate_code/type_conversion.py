#python is  dynamically typed 
#this means that datatypes can change during an application
#this type of coercion can happen implicitly in python or on purpose.
#each data type has its wrapper function of the same name

#conversion to boolen (bool)
#every datatype has its truthy and falsey values (convert to true or false)
#easier to remember the falsey values-most values are truthy
#zero numbers 0 and 0.0
#include str which is a collection or container(of single characters)
#not empty collections in JS are truthy

print("using bool()wrapper")
print(bool(1))
print(bool(99))
print(bool(-99))
print(bool(0))

#strings
print(bool("hello"))
print(bool("h"))
print(bool(""))
      
      #containers
print("list")
print(bool([1,2,3]))
print(bool([]))#false
print("set")
print(bool({1,2,3}))
print(bool({})) #False
print("dict")
print(bool({1: 1,2: 2,3:3}))
print(bool(dict()))#false

print(f"formatted:{10/3:.2f}")
