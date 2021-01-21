class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0] # this is heapify
        for item in items:
            self.heap.append(item)
            self._float_up(len(self.heap)-1)

    def push(self, datum):
        self.heap.append(datum)
        self._float_up(len(self.heap)-1)

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return None

    def pop(self):
        if len(self.heap) > 1:
            self._swap(1, len(self.heap)-1)
            maximum = self.heap.pop()
            self._bubble_down(1)
        else:
            maximum = None
        return maximum

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _float_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._float_up(parent)

    def _bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._bubble_down(largest)

    def heap_sort(self):
        sorted_heap = []
        while self.peek():
            sorted_heap.insert(0, self.pop())
        return sorted_heap

    def __str__(self):
        return str(self.heap)

'''
m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
print(m)

print()
a = MaxHeap([1])
print(a)
print(a.pop())
print(a)

print()
c = MaxHeap()
print(c)
print(c.pop())
'''

m = MaxHeap([1, 4, 2342, 45456, 1351, 15321, 451658, 3, 143, 15541])

print(m.heap_sort())
