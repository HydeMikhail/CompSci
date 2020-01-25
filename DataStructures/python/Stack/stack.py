#/home/mhyde/vEnvs/py36/bin/python

from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def peek(self):
        if not self.stack_underflow_cond():
            return self.top_item.get_data()
        else:
            return False

    def pop(self):
        if not self.stack_underflow_cond():
            item_to_return = self.top_item
            self.top_item = item_to_return.get_next_node()
            self.size -= 1
            return item_to_return.get_data()
        else:
            return False

    def push(self, data_to_enter):
        if self.stack_overflow_cond():
            node_to_enter = Node(data_to_enter)
            node_to_enter.set_next_node(self.top_item)
            self.top_item = node_to_enter
            self.size += 1
        else:
            return False

    def stack_underflow_cond(self):
        return self.size == 0

    def stack_overflow_cond(self):
        return self.size < self.limit

if __name__ == '__main__':
    stack = Stack(5)
    stack.push('E')
    print(stack.size)
    stack.push('D')
    print(stack.size)
    stack.push('C')
    print(stack.size)
    stack.push('B')
    print(stack.size)
    stack.push('A')
    print(stack.size)
    stack.pop()
    print(stack.size)
    stack.pop()
    print(stack.size)
    stack.pop()
    print(stack.size)
    print(stack.peek())
    print(stack.size)
    stack.pop()
    print(stack.size)
    print(stack.peek())
    print(stack.size)