
# there is mostly not var and var rather than is not none or is none
# min node is integrated into the 3rd deletion case

from Projects.KnightsTravails.Queue1 import Queue


class Node:
    def __init__(self, value):
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

                if n.left is not None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right is not None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def insert(self, value):
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = Node(value)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left:
                self._insert(value, cur_node.left)
            else:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left)
        elif value > cur_node.value:
            if cur_node.right:
                self._insert(value, cur_node.right)
            else:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right)
        else:
            print('Value already in tree')

    def find(self, value):
        if self.root:
            return self._insert(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._insert(value, cur_node.right)

    def search(self, value):
        if self.root:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._search(value, cur_node.right)
        return False

    def height(self):
        if self.root:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if not cur_node:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def in_order(self):
        if self.root:
            self._in_order(self.root)

    def _in_order(self, cur_node):
        if cur_node:
            self._in_order(cur_node.left)
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))  # WHY %S
            self._in_order(cur_node.right)

    def breadth_first_search(self, start):
        if not start:
            return

        q = Queue()
        q.enqueue(start)

        while not q.is_empty():
            print(q.peek().value)
            node = q.dequeue()

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    def delete_value(self, value):
        self.delete_node(self.find(value))

    def delete_node(self, node):
        if node is None or self.find(node.value) is None:
            print('Node to be deleted not found in the tree!')
            return None

        def find_num_children(n):
            num_children = 0
            if n.left:
                num_children += 1
            if n.right:
                num_children += 1
            return num_children

        node_parent = node.parent
        node_children = find_num_children(node)

        # Case 1: No children
        if node_children == 0:
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # Case 2: One child
        if node_children == 1:  # why no elif or return?
            if node.left:
                child = node.left
            else:
                child = node.right

            if node_parent:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            child.parent = node_parent
        # Case 3: Two Children
        if node_children == 2:
            successor = node.right
            while successor.left:
                successor = successor.left

            node.value = successor.value
            self.delete_node(successor)

            return  # you good after node has two children ( i think)

        if node_parent:
            node_parent.height = 1 + max(self.get_height(node_parent.left),
                                         self.get_height(node_parent.right))
            self._inspect_deletion(node_parent)

# new functions for avl tree
    def _inspect_insertion(self, cur_node, path=[]):
        if not cur_node.parent:
            return
        path = [cur_node] + path

        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        if abs(left_height-right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _inspect_deletion(self, cur_node):
        if not cur_node:
            return

        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        if abs(left_height-right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)  # find out why you rotate on the parent node (pay attention to rotate funcs)
        else:
            raise Exception('_rebalance_node: z, y, x node configuration not recognized!')

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
        if not y.parent:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2

        if t2:
            t2.parent = z

        y.parent = sub_root
        if y.parent:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        else:
            self.root = y

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def get_height(self, cur_node):
        if not cur_node:
            return 0
        return cur_node.height

    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left)
        right = self.get_height(cur_node.right)
        return cur_node.left if left >= right else cur_node.right


# test delete with 3 children

tree = AVLTree()
tree.insert(21)
tree.insert(24)
tree.insert(26)
tree.insert(25)
tree.insert(28)
tree.insert(29)
tree.insert(37634)
tree.in_order()

print(tree)


tree.breadth_first_search(tree.root)
