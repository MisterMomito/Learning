class Node:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n

    def __str__(self):
        return '(' + str(self.value) + ')'


class CircularLinkedList:
    def __init__(self, h=None):
        self.head = h
        self.size = 0

    def add(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.head.next = self.head
        else:
            new_node = Node(value, self.head.next)
            self.head.next = new_node
        self.size += 1

    def find(self, value):
        current_node = self.head
        while True:
            if current_node.value == value:
                return value
            elif current_node.next == self.head:
                return False
            current_node = current_node.next

    def remove(self, value):
        if self.size == 0:
            return False

        current_node = self.head
        while current_node.next != self.head:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next
        if current_node.next.value == value:
            current_node.next = current_node.next.next
            self.head = current_node.next.next
        else:
            return False

    def print_list(self):
        if self.head is None:
            return
        current_node = self.head
        print(current_node, end='->')
        while current_node.next != self.head:
            current_node = current_node.next
            print(current_node, end='->')
        print()


c = CircularLinkedList()
for value in [1, 2, 3, 4, 5, 6]:
    c.add(value)

c.print_list()


def is_circular(linked_list):
    try:
        point1 = linked_list.head.next
        point2 = linked_list.head.next.next

        while point1 != point2:
            if point1.next is None or point2.next is None:
                return False
            point1 = point1.next
            point2 = point2.next.next

        return True

    except AttributeError as e:
        return e


print(is_circular('21'))
