class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.value:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

        else:
            if self.value:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return self  # made return self rather than True

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
            return 1 + max(self.left.get_height() + self.right.get_height())
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


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)

