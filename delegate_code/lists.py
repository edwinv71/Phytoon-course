#a list is a mutable index or ordered container
#permits duplicates commonly used to store elements of the same type

#Creation
nums =[]
nums = list()
nums = [1,2,3]

#elemts referencing 
print(nums[2])

#element reasiigning
nums[2]= 4

#adding elements
nums.append(5)

##slicing-creation of a new list from all or part of an rinigal list
print(nums)

#slice syntax: [startidx: endIdx: 2]
#note endidx is exclusieve (one beyond what you need)
fib = [0,1,1,2,3,5,8,13,21,34]
print(len(fib))

#givr me between values 3 and 21 inclusive
print(fib[4:9:1])

#if we wanted to save and print we would traditionaly require two steps
slice1= fib[4:9]
print(slice1)

#suing the walrus
#print(slice1 = fib[4:9]) eroor
print(slice1 :=fib[4:9])

#13 till end
print(slice1 :=fib[7:])

#all list slicing is immutable


#built in funtions for lists
print(f"number of elements: {len(fib)}")
print(f"number of elements: {min(fib)}")

#buuilts in using dir( function)


#we may multiply lists
print(list6:= slice1+[0,0,0,0])

#we may multiply lists
print(list7:=slice1*10) # doesn't mutiply elements but gives us the same list 10 times over.

#return key index value pairs using the enumerate function
for index, element in enumerate(fib):
    print(index,element)
    

#list comprehension enables us to pass in a loop function
#to transform elements of a list#it returns a new list with transformations applied

#scalling
scaled_list = [element*2 for element in fib]

print(scaled_list)
#akin to a map function in other languages

#filter original list for numbers <10
print(under_10 := [element for element in fib if element <= 10])
