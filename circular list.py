class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
    def __init__(self,data):
        self.data=data
        self.next=None
       # self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
        #self.tail=None
    def insert(self,data):
        newNode=node(data)
        #self.tail=newNode
        if self.head is None:  
            self.head=newNode
            newNode.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=newNode
            newNode.next=self.head
            #newNode.prev=current
            
    def display(self):
        print(self.head.data,end="->")
        current=self.head.next
        while current!=self.head:
            print(current.data,end="->")
            current=current.next
                
   
            
                
                
obj=linkedlist()
obj.insert(5)
obj.insert(6)
obj.insert(3)
obj.display()
#obj.display_f()
#obj.display_b()
        



