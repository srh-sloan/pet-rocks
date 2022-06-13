
class Rock:
    def __init__(self, name:str, shape:str):
        self.name = name
        self.shape = shape
    
    def printinfo(self):
        print('Hi my name is',self.name,'and I am',self.shape)