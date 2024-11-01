#while loops and for loops
#for loop length of the container is known
#while loop-when number of iterations is not known beforehand.
#for loops generally used for iterating over the containers#length of the container(len()) is known in advance
names=["JACK","JANE","paul","jimmy"]
for name in names:
    print (len(names))


#list slicing and loops
#a list returns a new list , picked from original , with upto 3 args:
#strat index inclusive and end index exclusive
#when slicing to the very end of a list we put put it end imdex as length of list
print("list slicing 1")
for name in names[2:4]:
    print(name)
print("slicing list 2")
for name in names[0:4:3]:
    print(name)
print("slicing list 3")
for name in names [::-1]:#reordering
    print(name)


#dictionaries
names_as_dictionary={
    "politicians":["Gordon Brown"," David Hume"],
    "musicians":["Michael Jackson","Sauti Sol"],
}
#Values
for value in names_as_dictionary.values():
    print (value)
#both keys and values
for key,value in names_as_dictionary.items():
    print(key,value)

    #using a range funtion to control no of iteration
 #for i in range (1,11):
        #print (i)


#for i in range (1,11):
        #print (i)

counter=0
while counter<len(names):
if name[counter]=="paul"
counter+=1 #otherwise infinite loop
#break
print (names[counter])