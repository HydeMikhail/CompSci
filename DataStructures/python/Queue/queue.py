#!/home/mhyde/vEnvs/py36/bin/python

from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, data):
        if self.has_space():
            new_node = Node(data)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.set_next_node(new_node)
                self.tail = new_node
            self.size += 1
        else:
            print('Queue Overflow Protected. Node not Enqueued.')

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_data()
        else:
            print('Queue Underflow Protected. Nothing to Dequeue.')

    def has_space(self):
        return self.size < self.max_size

    def is_empty(self):
        return self.size == 0

if __name__ == '__main__':
    queue = Queue(5)
    print('\n')
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    queue.enqueue('D')
    queue.enqueue('E')
    queue.enqueue('F')
    print('\n')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print('\n')
