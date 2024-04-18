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

my_queue = Queue(4)
my_queue.print_queue()