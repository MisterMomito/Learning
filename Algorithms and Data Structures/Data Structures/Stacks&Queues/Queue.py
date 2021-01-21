
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)
        return self.items

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def print_queue(self):
        print(self.items)
        return


a = Queue()

for item in [0, 14, 52, 6, 73, 835, 3]:
    a.enqueue(item)

a.dequeue()
a.dequeue()

a.print_queue()
