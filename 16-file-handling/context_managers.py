# execute from the command line, ensure cursor is in this directory

with open("data2.txt") as file:
    for line in file:
        print(f" a line: {line}")

# no need to close
# no need to call read methods
# the file is the context (hence name context manager)
# __enter__ and __exit__ methods are called under the hood
# instead of having try-except blocks to handle errors
# the __exit__ method will handle ALL exception handling code
# so no need to write exception handling!
# plus, optionally, we may write our own context managers