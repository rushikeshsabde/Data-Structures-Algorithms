# sum of nodes value based on certain condations
from tree import root

# sum of all nodes in the binary tree
def sum(root):
    if root is None:
        return 0
    
    summation = root.key + sum(root.left) + sum(root.right)
    return summation

# Sum of all the parent nodes having child node x
# def sum2(root):


if __name__ == "__main__":
    print(sum(root))