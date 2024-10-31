'''
functions, as in any other language, wrap one or more LOC in a function name
to be called zero, one, or many times at some time in the future
functions are commonly defined in a script ON THEIR OWN, with no runtime code
the script with the runtime code in it, that USES the functions,
is separate, and IMPORTS them from the first script
the first script is called a module

how short can a function be?
1 LOC
why? to make code more declarative
the function name may be more descriptive than its workings
how long can a function be?
Not too long.
As a rule of thumb I would be wary of functions over 50-100 LOC
It is very likely they will have dependencies on other code.
If that other code were to break, so would your function.
You may never know this while unit testing
'''

def add_two_numbers(num1, num2):#parameters at function definition time - placeholders for data
    return num1 + num2

add_two_numbers(2,2)#argumantes (args) at runtime - actual data

print(add_two_numbers(2,2))

def print_two_numbers(num1, num2):#parameters at function definition time - placeholders for data
    print(num1 + num2)

print(print_two_numbers(2,2))#None
print_two_numbers(2,2)

# 1. no input, no output
# print("Hello")
# print("from greet1")
# print("How are you today?")

def greet1():
    print("Hello")
    print("from greet1")
    print("How are you today?")

greet1()#only see the terminal output when function is called

# 2. no input, output
def greet2():
    return "Hello\nfrom greet2\nHow are you today?"

print(greet2())

# 3. input and output
def greet3(name):
    return "Hello\n" + name + " from greet3\nHow are you today?"

# print(greet3())#TypeError: greet3() missing 1 required positional argument: 'name'
print(greet3("Alan"))#

# 4. input, no output
def greet4(name):
    print("Hello\n" + name + " from greet4\nHow are you today?")

greet4("Ben")

# named args
# all the above, to be precise greet4 and greet3 that take an argument, do so by positional

# 5. input and output, positional args
def greet5(name, age):
    return f"Hello {name}, you are {age + 1} next birthday"

print(greet5("alan", 59))
# print(greet5(59, "alan"))#TypeError: can only concatenate str (not "int") to str

# 6. input and output, named args
def greet6(name="person", age= 30):
    return f"Hello {name}, you are {age + 1} next birthday"

# print(greet6())# it runs with no args, default ones supplied
# print(greet6(age=59, name="Alan"))# it runs with args in a different order

if __name__ == "__main__":
    # code HERE will not execute in the importing script
    print(greet6())# it runs with no args, default ones supplied
    print(greet6(age=59, name="Alan"))# it runs with args in a different order


