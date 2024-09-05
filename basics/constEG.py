#call student and display  reg no
'''
class student:
    def __init__(self):
        self.name="bbb"
        self.reg="ii"
    def display(self):
        print("name",self.name)
        print("regno:",self.reg)

"""s1=student()
sl.name= "bhuvanesh"
print(s1.name)
s1.display()"""

s1=student()
s1.name="bhuvanesh"
s1.reg="1"

s2=student()
s2.name="bhuvi"
s2.reg="2"
s1.display()
s2.display()'''

# pass color  as a parameter  like fruit(red)

'''class fruit:

    def __init__(self,col): #we used another variable col and call the variable for color
        self.color=col
apple=fruit("red")

print(apple.color)'''

'''class teacher:
    def __init__(self,name,reg):
        self.name=reg
        self.reg=name
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.reg)

t1=teacher("thomas","12")
t1.name="bhuva"
t1.reg="12"'''
#t2 = teacher("seld","23")
'''t2.name="njib"
t2.reg="23"'''

'''t1.display()
t2.display()'''


class calculator:
    def __init__ (self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)

hello=calculator(10,2)
hello.add()

#we can directlt pass the  value  without using  constructor  like
'''

class calculator:

def add(self,a,b):
        print("add",a+b)

hello=calculator()
hello.add(10,2)






















