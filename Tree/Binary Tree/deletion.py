# Delete a node in binary tree 
# The deleted node is replaces by bottom most and right most node

# Algorithem
# 1)  find the deepest and rightmost node in binary tree and node which we want to delete.
# 2)  Replace the deepest rightmost node’s data with node to be deleted.
# 3)  Then delete the deepest rightmost node.

from tree import root
from BFS import bfs

def deleteLastNode(root, node):
    # node is a node to be delated
    queue = []
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)

        if temp is node:
            temp = None
            return

        if temp.right:
            if temp.right is node:
                temp.right = None
                return
            else:
                queue.append(temp.right)

        if temp.left:
            if temp.left is node:
                temp.left = None
                return
            else:
                queue.append(temp.left)


def deletion(root, key):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root

    keyNode = None
    queue = []
    queue.append(root)

    while len(queue) > 0 : 
        temp = queue.pop(0)

        if temp.data == key:
            keyNode = temp

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)
        
    # end of the while loop we'll get the last node of tree as temp
    if keyNode:

        x = temp.data
        deleteLastNode(root, temp)
        keyNode.data = x