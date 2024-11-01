#standard builr in data types
#lierals/single values/expressions that evaluate to them. 
#they are immutable  by default
#eg. bool. or boolean and its values are True or false. Immutable and values cannot be change jusby refrencing
my_bool=True
my_bool= False # doesn't change tru to false. it is a reassignment of the same reference not a mutation of the value
#int. or integer/whole number value
#values: whole number, negative or positive, OR an expression that evaluates to a number
#immutable types(values cannot be change, just re refrenced)
my_int=1
#float. OR floating point number values
##values: whole number, negative or positive with dot character, OR an expression that evaluates to a number
#immutable types(values cannot be change, just re refrenced)
my_float=1.0
#str. (strings)
#values :any charcters of zero or more
#immutable type
#single,double OR tripled-quoted 
#zero indexed(from first character)
#have a length propoerty, obtained by using len()
my_str="Hello"
first_character_=my_str[0]
print(first_character_)#H
print(len(my_str))#5
#they are indexed 0-4
#string methods do not mutate originals
print(my_str.upper())
print(my_str)
#it does not change original but just rerencfrences 
#container types
#mutiple values
#mayb be of the same type but strickly do not have to BaseException#
#mutable by default
my_list=["bat","ball","gloves"]
print(my_list)
#access member read
print(my_list[0])
#update member
my_list[1]="cricket ball"
my_list.append("whites")#adds to the end of the list
print(len(my_list))

#tuple
#dtatype whose elements cannot be reassigned
my_tuple=("bat","ball","gloves")
my_tuple=("goal","football","games")#we have redifined tuple
#using tuples may appear that we can group related data togetheer
my_restaurant=("The ultimate answer",42)
#in pyhton any python maybe updated

#Sets
#values; CAN BE OF ANY TYPE
#cannot contain duplicates
#powerful ways of dtermining sets and returning differences and similarities

#declared with curly braces
my_set={1,22,3,4,5,5}
print(my_set)#1,3,4,5,22
my_varied_set={"one",1,True}
print(my_varied_set)#one,1#true disapears as true is equated to 1
my_varied_set={"one",0,True}
print(my_varied_set)#0,one,true
print(bool(1))#true

print(bool([]))#False
print

#dict(dictionary)
#values :key:value pairs
#keys:maybe of any type but are commonly strings
#keys must be unique
#mutable
#python dict is NOT the same as an object
#not the same as dicts even though both are in curly braces 
#object are made by classes
#the way we drill down into the properties is different
#theroriticall everything is an object in python
my_dict={"name":"Fred","age":21,"employed":True}
print(my_dict)

#no type
my_none=None
print(type(my_none))
#means that the reference is associated with it points nowhere
#null, in other languages
#if it did reference any of the other types, it doesn't anymore

#Exercice 2

