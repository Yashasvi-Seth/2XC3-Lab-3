#Author: Sreyo Biswas

#class for a node in the binary search tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #function to check if node is a leaf node
    def is_leaf(self):
        return self.left is None and self.right is None

#class for the actual BST
class BST:
    def __init__(self):
        self.root = None

    #function that checks if the BST is empty
    def is_empty(self):
        return self.root is None

    #function that inserts a value into the BST
    def insert(self, value):
        if self.is_empty():
            self.root = BSTNode(value)
        else:
            #go through the tree and find the accurate position to insert the new value
            current = self.root
            while True:
                #if the value to be inserted is less than the current node's value, go left, otherwise go right
                if value<current.value:
                    if current.left is None:
                        current.left = BSTNode(value)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = BSTNode(value)
                        break
                    current = current.right

    #function that calculates the height of the BST
    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    #calculates height of the BST in a recursive manner
    def __get_height(self, node):
        if node is None:
            return 0
        left_height = self.__get_height(node.left)
        right_height = self.__get_height(node.right)
        return 1 + max(left_height, right_height)