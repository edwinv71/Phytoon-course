'''a tupple is and immutable index ordered container
it permits duplicates
it is commonly used to store different types of data together such as that returned from fucntion
ensures that data cannot be moddified'''

my_tupple = ("lewis",21,["walking","photography"],True)
fib = (0,1,1,1,2,3,5,8,21,34,55,89,144)

#tupple methods
print(fib.count(1))
print(fib.index(144))

#we would slice tupples as we would lists
#returns another tupple
print(low_numbers:=fib[:6]) #end index (0, 1, 1, 1, 2, 3)


#we can iterate tupples 
for el in fib:

    print(el)

#we can renumerate
for index, element in enumerate (fib):
    print(index,element)

#tupple arithmentic
print(fib + ("whendy",True, 377))
print(fib *2)

fib = fib +(233,377)
print (fib)

#looks here that the original is mutated when reassgined, item reassignment is the immutable bit