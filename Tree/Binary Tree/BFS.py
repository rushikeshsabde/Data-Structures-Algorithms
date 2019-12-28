from tree import root

def bfs(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)

    while(len(queue)>0):
        print(queue[0].key)

        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

if __name__ == "__main__":
    bfs(root) 

