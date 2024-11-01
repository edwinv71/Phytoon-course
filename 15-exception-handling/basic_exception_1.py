"""
   from a user POV, exception handling enables the code to recover
   and carry on from a catastrophic event
   from a dev POV, it enables us to create and raise Errors 
   (objects with information about the problem)
   according to business logic 
   exceptions should be seen as creating opportunities
   (for our system to intervene)
   not so much as presenting difficulties
"""
try:
    num1 = float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))
    total = num1 + num2
    print(f"sum of {num1} and {num2} is {total}")
except:
    print("oops something went wrong")

print("carrying on regardless")