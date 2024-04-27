class A:
    def __init__(self,a):
        self ._a=a
print(A(10)._a)




class A:
    def __init__(self,a):
        self.__a=a
        print(self.__a)
A(10)



    