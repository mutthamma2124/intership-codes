class node:
    def __init(self,data): 
        self.data=data
        self.next=None
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode
    def insert_at_beginning(self,data):
        NewNode=node(data)
        if self.head is None:
            self.head=NewNode
        else:
            NewNode.next=self.head
            self.head=NewNode
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
    def insert_at_position(self,data,position):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        elif position==1:
            newNode.next=self.head
            self.head=newNode
        else:
            current=self.head
            count=0
            while current:
                count+=1
                if count==position-1:
                    newNode.next=current.next
                    current.next=newNode
                    break
                current =current.next
            if count<position-1:
                self.insert_at_end(data)
            
        
obj=linkedlist()
obj.insert_at_beginning(5)
obj.insert_at_end(8)
obj.insert_at_beginning(2)
obj.insert_at_position(3,9)
obj.display()

