class a():
    def __init__(self):
        print("a")

class b(a):
    def __init__(self):
        super().__init__() # for call parent value 
        print("B")


class c (b,a):
    def __init__(self):
        super().__init__() # for call parent value 
        print("C")

obj=a()
