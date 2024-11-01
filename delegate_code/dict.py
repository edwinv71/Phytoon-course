#a dict is a mutable unordered container of key:values
#keys must be unique and ideally immutable
#values may be duplicated
#creation
book = {}
print(type(book)) #class dict

book_as_set ={"bok1","book2"}
print(type(book_as_set)) #class set

# way 2 
book =dict()

#adding props after instantation
book["title"] = "scary smart"
book["author"] = "Mo Gawdat"
book["published"]=2019
print(book)

#ther dict method
print (published_year := book.pop("published"))#muatates oringinal and returns popped key
print(book)

#iterating usinf keys to access values
#key_and_values
for key in book:
    print(key)#key in the abcense of any other method, a loop wil acess keys

    #values
for  value in book.values():
    print(value)

#keys and values
for key,value in book.item():
    print(key,value)

#using keys to access values
for key in book:
    print(f"{key}: {book[key]}")

