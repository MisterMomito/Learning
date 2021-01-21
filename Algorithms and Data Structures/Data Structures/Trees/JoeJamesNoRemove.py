class Tree:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, data):
        if self.data == data:
            return False  # duplicate value
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                self.left.parent = self
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                self.right.parent = self
                return True

    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def get_size(self):
        if self is not None:
            if self.left is not None and self.right is not None:
                return 1 + self.left.get_size() + self.right.get_size()
            elif self.left:
                return 1 + self.left.get_size()
            elif self.right:
                return 1 + self.right.get_size()
            else:
                return 1
        else:
            return -1

    def get_height(self):  # would it raise none-type error? Also above^
        if self is not None:
            if self.left is not None and self.right is not None:
                return 1 + max(self.left.get_height, self.right.get_height)
            elif self.left:
                return 1 + self.left.get_height
            elif self.right:
                return 1 + self.right.get_height
            else:
                return 1
        else:
            return -1

    def pre_order(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.pre_order()
            if self.right:
                self.right.pre_order()

    def in_order(self):
        if self is not None:
            if self.left is not None:
                self.left.in_order()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.in_order()

    def post_order(self):  # added myself
        if self is not None:
            if self.left is not None:
                self.left.pre_order()
            if self.right:
                self.right.pre_order()
            print(self.data, end=' ')

    def remove(self, data):
        # data not found
        if self is None:
            return False

        # find node
        if data < self.data:
            self.left.remove(data)
        elif data > self.data:
            self.right.remove(data)

        # Case 1: remove-node is the root
        if self.parent is None:
            if self.left is None and self.right is None:
                self.data = None
            elif self.left and self.right is None:
                self = self.left
            elif self.root.left is None and self.right:

        # Case 2: remove-node has no children
        elif self.left is None and self.right is None:
            if data < self.parent.data:
                self.parent.left = None
            else:
                self.parent.right = None
            return True

        # Case 3: remove-node has left child only
        elif self.left and self.right is None:
            if data < self.parent.data:
                self.parent.left = self.left
            else:
                self.parent.right = self.left
            return True

        # Case 4: remove-node has right child only
        elif self.left is None and self.right:
            if data < self.parent.data:
                self.parent.left = self.right
            else:
                self.parent.right = self.right
            return True

        # Case 5: remove-node has both children
        else:
            del_node = self._help_remove(self.right)
            self.data = del_node.data
            if del_node.right:
                if del_node.parent.data > del_node.value:  # check if it's okay to not compare directly to right node
                    del_node.parent.left = del_node.right
                elif del_node.parent.data < del_node.value:
                    del_node.parent.right = del_node.right
            else:
                if del_node.data < del_node.parent.value:
                    del_node.parent.left = None
                else:
                    del_node.parent.right = None
# return true here?
    def _help_remove(self, node):  # check if this recursion still works even with the first recursion of find
        if node.left:
            return self._help_remove(node.left)
        else:
            return node


t = Tree(0)
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.in_order()
t.remove(4)
t.in_order()















