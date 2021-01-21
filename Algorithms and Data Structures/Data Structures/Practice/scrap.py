'''
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

    def __repr__(self):
        if self.root is None:
            return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0:
                break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n is None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.value is not None:
                    buf = ' ' * int((5 - len(str(n.value))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.value), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left_child is not None:
                    next_nodes.append(n.left_child)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right_child is not None:
                    next_nodes.append(n.right_child)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right)
            else:
                self._insert(value, cur_node.right)
        else:
            print('Value already in tree')

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left is not None:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._find(value, cur_node.left)

    def get_height(self, cur_node):
        if cur_node is None:
            return 0
        return cur_node.height

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if node is None or self.find(node.value) is None:  # see if you can improve on this. Inefficient to call find 2x
            print("Node to be deleted not found in the tree!")
            return None

        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        # Case 1
        if node_children == 0:
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # Case 2 (node has a single child)
        if node_children == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # Case 3: node has two children:
            if node_children == 2:
                successor = min_value_node(node.right)
                node.value = successor.value
                self.delete_node(successor)
                return

            if node_parent is not None:
                node_parent.height = 1 + max(self.get_height(node_parent.left), self.get_height(node_parent.right))
                self._inspect_deletion(node_parent)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        if value < cur_node.value and cur_node.left is not None:  # could work with if var right?
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        else:
            return False

    # functions added for AVL...

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent is None:
            return
        path = [cur_node] + path

        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _inspect_deletion(self, cur_node):  # check over
        if cur_node is None:
            return

        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, x, y, z):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z, y, x node configuration not recognized')

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 is not None:
            t3.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.left = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
            z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
            y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left)
        right = self.get_height(cur_node.right)
        return cur_node.left if left >= right else cur_node.right


tree = AVLTree()
tree.insert(21)
tree.insert(24)
tree.insert(26)
tree.insert(25)
tree.insert(28)
tree.insert(29)
tree.insert(37634)
tree.print_tree()

print(tree)
'''





















