'''
a list is a mutable, indexed/ordered container
permits duplicates
commonly used to store elements of the same type
but need not be
'''

# creation
nums = []
nums = list()
nums = [1,2,3]

# element referencing
print(nums[2])#3

# element reassigning
nums[2] = 4

# adding elements
nums.append(5)

print(nums)#[1,2,4,5]

# slicing: the creation of a new list from all or part of the original
# slice syntax: [startIdx: endIdx: step]
# note endIdx is EXclusive (one beyond what you need)
fib = [0,1,1,2,3,5,8,13,21,34]
print(len(fib))#10

# give me between values 3 and 21 inclusive
print(fib[4:9])#[3, 5, 8, 13, 21]
# if we wanted to save AND print, we would traditionally require two steps
slice1 = fib[4:9]
print(slice1)
# using walrus
# print(slice1 = fib[4:9])#TypeError: 'slice1' is an invalid keyword argument for print()
# /doesn't understand compound assignment with return
print(slice1 := fib[4:9])# assignment AND return in same expression
print(slice1 := fib[7:])# 13 till the end?
print(slice1 := fib[::2])# steps of 2
print(slice1 := fib[::-2])# reversed in steps of 2

# ALL list slicing is immutable (returns a new list)
print(fib)#original unaffected

# builtins for list
print(f"num elements: {len(fib)}")
print(f"sum elements: {sum(fib)}")
print(f"min elements: {min(fib)}")
print(f"max elements: {max(fib)}")

# builtins using dir() function

# we may add lists
print(list6 := slice1 + [0,0,0])#[34, 13, 5, 2, 1, 0, 0, 0]

# we may multiply lists
print(list7 := slice1 * 10) #doesn't multiply elements but gives us the same list ten times over

# we can return index, value pairs
for index, element in enumerate(fib):
    print(index, element)

# list comprehension enables us to pass in a loop function
# to transform elements of a list
# it returns a new list with transformations applied

# scale original list of numbers
scaled_list = [element * 2 for element in fib]
print(scaled_list)
# akin to a map function in other languages

# filter original list for numbers < 10
print(under_tens := [el for el in fib if el <= 10])
# akin to a filter function in other languages


