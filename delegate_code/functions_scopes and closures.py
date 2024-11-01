#scope defined the visibikity and lifespan of a variable .
#local scope ;-declared within a function
# visible within the function or its blocks
#globa scopes
#-visible outside of any fucntions
#-lives whilst the wholw script is exucuting.
#-pure funtions; accepts copies of dat , always return the same thing every time for given same input
#imoure funtions :have global dependancies on other functions/variables

next_num=1#global

#impure function
def get_next_num():
    return next_num

print(get_next_num())
next_num=2
print(get_next_num())

#pure funtion
#idempotenet and no global dependancies.
#passes in a acopy of global data
def get_next_num_pure(next_num):#pass in a copy of data
    return next_num

print (get_next_num_pure(next_num))
next_num=3
print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))

#if we wish to update global state from within a function, we must bind the global state with a global keyword
def increment_next_num_impure():
    return next_num+1

print(increment_next_num_impure())


##function with local variable 
