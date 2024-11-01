# execute from the command line, ensure cursor is in this directory

file = open("data.txt")#path must be fully qualified
print(type(file))#<class '_io.TextIOWrapper'>

# 1. read (whole file or a specified no/ of characters)
file_contents = file.read()
print(file_contents)
file.close()

# 2. open, limit characters
print("partial read of file")
file = open("data.txt")#need to open closed file again for reading
print(some_of_file := file.read(100))#ValueError: I/O operation on closed file.
file.close()

# 3. readline
print("one line of file")
file = open("data.txt")
print(line := file.readline())
file.close()

# 4. readlines
print("line by line of file")
file = open("data.txt")
print(lines := file.readlines())#returns list of strings
file.close()