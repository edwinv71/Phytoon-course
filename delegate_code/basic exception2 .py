try:
    num1 = float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))
    result = num1 / num2
    print(f"division of {num1} and {num2} is {result}")
except ZeroDivisionError:
    print("cannot devide by zero")
else:
    print (f"result is {result}")
finally:
    print("thank you")

    print("carry on regardless")