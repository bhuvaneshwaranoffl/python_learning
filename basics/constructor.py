class laptop:
    def __init__(self): #construtor ,allocates memory,called by objject
        self.ram=""
    def display(self): #use self keyword 
      print("ram:",self.ram)


hp=laptop()#initialize object
dell = laptop ()
hp.ram = "8GB"
dell.ram="23GB"


hp.display()
dell.display()

# self  is a kkeywprd for calling current object 
