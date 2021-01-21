class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def get_height(self):
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 1

    def pre_order(self):
        if self:
            print(self.value)
            if self.left:
                self.left.pre_order()
            if self.right:
                self.right.pre_order()

    def in_order(self):
        if self:
            if self.left:
                self.left.in_order()
            print(self.value)
            if self.right:
                self.right.in_order()

    def post_order(self):
        if self:
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
            print(self.value)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def get_height(self):
        if self.root:
            return self.root.get_height()
        else:
            return -1

    def pre_order(self):
        if self.root is not None:
            print('Pre-order')
            self.root.pre_order()

    def post_order(self):
        if self.root is not None:
            print('Post-order')
            self.root.post_order()

    def in_order(self):
        if self.root is not None:
            print('In-order')
            self.root.in_order()

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # delete node is in the root
        elif self.root.value == data:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                del_parent = self.root
                del_node = self.root.right
                while del_node.left:
                    del_parent = del_node
                    del_node = del_node.left

                self.root.value = del_node.value
                if del_node.right:
                    if del_parent.value > del_node.right.value:
                        del_parent.left = del_node.right
                    elif del_parent < del_node.right.value:  # could use else here cuz never equal right?
                        del_parent.right = del_node.right
                else:
                    if del_node.value < del_parent.value:
                        del_parent.left = None
                    else:
                        del_parent.right = None

            return True

        # find node to remove
        parent = None
        node = self.root
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.left
            elif data > node.value:
                node = node.right

        # Case 1: data is not found
        if node is None or node.value != data:
            return False

        # Case 2: remove-node has no children
        elif node.left is None and node.right is None:
            if parent.value > data:
                parent.left = None
            else:
                parent.right = None
            return True

        # Case 3 delete node has only left child
        elif node.left and node.right is None:
            if parent.value > data:  # why does it say node.left is None???
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        # Case 4 delete node has only right child
        elif node.left is None and node.right:
            if parent.value > data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        # Case 5 delete node has two children
        else:
            del_parent = node
            del_node = node.right
            while del_node.left:
                del_parent = del_node
                del_node = del_node.left

            node.value = del_node.value
            if del_node.right:
                if del_parent.value > del_node.right.value:
                    del_parent.left = del_node.right
                elif del_parent < del_node.value:
                    del_parent.right = node.right
            else:
                if del_parent.value > del_node.value:
                    del_parent.left = None
                else:
                    del_parent.right = None


bst = Tree()
print(bst.insert(10))
# print(bst.insert(5))
bst.pre_order()
print(bst.get_height())
# bst.postorder()
# bst.inorder()
print(bst.remove(10))
bst.pre_order()
