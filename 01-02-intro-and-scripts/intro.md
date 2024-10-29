# Introduction to the Python language

## Introduction and History

Python: not named after snakes, but after Monty Python TV show.

Guido van Rossum, Python's creator was a huge Monty Python fan. There are still obscure references to Monty Python humour in the official docs.

Object-oriented language, arguably easier to learn than Java,

OO languages:
Favour data encapsulation in object structures (for PYTHON, THE DICTIONARY STRUCTURE IS AKIN TO A LITERAL OBJECT IN OTHER LANGAUGES) apologies for caps lock!

JS: object literal:
{ name: "Alan",
age: 59}
JSON:
{ "name": "Alan",
"age": 59}
PY: dictionary:
{ name: "Alan",
age: 59}

objects: key: value pairs, comma separated, enclosed in curly braces{}

as a complement to OOP (Object Oriented Programming) is

## Functional Programming, or FP

Immutable data structures preferred, that cannot change in the same way mutable objects can.

Think of OOP as "Save" - save sin place

Think of FP as "Save As" - saves a new copy with changes made.

Neither OOP NOR FP are exclusive! They play nicely together in most production apps.

## Python versioning

Python was re-written between versions 2 and 3. Strangely for a language, this was a BREAKING CHANGE. Code written in 3 > will not run on the 2 interpreter.

Most of what we do hasn't changed much since 3.5. But best to install latest version from python.org/downloads

Once installed, run two ways: - 1. as REPL shell (Read, Evaluate, Print, Loop) - one line at a time, always useful as you code larger scripts to check syntax - 2. script more: write in an editor, save with the .py file extension, run in editor or from command line.

## Implementations

A Python implementation is not something we should concern ourselves with as it is to do with the underlying language.

Python code, using the standard implementation of CPython (underlying language is C) is interpreted - ie theree is NO separate compile time stage to check for syntax errors. No performance optimisation at low-level machine code, but the IDE can still help us with suggestions (that the code we write MIGHT not work at runtime).

## Editors

PyCharm, Spyder, Idle (after Eric Idle), used to ship with Python install, Visual Studio (paid Microsoft.net environment), Visual Studio Code (Open Source), IntelliJ IDEA, Webstorm, Eclipse, Sublime, Atom.

We use Visual Studio Code a sit is fully-featured and open source.

## Documentation

The Python official docs are intended for those who already have a level of proficiency in coding, and can be quite hard to read as a beginner. They are excellent for those for whom Python is not their first langauge.

Fortunately there are several alternatives. W3Schools.com is excellent for learning, and GeeksForGeeks.org is excellent for looking things up as you go. More detail tahn W3Schools, but less in depth than Python docs.

If yoiu want to serach for, say the print() function, try combining it in your search string with the source eg
"geeksforgeeks python print()"
"W3 python print()"

## Naming conventions

Variables and functions should be named snake_case.

Classes should be named in PascalCase (CamelCase).

So if you EVER see a capital letter in Python, tehre should be a class definition associated with that.

Python does not support constants a ssuch (variable taht may not be reassigned) but should indicate that the data should not be changed by writing them in SCREAMING_SNAKE_CASE.

Comments should be whole sentences, sentence case, and terminated with a full stop and two spaces.

All these are BEST PRACTICE, and flouting them doesn't mean your code won't run, it's just best to sticj to them for readability.

All these things are not manadatory, but to ignore them is to code in a non-Pythonesque way.

## Indenting and line-splitting

Indents are fundamental to Python and denote code blocks (LOC belonging to a particluar statement).

Each statement in Python is terninated by the new line character.

Multople statement MAY be written on one line semi-colon separated, but SHOULD NOT - not typical.

e.g. num1 = 1; num2 = 2

splits should happen if line length exceeds 89 characters or before

3 ways:

technology_without_an_interesting_name = "TWAIN"
technology_without_an_interesting_name /
= "TWAIN"
{technology_without_an_interesting_name
= "TWAIN"}
(technology_without_an_interesting_name
= "TWAIN") # see Walrus operator, probably most readable
