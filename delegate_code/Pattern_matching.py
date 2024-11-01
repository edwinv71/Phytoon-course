# execute from the command line,ensure cursor is in this directory
file = open ("")#path must be fully qualified

#1.read whole file or a specified number of characters
file_contents = file.read()
print(file_contents)
file.close()

#2.open,limit characters
file = open ("")
print("partial read of file")
print (some_of_file := file.read(100))# read only 100 characters
file.close()
#.3. read line 
file.open("")
print (line := file.readline())
file.close()


#4.read lines
file.open("")
print (lines := file.readlines())# returns list of string
file.close()