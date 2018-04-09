from linkedList import *


class DeQueue(object):
    def __init__(self):
        self.items = LinkedList()
        
    def isEmpty(self):
        if self.items.isEmpty():
            return True
        else:
            return False
    
    def addFront(self,item):
        self.items.add(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop(0)
    

    
    
    
def main():    
    d = DeQueue()
    print (d.isEmpty())
    d.addFront(3)
    d.addFront(5)
    d.removeFront()
    print (d.isEmpty())

main()


    

