# ARITHMETIC
print(7 % 3)
print(7 ** 3)
print(7 // 3)
print(["ho"] * 3)
print(["hee", "haw"] * 3)
print("hee" * 3)
# to multiply strings is possible in Python
# because a special emthod of the string class is overidden
# to provide this behaviour
# it specifies what the * operator should do, in the case of strings
# more of that in objects and classes session!

# UNARY
print(not False)
print(not 2)
print(not 0)
print(not "")
print(not [1])#containers with content are True
print(not 1) #False too but for a different reason

# COMPARISON
print("a" > "b")#ASCII values
print("abc" > "dbc")#ASCII values
print("ABC" > "abc")#ASCII values
print([1,2,3] < [1,1,4])#
print([1,2,3] > [1,1,4])#
print([1,2,3] > [1,4,1])#
print([1,2,3] > [0,1,2])#compares one by one
print((1,2,3) > (0,1,2))#compares one by one
print({1,2,3} > {0,1,2})#

print({"a", "b", "c"} == {"b", "a", "c"})#sets are UNordered
print(["a", "b", "c"] == ["b", "a", "c"])
print(3 == 3)
print(3 is 3)#object method, but 3 is immutable so same object referenced
print([] == [])#True - same truthy value (coerced to boolean for comparison)
print([] is [])#False - different memory addresses
print("o" in "bobble")#membership operator
print("john" in {"name": "john"})#False: 
# membership operator in dicts compares KEYS

# LOGICAL
print(True and bool(0))#==>>
print(True and False)
print(bool([]) or bool("Hello"))#==>>
print(False or True)
# NOTE: when OBJECTS are used in and/or expressions
# results are VERY different!
