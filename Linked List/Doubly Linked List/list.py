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
        if temp.next is not None:
            temp.next.prev = newNode
        newNode.prev = temp
        temp.next = newNode

    def insertAfterValue(self, data, value):
        newNode = Node(data)
        temp = self.head
        
        while(temp):
            if temp.data == value:
                newNode.next = temp.next
                if temp.next is not None:
                    temp.next.prev = newNode
                newNode.prev = temp
                temp.next = newNode
                return
            temp = temp.next

    def pop(self):
        # to remove first element

        # if list is empty
        if self.head is None:
            return

        temp = self.head
        self.head = temp.next
        temp.next.prev = None
        temp = None

    def remove(self):
        # to remove last node
        temp = self.head
        # if list is empty
        if self.head is None:
            return
        
        # if list has one item
        if self.head.next is None:
            self.head = None
            return
        
        # else traverse till second last element
        while(temp.next.next):
            temp = temp.next
        temp.next = None
        
    def removeNodeByValue(self, value):
        temp = self.head
        # if list is empty
        if self.head is None:
            return
        
        # the first item only contains the value
        if self.head.data == value:
            self.pop()
            return
        
        while(temp):
            if temp.data == value:
                break
            pre = temp
            temp = temp.next
        pre.next = temp.next
        temp.next.prev = pre
        temp = None

    def removeNodeByIndex(self, index):
        temp = self.head

        # if the list is empty
        if self.head is None:
            return

        #  if index is one 
        if index == 1:
            self.pop()
            return

        for i in range(1, index-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return

        if temp.next is None:
            return
        if temp.next.next is not None:
            temp.next.next.prev = temp   
        temp.next = temp.next.next
        temp = None

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
    doubleLinkedList.insertAfterValue(11,10)
    doubleLinkedList.pop()
    doubleLinkedList.remove()
    doubleLinkedList.removeNodeByValue(2)
    doubleLinkedList.removeNodeByIndex(2)
    doubleLinkedList.printList()
    



