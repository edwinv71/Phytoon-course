'''
args - multiple positional arguments
denoted in parens as *args
the args is arbitrary
the * is mandatory

kwargs - multiple named (keyword) arguments
denoted in parens as **kwargs
the kwargs is arbitrary
the ** is mandatory
'''

# *args - zero, one, or more arguments are automatically packed into a tuple
# this parameter MUST come after any other positional parameters
def greet(name, hobbies):
    print(f"Hello my name is {name}")
    print(f"My hobbies are {hobbies}")

greet("Alan", "Photography, film, music, food")
greet("Alan", ["Photography", "film", "music", "food"])

def greet(name, *hobbies):
    '''
    A function to accept a name and a list of hobbies
    '''
    print(f"Hello my name is {name}")
    print(f"My hobbies are {hobbies}")#packed into a tuple
greet("Alan", "Photography", "film", "music", "food")
greet("Billy No Mates")

# **kwargs - zero, one, or many named arguments get packed into a dictionary
# must be after *args in parameter list
def greet(name, *hobbies, **other_details):
    """This function bla bla...

    Args:
        name (str): bla bla...
    """
    print(f"Hello my name is {name}")
    print(f"My hobbies are {hobbies}")#packed into a tuple
    print(f"I live at {other_details}")#packed into a dict

greet("Billy No mates")
greet("Alan", "photography", "film", county="Donegal", country="Ireland")

#  DOCSTRINGS
# a doctsring is a triple-quoted (double or single doesn't matter) comment as the first few lines of a function
# it gets picked up by interactive help
# properly formatted, it may pass on info about arguments and return types
def function_for_docstring_demo(name, age):
    """_summary_

    Args:
        name (_type_): _description_
        age (_type_): _description_

    Returns:
        _type_: _description_
    """
    return f"{name} : {age}"
