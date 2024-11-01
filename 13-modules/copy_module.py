'''
when we copy VALUES (bool, str, float, int) which technically are objects too
(everything is an object in Python)
we may easily break the original reference to the value and cretae a new one
when however we copy REFRENCES to collections of data (dict, list, tuple, set)
we may still have FURTHER NESTED REFERENCES in the original data.

These do not break the link to the original. 

Therefore the original may be mutated through the copied reference.
In most cases this is undesirable.
'''

my_list = ["Lewis", "Edwin", "Alan"]
my_copied_list = my_list

my_copied_list.append("Shveta")
print(my_copied_list)
print(my_list)#['Lewis', 'Edwin', 'Alan', 'Shveta'] original changed

# there are many ways ANY programming language will try to get round this

# Python modules are extremely powerful and provide the best, quickest, and most comprehensive solution

#  the copy module may run to thousands of lines of code
# we call it very simply:
import copy

#OR
from copy import copy, deepcopy

# we want a copy of the list with all original references broken
my_copy = copy(my_list)
my_copy.append("Euan")
print(my_copy)#['Lewis', 'Edwin', 'Alan', 'Shveta', 'Euan']
print(my_list)#['Lewis', 'Edwin', 'Alan', 'Shveta']
# original unchanged
#  but actually, my_copy is still a shallow copy AT MORE THAN ONE LEVEL OF RECUSION!
my_dict = {"names": my_list}
my_dict_copy = copy(my_dict)
my_dict_copy["names"].append("Akheela")
print(my_dict_copy)#{'names': ['Lewis', 'Edwin', 'Alan', 'Shveta', 'Akheela']}
print(my_dict)#{'names': ['Lewis', 'Edwin', 'Alan', 'Shveta', 'Akheela']}
# copy() from the copy module is a shallow copy past one level of nesting
# deepcopy() from the copy module fixes this for ANY level of recursion in ANY object
# 
my_dict_deepcopy = deepcopy(my_dict)
my_dict_deepcopy["names"].append("Hamza")
print(my_dict_deepcopy)#{'names': ['Lewis', 'Edwin', 'Alan', 'Shveta', 'Akheela', 'Hamza']}
print(my_dict)#{'names': ['Lewis', 'Edwin', 'Alan', 'Shveta', 'Akheela']} original unchanged

