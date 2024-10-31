def get_greeting() -> str:
    return "G'Day"

def get_greeting(name: str) -> str:
    return "G'Day " + name

def get_product(num1: float, num2: float) -> float:
    return num1 * num1

def get_first(a_list):
    return a_list[0]

def get_name(a_dict):
    return a_dict["name"]

def get_circumference(radius):
    return 2 * 3.14 * radius

def print_first(a_list):
    print(a_list[0])

def print_name(a_dict):
    print(a_dict["name"])

def print_circumference(radius):
    print(2 * 3.14 * radius)
