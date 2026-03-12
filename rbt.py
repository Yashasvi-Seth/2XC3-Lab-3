class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

#--------------------------------------------------------------------------------------------------
# Implemented by : Yashasvi Seth

    def rotate_right(self):
        new_root = self.left
        if new_root == None:
            return self
        
        # connecting self's left child to new_root's right child
        self.left = new_root.right

        # assigning parent of new_root's right child as self
        if new_root.right != None:
            new_root.right.parent = self  

        # connecting the new root to the parent of self after rotation
        new_root.parent = self.parent
        # check if left or right child 
        if self.parent != None:
            if self.is_left_child():
                self.parent.left = new_root
            else:
                self.parent.right = new_root
        
        # connecting self as the right child of new_root
        new_root.right = self
        self.parent = new_root
        return new_root
        

    def rotate_left(self):
        new_root = self.right
        if new_root == None:
            return self
        
        # connecting self's right child to new_root's left child
        self.right = new_root.left

        # assigning parent of new_root's left child as self
        if new_root.left != None:
            new_root.left.parent = self  

        # connecting the new root to the parent of self after rotation
        new_root.parent = self.parent
        # check if left or right child 
        if self.parent != None:
            if self.is_left_child():
                self.parent.left = new_root
            else:
                self.parent.right = new_root
        
        # connecting self as the left child of new_root
        new_root.left = self
        self.parent = new_root
        return new_root


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

#--------------------------------------------------------------------------------------------------
# Implemented by : Emre Bozkurt
    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            if node.parent.is_left_child():
                uncle = node.parent.get_uncle()
                if uncle != None and uncle.is_red():
                    node.parent.make_black()
                    uncle.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node.is_right_child():
                        node = node.parent
                        node.rotate_left()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_right()
            else:
                uncle = node.parent.get_uncle()
                if uncle != None and uncle.is_red():
                    node.parent.make_black()
                    uncle.make_black()
                    node.parent.parent.make_red()
                    node = node.parent.parent
                else:
                    if node.is_left_child():
                        node = node.parent
                        node.rotate_right()
                    node.parent.make_black()
                    node.parent.parent.make_red()
                    node.parent.parent.rotate_left()
        while self.root.parent != None:
            self.root = self.root.parent
        self.root.make_black()
#--------------------------------------------------------------------------------------------------          

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
