class laptop():
    charger = "C-Type"

    def  __init__(self):
        self.brand=""
        self.price=34
    def  setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)

      #if we use @classmethod (decorator) in this line laptop.setCharge(laptop) we can write as laptop.setCharge()
      #class method use cls instead of self
    def setCharge(cls):
        cls.charger="B-type"

      #static
    @staticmethod #decorator
    def info():
        print("hi")

hp=laptop()
hp.setPrice(45)

hp.getPrice()


#for print proce first do  set  and then get the value

laptop.setCharge(laptop)

hp.info()
