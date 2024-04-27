class A:
    def __init__(self):
        print("init A")
       # super(). __init__()
class B:
    def __init__(self):
        print("init B")
        super(). __init__()
class C(B,A):
    def __init__(self):pass
        #super(). __init__()
        #super(). __init__()
obj=C()