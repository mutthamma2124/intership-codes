class node:
    def __init__(self,data): 
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
    def delete_at_beginning(self):
        if self.head is None:
            print("no data found")
        else:
            current=self.head
            self.head=self.head.next
            current.next=None
    def delete_at_end(self):
        if self.head is None:
            print("no data found")
        elif self.head.next is None:
            self.head=None
        else:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=None
    def delete_by_value(self,data):
        if self.head is None:
            print("no data found")
        elif self.head.data==data:
            self.delete_at_beginning()
        else:
            current=self.head
            count=0
            while current.next:
                if current.next.data==data:
                    count=count+1
                    current.next=current.next.next
                    break
                current=current.next
                if count==0:
                    print("no data found")
    def search(self,key):
         current=self.head
         count=0
         while current :
             count=count+1
             if current.data==key:  
                print("data found at position",count)
                count=-1
                break
             current=current.next
         if count!=-1:
                print("data not found")
            
            
        
obj=linkedlist()
obj.insert_at_beginning(5)
obj.insert_at_beginning(8)
obj.insert_at_beginning(7)
obj.insert_at_beginning(6)
obj.search(5)
#obj.delete_by_value(6)
 #obj.insert_at_position(3,9)
#obj.delete_at_beginning()
#obj.delete_at_end()
#obj.display()



