#Raw strings 
#sometimes escape characters need to be printed literally, e.g in a file path
#C:\users\alan
#print(C:\users\alan) this brings an error

#instead we can wite a arw sring
print(file_patyh := r"C:\users\alan") # this works

#print(waving_hand := '\U+1F44B') 'error'
#print(waving_hand := '\U0001F44B')

s1= "hello"
s2= "hello"
print(s1,id(s1))
print(s2,id(s2))
#strings are immutables and there ids will be the same

#list are mutable
list1= ["hello"]
list2= ["hello"]
print(list1,id(list1))
print(list2,id(list2))
#list1 and 2 are stored in differnent location