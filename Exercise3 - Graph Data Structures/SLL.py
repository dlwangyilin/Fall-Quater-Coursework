class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def appendFirst(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head.next
            self.head = node
        self.size += 1

    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data

    def getsize(self):
        return self.size

if __name__ == '__main__':
    A = LinkedList()
    A.append(2)
    A.append(5)
    print(A.getsize())
    for node in A.iter():
        print('node is {0}'.format(node))