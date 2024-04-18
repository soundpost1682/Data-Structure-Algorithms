class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        tmp = self.first
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        tmp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            tmp.next = None
        self.length -= 1
        return tmp


my_queue = Queue(11)
my_queue.enqueue(22)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

