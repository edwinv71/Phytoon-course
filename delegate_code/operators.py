#symbols that perform operations
#x=1
#x=x+1
#fist assigns x to 1
#second assigns the result of an expression-itself plus 1
#the expression has two operators 

#arithmetic operators
#+
#-
#* multi[lication
#** exponent eg 2**3 is 2 cubed
#/division
#%modulo-reminder, whole number devieion
#// -quatient , whole number division
#print(10%2)
print(f"formatted:{10/3:.2f}")
#promotion is the act of storing smaller data types in larger ones.
print(10/3)# float result, int operands
print(9+2)#int result
print(9+2.0)#float reult-promoted to float

###no numeric arithmentic
print("ho"*3)
print("*"*1000)


#assignment operators
#= is a single assignment 
#+= is compound assignment
##works for strings and numbers
my_num=1
my_num+=1
my_num+=1
print(my_num)

my_string=""
my_string+="I"
my_string+="love"
my_string+="python"
print(my_string)#ilovepython

#walrus operator:=
#assigns and return at the same time
#before walrus
x=1
print(x)
#print(x=2) #TypeError: 'x' is an invalid keyword argument for print()

#with walrus
print(y:=2)
#assigns and returns in the same statement


#/inreament and decreement operators do noe exist in python. ie ++,--
#so we just say x=x+1 or x+=1
#mutiple assignment is not very python esque
#x=1;y=2;z=3
#a better way is af follows
x,y,z=4,5,6
#eqiuvalent in JS is distrucuring

##dictionaries
my_dict = {"name":"Lewis","age":30}
name,age = my_dict["name"],my_dict["age"]
# note square brackets notation for dict props

#List
my_num=[1,2,3,4]
first,second third,forth = my_num[0],my_num[1]


#assignment operator chaining (more specialised, avaoid writing)
x=1
y=1
#same as 
x=y=1

#comparison operators
#<= less tha or equal to
#!= not equal
#is  tests the identity

my_list =[1,2,3]
my_other_list = [1,2,3]
print(my_list is my_other_list) #false

#system why python uses to determine if two variable reference is built in id()
print(id(my_list))
print(id(my_other_list))##my list and my other list ids are different and one is not a copy of the other. Because it copies the reference it is called a shallow copy. The original can be muteted to a new refrence


#best way
import copy
my_deep_copied_list = copy.deepcopy(my_list)
my_deep_copied_list.append(5)
print(my_deep_copied_list)#1,2,3,5
#the original is unaffected as previous.