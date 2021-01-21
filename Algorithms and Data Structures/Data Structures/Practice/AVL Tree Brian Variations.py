class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:  # changed from if self.root is None so if issue this possible
            return self._insert(data, self.root)
        else:
            self.root = Node(data)

    def _insert(self, data, cur_node):
        if data < cur_node.value:  # maybe add true/false success statements
            if cur_node.left is None:
                cur_node.left = Node(data)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right)
            else:
                self._insert(data, cur_node.right)
        else:
            print('Value already in tree.')

    # specified traversal types

    def pre_order(self):
        if self.root is not None:
            self._pre_order(self.root)

    def _pre_order(self, cur_node):
        if self.root:
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))
            self._pre_order(cur_node.left)
            self._pre_order(cur_node.right)

    def in_order(self):
        if self.root is not None:
            self._in_order(self.root)

    def _in_order(self, cur_node):
        if cur_node is not None:
            self._in_order(cur_node.left)
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))
            self._in_order(cur_node.right)

    def post_order(self):
        if self.root is not None:
            self._post_order(self.root)

    def _post_order(self, cur_node):
        if cur_node is not None:
            self._post_order(cur_node.left)
            self._post_order(cur_node.right)
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))

    def height(self):
        if self.root is None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def find(self, data):
        if self.root:  # again changed to if var instead of if is not
            return self._find(data, self.root)
        else:
            return False

# my find
    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left:  # took out is not none
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if node is None or self.find(node.value) is None:
            print('Node to be deleted not found in the tree!')
            return None

        # deleted the min value equation
        # returns the number of children for the specified node
        def num_children(n):
            children = 0  # changed to children to avoid scope conflicts
            if n.left:
                children += 1
            if n.right:
                children += 1
            return children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into three different cases based on the
        # the structure of the tree & node to be deleted

        # Case 1: Node has no children
        if node_children == 0:
            if node_parent:  # changed to if var rather than is not None
                # remove reference to the node from the parent
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # Case 2: Node has single child
        if node_children == 1:

            # get the single child node
            if node.left:
                child = node.left
            else:
                child = node.right

            if node_parent is not None:
                # replace the node to be deleted with its child
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

            # Case 3: Node has two children
            if node_children == 2:
                # get the in-order successor of the deleted node
                successor = node.right
                while successor.left:
                    successor = successor.left

                # copy the inorder successor's value to the node formerly
                # holding the value we wished to delete

                node.value = successor.value

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, cur_node):
        if cur_node.value == data:
            return True
        elif cur_node.value > data and cur_node.left:
            return self._search(data, cur_node.left)
        elif cur_node.value < data and cur_node.right:
            return self._search(data, cur_node.right)
        return False

    def _inspect_insertion(self, cur_node, path=[]):

    def _inspect_deletion(self, cur_node):

    def _rebalance_node(self, z, y, x):

    def _right_rotate(self, z):

    def _left_rotate(self, z):

    def get_height(self, cur_node):

    def taller_child(self, cur_node):
