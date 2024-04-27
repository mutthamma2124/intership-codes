class A:
    def __init__(self):
        print("init A")
class B(A):
    def __init__(self):
        A(). __init__()
        print("init B")
class C(B):
    pass
obj=C()