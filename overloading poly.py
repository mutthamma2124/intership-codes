

class a:
    def ab(self,python,java):
        if java==0:
            print("trainer",python)
        elif python and java:
            print("trainer",python,java)
    
    def ab(self,python,java=0) :
        if java==0:
           print("trainer",python)
        elif python and java:
            print("trainer",python,java)
obj=a().ab("python","java")




