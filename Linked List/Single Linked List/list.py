class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList: 

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def append(self, data):
        newNode = Node(data)
        
        # if list is empty
        if self.head is None:
            self.head = newNode
            return
        
        # add in the end
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newNode
    
    def pop(self):
        # remove the first node
        
        # if list is empty
        if self.head is None:
            return
        temp = self.head
        self.head = temp.next
        temp= None

    def remove(self):
        # remove the last node

        # if the list is empty
        if self.head is None:
            return
        
        # if list has only one node
        if self.head.next is None:
            self.head = None
            return

        # List has more than one item
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None
    
    def removeNode(self,key):
        temp = self.head

        # check if the head contains the 
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
    
        while(temp):
            if temp.data == key:
                break # exit out of while loop 
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None
    
    def removeNodeByIndex(self, index):
        temp = self.head

        # delete the first node
        if index is 1:
            self.head = temp.next
            temp = None
            return
        
        for i in range(1, index-1):
            temp = temp.next
            if temp is None:
                break

        #  if the given position does not exist 
        if temp is None:
            return
        # we have to delete the temp.next Node 
        if temp.next is None:
            return
        
        temp.next = temp.next.next
        temp = None

    def insertAfterIndex(self, index, data):
        newNode = Node(data)
        temp = self.head
        for i in range(1,index):
            temp = temp.next
            if temp is None:
                break
        newNode.next = temp.next
        temp.next = newNode

    def insertAfterValue(self,value, data):
        temp = self.head
        newNode = Node(data)
        while(temp):
            if temp.data == value:
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next

    def insertAfterNode(self, node, data):
        newNode = Node(data)
        newNode.next = node.next
        node.next = newNode
        

if __name__ == "__main__":
    singleList = LinkedList()
    singleList.push(3)
    singleList.push(2)
    singleList.push(1)
    singleList.append(4)
    singleList.append(5)
    singleList.append(6)
    singleList.pop()
    singleList.remove()
    singleList.removeNode(3)
    singleList.removeNodeByIndex(2)
    singleList.insertAfterValue(2,10)
    singleList.insertAfterIndex(2,11)
    singleList.printList()