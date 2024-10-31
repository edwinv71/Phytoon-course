'''
conditional statements are very smilar in Python to other languages,
they execute a block of code depending on whether a condition evaluates True or False
if True:
    code block, defined by indent, immediately following is executed
if False:
    skipped

an else block has NO condition and means, really ANYTHING else

you can test multiple conditions using if elif else

following execution of a branch the interpreter steps out of the statement structure, like a break

so when using ranges of values, if..elif blocks should be arranged with care to avoid unreachable code

Since recently in Python 3.10 there is another decision control statement
Called Structural Pattern Matching or match case
This mimicks the behaviour of switch in Java and JS, which traditionally has had no equivalent in Python
The match statement tests a single variable or expression for equality

'''

# single branch IF
if False:
    print("true path executed")

# single branch IF
if False:
    print("true path executed")
else:
    print("else block executed")

# two or more branches IF-ELIF-ELSE

if False:
    print("first IF executed")
elif True:
    print("second IF executed")#exits here, else not executed
else:
    print("else block executed")

# if-else on one line pythonesque alternative to ternary operator in other languages
# concept: its one thing or another. A hard choice, an XOR gate in electronics
temp = "cold"
temp = "scorchio"
clothing = "jumper" if temp == "cold" else "T-shirt"
print(clothing)

#  ranges
hr = 150
bp = {"diastolic": 150, "systolic": 100}

if hr < 130 and bp["diastolic"] < 130:
    print("healthy individual")
elif hr < 160 and bp["diastolic"] < 160:
    print("you should ring your GP for a checkup!")
else:
    print("you should go to A&E!")