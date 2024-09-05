
''''
#having all created , instance variable

class phone ():
    def  __init__(self,brand,charger):
       self.brand=brand
       self.charger=charger
    def display(self):
       print ("brand:",self.brand)
       print ("Charger-Type:",self.charger)
samsung=phone("sammsung","b-type")
samsung.display()
redmi=phone("redmi","b-type")
redmi.display()
'''

#now  c  type is common using class varible

class phone ():
    charger="C-Type" # we declare as an constant varible

    def  __init__(self,brand):
       self.brand=brand
       
    def display(self):
       print ("brand:",self.brand)
       print ("Charger-Type:",self.charger)

phone.charger="B-Type"  # if want to override 
samsung=phone("sammsung")
samsung.display()
redmi=phone("redmi")
