#TODO can we convert container type eg dict to int or float
my_dict = {"age": 21}
print(type(my_dict))#<class 'dict'>
# my_dict = float(my_dict)#TypeError: float() argument must be a string or a real number, not 'dict'
# my_dict = int(my_dict)#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
my_dict_key = int(my_dict["age"])
print(type(my_dict_key))#<class 'int'>
my_dict_key = float(my_dict["age"])
print(type(my_dict_key))#<class 'float'>