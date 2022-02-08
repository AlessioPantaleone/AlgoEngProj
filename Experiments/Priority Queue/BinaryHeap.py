from Imports.myimports import *


class BinaryHeap:
    def __init__(self, arr=None):
        if arr is None:
            arr = [20, 10, 15, 8, 7, 13, 14, 2, 5, 6]
        self.heap = arr
        self.heapify(0)

    def __str__(self):
        return str(self.heap)

    def fixHeap(self, node: int):
        if (2 * node) + 1 > len(self.heap) - 1 and (2 * node) + 2 > len(self.heap) - 1:
            return
        else:
            u = (2 * node) + 1
            if (2 * node) + 2 < len(self.heap):
                if self.heap[(2 * node) + 2] > self.heap[(2 * node) + 1]:
                    u = (2 * node) + 2
            if self.heap[node] < self.heap[u]:
                temp = self.heap[node]
                self.heap[node] = self.heap[u]
                self.heap[u] = temp
                self.fixHeap(u)

    def deleteMax(self):
        if len(self.heap) > 0:
            max = self.heap[0]
            lastleaf = self.heap.pop()
            if len(self.heap) != 0:
                self.heap[0] = lastleaf
                self.fixHeap(0)
            return max

    def getMax(self):
        return self.heap[0]

    def getLength(self):
        return len(self.heap)

    def heapify(self, node: int):
        if node > len(self.heap):
            return
        self.heapify((2 * node) + 1)
        self.heapify((2 * node) + 2)
        self.fixHeap(node)

    def insert(self, element: int):
        self.heap.append(element)
        self.heapify(0)


if __name__ == "__main__":
    for iterations in range(15):

        RandomArr = random.sample(range(100), 50)
        PythonSorted = RandomArr.copy().sort(reverse=True)

        Heap = BinaryHeap(RandomArr)

        Sorted = []
        while Heap.getLength() > 0:
            Sorted.append(Heap.deleteMax())

        print(Sorted)
        print(PythonSorted)
        assert Sorted == PythonSorted
        print("END ITERATION")
