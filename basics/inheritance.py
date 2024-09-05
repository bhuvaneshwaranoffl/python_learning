#single inheritance

class dad():
    def phone(self):
        print("dad's phone")

class son(dad): # for inheritance add the cparent class inside child class
    def laptop(self):
        print("son's laptop")

ram =son()
ram.phone()


#multiple inheritance

class dad():
    def phone(self):
        print("dad's phone")

class mom():
    def sweet (self):
        print("mom's Sweet")

class son(dad,mom): # for inheritance add the cparent class inside child class
    def laptop(self):
        print("son's laptop")

ram =son()
ram.phone()
ram.sweet()

#multilevel

class grandpa():
    def phone(self):
        print("granpa's phone")

class dad(grandpa):
    def money (self):
        print("money")

class son(dad):
    def laptop(self):
        print("my laptop")

ram = son()
ram.laptop()

d1=dad()
d1.phone()

#hierarchy

class dad():
    def money(self):
        print("dad's money ")

class son1(dad):
    pass

class son2(dad):
    pass
class son3(dad):

    pass # empty class

s=son2()
s.money()

#hybrid 




class dad():
    def money(self):
        print("dad's money ")

class land():
    def important(self):
        print("imp land")

class son1(dad,land):
    pass

class son2(dad):
    pass
class son3(dad):
    pass


s=son2()
s.money()






