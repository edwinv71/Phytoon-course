'''
modules are scripts imported for use in other scripts
packages are collections of modules (or sub-packages):
folder containing module scripts has an __init__.py file - 
NO contents, just __init__.py file created

there is a variant package called namespace package that does not require an __init__.py file

various types of modules
1. modules with standard Python core ("batteries included")
imported by default
no need to qualify eg. print()

2. modules in standard Python core
BUT you must import them directly and optionally, for example re (regular expressions)

3. modules you typically install on the command line using a package manager such as pip
from Python Package Index directory https://pypi.org
eg. conda by anaconda popular for data science

4. modules that we create and, optionally, open source
'''

import json

books = [
    {'title': 'The Gruffalo', 'author': 'Julia Donaldson'},
    {'title': 'The Twits', 'author': 'Roald Dahl'},
    {'title': 'The Bippolo Seed', 'author': 'Dr. Seuss'}
]

# python to JSON: json.dumps()

books_json = json.dumps(books)
print(books_json)
# [{"title": "The Gruffalo", "author": "Julia Donaldson"}, {"title": "The Twits", "author": "Roald Dahl"}, {"title": "The Bippolo Seed", "author": "Dr. Seuss"}]
print(type(books_json))#str

# JSON to python: json.loads()

print( books_python_again := json.loads(books_json))#loadS for string handling

with open("widget.json") as widget_file:
    # read contents into python dict
    a_dict = json.load(widget_file)#load for file handling
    print(a_dict)

    # edit dict data
    a_dict["widget"]["image"]["src"] = "Images/Moon.jpg"
    a_dict["widget"]["image"]["name"] = "moon1"
    a_dict["widget"]["text"]["onMouseUp"] = "moon1.opacity = (moon1.opacity / 100) * 90;"

# serialise and write to new file

with open("modified-widget.json", mode="w") as modified_widget_file:
    json.dump(a_dict, modified_widget_file)
