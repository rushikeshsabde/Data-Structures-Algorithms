# class for creating 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    # for adding the node at start of list
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    
    def append(self, data):
        newNode = Node(data)
        temp = self.head

        # if the linked list is empty
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        # traverse till end node 
        while(temp.next):
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def insertAfterIndex(self, data, index):
        newNode = Node(data)
        temp = self.head
        # if the linked is empty 
        if self.head is None:
            newNode.prev = None
            self.head = newNode
        
        for i in range(1, index):
            temp = temp.next
            if temp is None:
                break
        newNode.next = temp.next
        if temp.next.prev is not None:
            temp.next.prev = newNode
        newNode.prev = temp
        temp.next = newNode
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    doubleLinkedList = LinkedList()
    doubleLinkedList.append(2)
    doubleLinkedList.append(3)
    doubleLinkedList.push(1)
    doubleLinkedList.insertAfterIndex(10,2)
    doubleLinkedList.printList()



