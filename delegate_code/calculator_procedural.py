total=0

def add(num):
    global total
    total+=num
    
def sub(num):
    global total
    total-= num

def mul(num):
    global total
    total*= num
    
def div(num):
    global total
    total/=num

def equal():
    global total
    return_value=total
    total=0 #reset total
    return return_value


add(5)
sub(2)
mul(3)
div(9)

print(equal())
print(total)