class A:
    def __init__(self):
        print("init a")
        super().__init__()
class B:
    def __init__(self):
        print("init b")
        #super().__init__()
class C(A,B):
    def __init__(self):
        print("init c")
        super().__init__()
C()

