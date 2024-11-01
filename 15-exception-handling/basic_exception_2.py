try:
    num1 = float(input("enter the first number:"))#ValueError
    num2 = float(input("enter the second number:"))
    result = num1 / num2#ZeroDivisionError
except ValueError:
    print("please enter digits and decimal point only")
except ZeroDivisionError:
    print("cannot divide by zero")
# we can chain an optional else just as in loops
# we can include a finally block
# the finally block will run whether or not an exception has been caught
else:
    print(f"result of {num1} divided by {num2} is {result}")
finally:
    print("thank you and goodbye")

print("carrying on regardless")