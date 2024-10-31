class Calculator:

    def __init__(self):
        self.total = 0
        # for an object to have fields
        # they MUST be declared inside the constructor
    def add(self, num):
        self.total += num

    def sub(self, num):
        self.total -= num

    def mul(self, num):
        self.total *= num

    def div(self, num):
        self.total /= num

    def equals(self):
        return_value = self.total
        self.total = 0
        return return_value



    