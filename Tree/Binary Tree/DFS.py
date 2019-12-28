from tree import root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key)

if __name__ == "__main__":
    print("inorder traversal")
    inorder(root)
    print("preorder traversal")
    preorder(root)
    print("postorder traversal")
    postorder(root)