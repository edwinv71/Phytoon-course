object oriented language/00 languages-favour data and encapsulation in object structure-the dictionary stucture is akin to a literal object in other langauge. For java script object literal would be like {Lewis Korir}
JSON:
PY: dictionary:
{name: lewis korir}
object key are value pairs, comma separated, enclosed in curly brackets
As a complement to OOP is funtional programming.  Immutable data structures prefered that cannot change in the same way mutable objects can. 
Think of OOP as "save"-saves in place. Think of FP as Save as - saves a new copy with changes made. Neither oop nor FP are exclusive and play nicely together in most production apps.
## python versioning 
python was rewritten between versions 2 and 3. I.E code written in 3 will not run on the interpretter 2.
## Installing python
1. as REPL shell (Read Evalaute Print , Loop-One line at a a time to code larger cripts to check syntax)
2.Cript more:Writiing in an editor, save with the .py file extension, run in editort or from command line.
## python interpration
Python implemntation is not something we should concern ourselves with as it is to do with the underlying language. Python code using the standard implementaion of python (underlying language C) is intepratted. ie there is no sperate compile time stage to check for syntax errors. No performance optimisation at low level machine codde  but the IDE can still help us with suggestions that the code we right might nto work at run time

## editors
pycharm,spyder,idle.
we use visual studio code as it is fully featured and open source.

## DOCUMENTATION
python official docs are intended for those who have a level of proficciency in coding and can be hard to read as abeginner. They are excellent for those who pythin is not their first language. fORTUNATELY THERE ARE SEVERAL ALTERNATIVES like W3Schools.com is excelent for learning and Geeksforgeeks,org is exllent for looking up things as you go.If you want oto search for print funtion, try comnining it your serch string with the source eg geeks for geeks python  print() or w3 python  print()

## naming conventions
Variables and functions shouls be named  snake_case.
Classes should be in PascalCase or camel case
If you see a capital letter in python, there should be a class definition associated with that.
Python does not support consonants as such- variables that may not be reassigned but should indicate that the data should not be changed bu writiing them in SCREAMING_SNAKE_CASE.
Cooments should be whole sentences and terminated with a full stop and two spaces

All these are best practyices  and founting them doesnt mean your code won't run. It is best to just stick to them for reade
## identing and line splitting
identing is fundamental and denotes code blocks , lines of code belonging to a particular statement. Multiple statements may be written in one line semi colon separeted but SHOULD NOT - not typical.
e.g num1=1; num2=2
splits should happen if line lengths exceeds 89 characters or before.
3 ways
Technology_without_an_interesting _ name="TWAIN"
Technology_without_an_interesting _ name/
="TWAIN"
{Technology_without_an_interesting _ name/
="TWAIN"}
(Technology_without_an_interesting _ name/
="TWAIN")# see walrus operator
