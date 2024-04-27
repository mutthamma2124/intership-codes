class A:
    def __init__(self,a):
        self.a=a
    def __mul__(muttu,chandu):
        return muttu.a*chandu.a
muttu=A(10)
chandu=A(20)
print(muttu*chandu)

