class Queue:
    def __init__(self):
        self.queue=[]
        self.size=5
        self.front=self.rear=-1
    def enqueue(self,data):
        if self.front==-1 and self.rear==-1:
            self.front=self.rear=0
            self.queue.append(data)
        elif self.rear<self.size-1:
            self.rear+=1
            self.queue.append(data)
        else:
            print("queue is full")
    def dequeue(self):
        if self.front>self.rear:
            print("queue is empty")
        self.front+=1
       # self.queue.pop(self.queue[self.front])
        #self.front=self.front+1
        
            
    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=" ")
        #for i in self.queue:
           # print(i,end=" ")
        
        
        
        
obj=Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(6)
obj.dequeue()
obj.dequeue()

obj.display()

