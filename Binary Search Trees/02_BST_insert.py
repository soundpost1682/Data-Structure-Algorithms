class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        tmp = self.root
        while True:
            if new_node.value == tmp.value:
                return False
            if new_node.value < tmp.value:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                tmp = tmp.rught

my_tree = BinarySearchTree()
my_tree.insert(21)
my_tree.insert(14)
my_tree.insert(35)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

