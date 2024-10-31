total = 0

def add(num):
    global total
    total += num
    
def sub(num):
    global total
    total -= num
    
def mul(num):
    global total
    total *= num
    
def div(num):
    global total
    total /= num
    
def equals():
    global total
    return_value = total
    total = 0
    return return_value

if __name__ == "__main__":
    add(5)
    print(total)
    sub(2)
    print(total)
    mul(3)
    print(total)
    div(9)
    # expected: 1.0
    print(equals())#expected 1.0
    print(total)#expected 0