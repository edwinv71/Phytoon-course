#TODO - different ways of importing
# way 1: whole module
import functions_exercise_module
# functions must be referenced with fully qualified name
# usage:
print(functions_exercise_module.get_greeting("Alan"))#should rename first two functions in module
# pros: you know exactly which function is being called 
# you know exactly what module is being called
# cons: fully-qualified names can be tedious when repeatedly called in the importing script

# way 2: named imports (best way imo)
from functions_exercise_module import get_product #note: no invocating brackets
# functions individually named in import line
# usage:
print(get_product(2,2))
# pros - you can see exactly which functions from the module are used
# you don't have to repeat the module code
# cons - if your code that calls the functions is a million miles away from the import statement 
# (usually at the top of the script importing)
# function may look like a local one

# way 3: the wildcard *, (worst way of all 3 imo)
from functions_exercise_module import *
# the wildcard is used, meaning all functions
# usage:
print(get_first([1,2,3]))
# pros: much faster to write during development
# cons: you have absolutely no clue which functions come from a module

# NONE of the different ways have a perf benefit over the others
# you are only SYMBOLICALLY linking to module code