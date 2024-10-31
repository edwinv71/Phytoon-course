'''
Loops come in two sorts: the while loop and the for loop
# while loops are commonly used for console IO
# there may be no obvious end to the process
# for loops are commonly used to iterate over containers
# the length of the container is known in advance
The for loop in Python is syntactic sugar for a while loop, 
usually when the number of iterations is known in advance.
There are no for loops at runtime, only while loops that the code is compiled into.
While loops in source code are useful when the number of iterations is not known in advance.

In Python, an optional else clause may be added to the end of both types of loop, for and while.
It is executed if the loop completes and doesn't hit a break statement.
In other words, if the loop completes normally.
To make this clearly readable, add a comment "# no break" next to the else clause.
'''
names = ['Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson']

# for loop - generally used for iterating over containers
# the length of the container(len()) is known in advance

for name in names:
    print(name)

print(len(names))

# list slicing and loops
# a list slice returns a new list, picked from the original, with up to 3 args:
# [start_index_inclusive, end_index_exclusive, step]
# when slicing to the very end of a list, we put in end_index as len(list) - there is no element AT this index!
print("list slicing 1")
for name in names[2:4]:
    print(name)
print("list slicing 2")
for name in names[5:6]:
    print(name)
print("list slicing 3")
for name in names[0:7:2]:
    print(name)
# print(names[7])#IndexError: list index out of range
print("list slicing 4 - reversed")
for name in names[::-1]:
    print(name)

names_as_set = {'Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson'}
print("from a set")
for name in names_as_set:
    print(name)
    '''order
first time
James Brown
Janet Jackson
David Hume
Michael Jackson
Gordon Brown
David Bowie

second time
Gordon Brown
Janet Jackson
Michael Jackson
James Brown
David Bowie
David Hume
    '''

# dictionaries

names_as_dict = {
    "politicians": ["Gordon Brown", "David Hume"],
    "musicians": ["Michael Jackson", "James Brown"],
}

# keys
for key in names_as_dict.keys():
    print(key)

# values
for value in names_as_dict.values():
    print(value)

# both keys AND values
for key, value in names_as_dict.items():
    print(key, value)

# using a range function to control no. of iterations
for i in range(1,11):#end index exclusive as well
    print(i)

# optional else clause and break and continue

counter = 0
while counter < len(names):
    if names[counter] == "Janet Jackson":
        # break
        counter += 1#otherwise infinite loop
        continue
    print(names[counter])
    counter += 1
else:
    print("loop finished")

# conditionals exercise refactored to a loop

while True:
    year = input("Enter the year you were born, or 0 to quit:")
    year = int(year)
    if year == 0:
        break
    elif year < 1946:
        print("too old to be categorised")
    elif year >= 1946 and year <= 1965:
        print(f"Born in: {year}: Baby Boomer")
    elif year >= 1966 and year <= 1976:
        print(f"Born in: {year}: Gen X")
    elif year >= 1977 and year <= 1994:
        print(f"Born in: {year}: Millenial")
    else:
        print(f"Born in: {year}: Gen Z")