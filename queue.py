class Node:
 
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data 
        self.next = None

        
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext
        
        
class Queue:
     
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0 
         
 
    def isEmpty(self):
        return self.front == None
     
    # add an item to the queue
    def enqueue(self, item):
        item = Node(item)
         
        if self.rear == None:
            self.front = item
            self.rear = item
            return
        self.rear.next = item
        self.rear = item
 
    # remove an item from queue
    def dequeue(self):
         
        if self.isEmpty():
            return
        item = self.front
        self.front = item.next
 
        if(self.front == None):
            self.rear = None
        return str(item.data)




## testing the function out
            
def main():           
    q = Queue()
    q.enqueue(10)
    q.enqueue(40)
    q.enqueue(50)
    print (q.isEmpty())
    print("Dequeued item is ", q.dequeue())

main()

 