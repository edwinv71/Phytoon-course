name = input ("Enter your name:")
print (name)
age = input ("What is your age?")
print(age)
print ("My name is ",name,".I am ",age,"years old")
print ("My name is "+name+".I am "+age+"years old")#string conncurtination and can only work for a string
age = int (age)# corced data type

##placeholder. Python 3
print ("name:{} Age next birthday:{}".format(name,age+1))
#python 3.5
print(f"name:{name}. Age next birthday:{age+1}")
#python 3.7
print(f"""
      name:{name}
      age next birthday :{age+1}""")
#my_float = 21.0
#print(type my_float)#class float. if my_float = 21 without decimal, classifies as int
int_from_user = input ("enter a number")
#if decimal point added
print(type(int_from_user)) #str
#float_from_user = float (int_from_user)
print(type(int_from_user))
raedy_made_float=float (input("Enter a number"))
print(type(raedy_made_float))

#variables and data type