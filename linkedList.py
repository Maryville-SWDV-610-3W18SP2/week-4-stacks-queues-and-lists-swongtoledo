class Node(object):
    def __init__(self, data, Next = None):
        self.data = data
        self.next = Next

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext

class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, element):
        temp = Node(element)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def getAllData(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.getData())
            current = current.getNext()

        return elements

    def insert(self,index,data):
        if index>=self.length() or index<0:
            return self.append(data)
        cur_node=self.head
        prior_node=self.head
        cur_idx=0
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
                new_node=node(data)
                prior_node.next=new_node
                new_node.next=cur_node
                return
            prior_node=cur_node
            cur_idx+=1

    def getItem(self, index):
        ##return an item given an index
        current = self.head
        for i in range(index):
            current = current.getNext()
        if current != None:
            return current.getData()
        else:
            raise("index out of range")


    def pop(self, index):
        self.remove(self.getItem(index))
