 
# Class to represent a node
class Node:
 
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data 
        self.next = None
 
class Stack:
     
    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None
 
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
 
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.root 
        self.root = newNode
        print ("pushed to stack",data)
     
    def pop(self):
        if (self.isEmpty()):
            return len(self) == 0 
        temp = self.root 
        self.root = self.root.next
        popped = temp.data
        return popped
     
    def peek(self):
        if self.isEmpty():
            return len(self)== 0
        return self.root.data




## testing the stack
def main():
    stack = Stack()
    stack.push(30)        
    stack.push(40)
    stack.push(50)
 
    print ("Popped from stack {0}".format(stack.pop()))
    print ("Top element is {0}".format(stack.peek()))
    
main()
    