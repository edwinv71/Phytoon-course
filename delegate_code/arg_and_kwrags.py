'''
args -multiple positional arguments denotedin parens as *args
the* is mandatory

kwargs-multiple named keyword arguments denoted in parens as **kwargs
the args is arbitrary
the ** ins mandatory
'''

#args-zero,one or more arguments are packed inti a tupple
#this parameter must come after any other positional parameters
def greet(name,hobbies):
    print(f"Hello, my name is {name} and my hobies are {hobbies}")

greet("Alan","Photography,film, music, food")

#passing as seprate variables
greet("Alan",["Photography","film", "music", "food"])


## **kwargs - zero, one or many named arguments get packed into a dictionary
#must be after single *agrs in parameter list
def greet(name,*hobbies,**other_details):
    print(f"Hello, my name is {name} and my hobies are {hobbies} and I live at {other_details}")

greet("Billy No gates")
greet("Alan","photography","film", county="Donegal",country="ireland")

##doc strings
#a doc string is atriple quoted (double or single doesn't matter) comment as the first few lines of the 