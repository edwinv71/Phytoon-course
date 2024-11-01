def add_two_numbers(num1,num2)
    return num1+num2
add_two_numbers((2,2))
print(add_two_numbers2,2)


###no input no output
print("hello")
print("how are you")

def gree1():
    print("hello")
    print("How are you")

#greet1()#on;y see the teminal output when function is calle

#2.no input but with output
def greet2():
    return"Hello\nfrom greet2\nhow are you?"
print(greet2())

#3.input and output
def greet3(name):
    return "Hello\n"+ name + "from greet3"
    

#named arguments
##all the above greet 3 and greet 4 take an argument and do so by positional arguments.
#5.input and output, positional arguments.
def greet5(name,age):
    return f"Hello {name}, you are {age+1} next birthday"
print(greet5("alan,59"))
#print(greet5("59,alan")) type error arguments are interchanged.

#named argments
def greet 6(name="person", age=30):# runs with no arguments , default ones provided

    return f"Hello{name},you are {age+1} next birthday"
