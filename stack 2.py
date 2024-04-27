class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.size=3
        self.top=-1
    def push(self,data):
        newNode=node(data)
        if self.top<self.size-1:
            self.top+=1
            if self.head==None:
                self.head=newNode
            else:
                newNode.next=self.head
                self.head=newNode
        else:
            print("stack  overflow")
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        else:
            self.head=self.head.next
            self.top-=1
        
obj=stack()
obj.push(5)
obj.push(6)
obj.push(7)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.display()

