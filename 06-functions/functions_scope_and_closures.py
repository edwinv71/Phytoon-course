'''
scope defines the visibility and lifespan of a variable
local scope:
-   declared within a function
-   visible only within the function or its blocks
-   lives and dies with the function execution
global scope:
-   declared outside of any functions
-   visible to all functions in the script
-   lives whilst the whole script is executing
-   pure functions: accept copies of data, 
-   ALWAYS return the same thing EVERY time, for given same input
-   impure functions: have global dependencies on OTHER functions/variables,
-   do not always return same result for same given input

'''

next_num = 1 # global

# impure function
# NOT idempotent
# has global dependency
def get_next_num():
    return next_num

print(get_next_num())
print(get_next_num())
next_num = 2
print(get_next_num())

# pure function
# idempotent
# no global dependencies
# passes in a COPY of global data
def get_next_num_pure(next_num):#pass in a COPY of data
    return next_num

print(get_next_num_pure(next_num))
next_num = 3
print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))

def increment_next_num_pure(next_num):#pass in a COPY of data
    return next_num + 1

print(increment_next_num_pure(next_num))
print(increment_next_num_pure(next_num))
print(next_num)#still 3 - only the COPY is incremented

# if we wish to update GLOBAL STATE from within a function we must BIND the global state with the global keyword
def increment_next_num_impure():#pass in a COPY of data (same function definition as before)
    return next_num + 1

print(increment_next_num_impure())
print(next_num)#still 3

def increment_next_num_impure():#pass in a COPY of data
    return next_num + 1

# # function with local variable state
def increment_global_num():#BIND to global data
    global next_num
    # print(next_num)
    next_num += 1
    return next_num

# increment_global_num()#3

print(increment_global_num())
print(increment_global_num())
print(increment_global_num())
print(next_num)# value 6

# so to summarise, binding the function scope to the gloabl scope using the keyword global
# means a function can affect the scope above it
# similarly, we may RETURN a function from another function
# if the OUTER function has a variable/variables in it, these are said to be lexicall-scoped
# that is, when the inner function was returned, it captures a reference to the outer function's scope
#######################################################################
# this enables functions to have memory from one invocation to the next
#######################################################################
# these are called closures

# define a closure
def increment_with_closure():
    # this scope is local to the outer function
    # but EFFECTIVELY GLOBAL to the inner function
    next_num = 100 #lexically-scoped variable
    # return an inner function:
    def get_next_num():
        # next_num = 1#to get this to work locally we must initialise the LOCAL next_num
        nonlocal next_num#this BINDS the value of next_num to the outer function value
        next_num += 1
        return next_num
    return get_next_num
    
# create a closure
my_closure = increment_with_closure()
    
print(my_closure())
print(my_closure())
print(my_closure())

# reset: create a new closure
my_closure = increment_with_closure()
    
print(my_closure())
print(my_closure())
print(my_closure())
