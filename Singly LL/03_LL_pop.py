class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1



# check Nodes via printing
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):       # created a node
        new_node = Node(value)     
        if self.length == 0:      # if this is empty
            self.head = new_node
            self.tail = new_node
        else:                      # or 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1            # add the node
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

my_LL = LinkedList(3)
my_LL.append(5)
my_LL.append(8)
my_LL.pop()
my_LL.pop()
my_LL.printlist()

