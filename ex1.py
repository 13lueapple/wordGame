class A:
    def __init__(cls):
        cls.var1 = 1
    
    def run():
        print(A.var1)
    
    @classmethod
    def runclsm(cls):
        print(cls.var1)
    
    def runself(self):
        print(self.var1)
        
a = A()
a.runself()