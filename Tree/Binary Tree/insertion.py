# Given a binary tree and key, 
# insert the key into tree at the first possible position in level order  

# Iterate through level order traversal
# find a node whose left chiild is empty or a right child empty and make it a tree node

from tree import root, Node
from BFS import bfs

def insert(root, key):
    queue = []
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)

        if temp.left is None:
            temp.left = Node(key)
            return

        else:
            queue.append(temp.left)

        if temp.right is None:
            temp.right = Node(key)
            return
        else:
            queue.append(temp.right)

if __name__ == "__main__":
    insert(root, 10)
    insert(root, 11)
    bfs(root)