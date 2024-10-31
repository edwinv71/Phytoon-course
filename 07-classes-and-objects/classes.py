'''
a class is
a BLUEPRINT or TEMPLATE for
creating objects of a certain user-defined type
there exist many system classes such as string and list
when we create our own classes, however, we create our own types
you may choose classes over dictionaries to represent complex data
as every instance of the class will have 
the same fields (variables) and
the same methods (functions)
whereas if we used dictionaries, every usage has to be defined again
classes enforce standards applied by all objects of taht class
'''

class Client:
    def __init__(self):#constructor
        self.name = "Client name"
        self.email = "your email"
        self.dependents = []

client1 = Client()
# UNLIKE dictionaries' square bracket notation
# an object's props are referenced with dot notation
print(client1.name)
print(client1.email)
print(client1.dependents)

# setting object props
client1.name = "Alan"
client1.name = "alan@alan.com"
client1.dependents = ["person1", "person2"]
client1.dependents.append("sophie")
client1.dependents.append("susie")

class Client:
    def __init__(self, name_from_user, email_from_user):#constructor
        self.name = name_from_user
        self.email = email_from_user
        self.dependents = []
# each version of the Client class here overwrites the last
# this script is therefore procedural (top to bottom)
# more usually in Python, classes are in mdoules, alongside functions
# and the modules are called from a procedural script
class Client:
    def __init__(self, name, email):#constructor
        self.name = name
        self.email = email
        self.dependents = []

# client2 = Client()#TypeError: Client.__init__() missing 2 required positional arguments: 'name' and 'email'
client2 = Client("Alan", "alan@alan.com")#TypeError: Client.__init__() missing 2 required positional arguments: 'name' and 'email'
print(client2.name)
print(client2.email)
print(client2.dependents)
print(client2)#<__main__.Client object at 0x100ab8d10>
# program quit and relaunched:
# <__main__.Client object at 0x10253cd10>
my_list = [1,2,3]
print(my_list)#[1, 2, 3]
# the list CLASS overrides the dunder method __str__
# it provides a string representation of the object
# if we want our own custom objects to have this behaviour we must implement it ourselves
class Client:
    def __init__(self, name, email):#constructor
        self.name = name
        self.email = email
        self.dependents = []
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, dependents: {self.dependents}"
    
client3 = Client("Ben", "ben@ben.com")
print(client3)#meaningful string representation of the object
# there are a LOT of dunder methods

# custom methods
class Client:
    def __init__(self, name, email):#constructor
        self.name = name
        self.email = email
        self.dependents = []
    def add_dependent(self, name):
        # there is little point in writing custom setter methods for fields if we do not implement business logic
        # for example, a dependent must not already exist
        if name not in self.dependents:
            self.dependents.append(name)
        else:
            print(f"{name} already added")
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, dependents: {self.dependents}"

client4 = Client("Euan", "email")
client4.add_dependent("dependent_name")
print(client4)
client4.add_dependent("dependent_name")
print(client4)
