class ECE:
    def __init__(self,amount):
        self.amount=amount
    def total(self,other):
        print(self.amount,other.amount,self.amount+other.amount)
    def getback(self):
        print(self.amount)
shravanthi=ECE(100)
rohini=ECE(1000)
ECE.total(shravanthi,rohini)