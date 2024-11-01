"""
for a user POV exceptional handling enables the code to recover and continue to carry from a catastrophic event
"""

num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
total = num1 + num2
print(f"sum of {num1} and {num2} is {total}")

#try 
try:
    num1 = float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))
    total = num1 + num2
    print(f"sum of {num1} and {num2} is {total}")
except:
    print("oops something went wrong")
