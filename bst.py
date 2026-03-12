#Author: Sreyo Biswas

#class for a node in the binary search tree
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #function to check if node is a leaf node
    def is_leaf(self):
        return self.left == None and self.right == None

#class for the actual BST
class BST:
    def __init__(self):
        self.root = None

    #function that checks if the BST is empty
    def is_empty(self):
        return self.root == None

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
                    if current.left == None:
                        current.left = BSTNode(value)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = BSTNode(value)
                        break
                    current = current.right

    #function that calculates the height of the BST
    def get_height(self):
        #if the tree is empty return 0
        if self.is_empty():
            return 0
        #use a stack to do a depth first traversal of the tree and keep track of the maximum depth reached
        stack = [(self.root, 1)]
        maxHeight = 0
        #if there is a node on the stack, pop it and add its children to the stack with their corresponding depth (current depth + 1)
        while stack:
            node, depth = stack.pop()
            if node != None:
                maxHeight = max(maxHeight, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return maxHeight