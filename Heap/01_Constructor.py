class maxHeap:
    def __init__(self) :
        self.heap = []
    
    def leftChild(self, idx):
        return 2* idx + 1
    def rightChild(self, idx):
        return 2* idx + 2
    def parent(self,idx):
        return (idx-1) // 2
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        
