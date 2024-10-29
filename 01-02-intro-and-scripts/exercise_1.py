# 1. Create a script named exercise1_console_io.py.
# 2. Prompt the user to input his/her name and capture it in variable named name.
# 3. Prompt the user to input his/her age and capture it in a variable named age.
# 4. Print the user's name and age to the console. You might try doing this with one
# invocation of the built-in print function.
# 5. Execute the script in VSC.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(name, age)

print(type(name))#<class 'str'>
print(type(age))#<class 'str'>

print("Name:", name, "Age:",age)
print("Name:" + name + "Age:" + age)#name and age are still strings
# print("Name:" + name + "Age next birthday:" + age + 1)#TypeError: can only concatenate str (not "int") to str
age = int(age)#coerced data type str to int
print(type(age))#<class 'int'>
print("Name: " + name + " Age next birthday: " + str(age + 1))#Python2 old school

# PLACEHOLDERS, Python 3 >
print("name: {} \nAge next birthday: {}".format(name, (age + 1)))

# PLACEHOLDERS, Python 3.5 >
print(f"name: {name} \nAge next birthday: {age + 1}")

# PLACEHOLDERS, Python 3.7 >
print(f"""
name: {name} 
Age next birthday: {age + 1}""")

my_int = 21#encodes as int as there is no decimal place
print(type(my_int))#<class 'int'>
my_float = 21.0#encodes as float
print(type(my_float))#<class 'float'>

int_from_user = input("Enter a number")
# ValueError: invalid literal for int() with base 10: '20.0'
# if decimal point added
print(type(int_from_user))# str
# int_from_user = int(int_from_user)
float_from_user = float(int_from_user)
print(type(float_from_user))

# a lot of Python devs would do this:
ready_made_float = float(input("Enter a number"))
print(type(ready_made_float))
# not recommended for error handling
# because the input() function will NOT cause the rror
# but the conversion to float will
# so a better way:
float_as_str = input("Enter a number")#this line will not error
float_as_str = float(float_as_str)#this line may error and should be separate therefore

