class maxHeap:
    def __init__(self) :
        self.heap = []
    
    def leftChild(self, idx):
        return 2* idx + 1
    def rightChild(self, idx):
        return 2* idx + 2
    def parent(self, idx):
        return (idx-1) // 2
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        
    
    def insert(self, value):
        self.heap.append(value)
        tmp = len(self.heap) -1
        while tmp > 0 and self.heap[tmp] > self.heap[self.parent(tmp)]:
            self.swap(tmp, self.parent(tmp))
            tmp = self.parent(tmp)


myHeap = maxHeap()
myHeap.insert(99)
myHeap.insert(72)
myHeap.insert(61)
myHeap.insert(58)

print(myHeap.heap)

myHeap.insert(100)
print(myHeap.heap)

myHeap.insert(75)
print(myHeap.heap)
