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
    
    def remove(self):
        if len(self.heap) ==0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return max_val
    
    def sink_down(self, idx):
        maxIDX = idx
        while 1:
            leftIDX = self.leftChild(idx)
            rightIDX = self.rightChild(idx)
            if len(self.heap) > leftIDX and self.heap[leftIDX] > self.heap[maxIDX]:
                maxIDX = leftIDX
            if len(self.heap) > rightIDX and self.heap[rightIDX] > self.heap[maxIDX]:
                maxIDX = rightIDX
            if maxIDX != idx:
                self.swap(idx, maxIDX)
                idx = maxIDX
            else: return 

    
        


myHeap = maxHeap()
myHeap.insert(955)
myHeap.insert(750)
myHeap.insert(800)
myHeap.insert(550)
myHeap.insert(600)
myHeap.insert(500)
myHeap.insert(650)

print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)

myHeap.remove()
print(myHeap.heap)





