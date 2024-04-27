class ECE:
    def __init__(self,*marks):
        self.m1=marks[0]
        self.m2=marks[1]
        self.m3=marks[2]
        self.m4=marks[3]
        self.m5=marks[4]
        self.total()
    def total(self):
        self.total=self.m1+self.m2+self.m3+self.m4+self.m5
    def rank(*self):
        l=[]
        for i in self:
            l.append(i.total)
        print(l)
        sort=sorted(l)
        print(sort)
shobha=ECE(100,100,100,100,100)
shabbu=ECE(90,90,90,90,90)
rohini=ECE(80,80,80,80,80)
ECE.rank(shobha,shabbu,rohini)