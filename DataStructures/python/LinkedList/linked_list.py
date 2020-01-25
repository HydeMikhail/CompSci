#!/home/mhyde/vEnvs/py36/bin/python

from node import Node

class LinkedList:
    def __init__(self, data=None):
        self.head_node = Node(data)

    def insert_head_node(self, new_data):
        new_node = Node(new_data)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def remove_node(self, data_to_remove):
        current_node = self.head_node
        if current_node.data == data_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.data == data_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_data() != None:
                string_list += str(current_node.get_data()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
            

if __name__ == '__main__':

    list1 = LinkedList('D')
    list1.insert_head_node('C')
    list1.insert_head_node('B')
    list1.insert_head_node('A')

    print(list1.stringify_list())

    list1.remove_node('C')

    print(list1.stringify_list())

    list1.remove_node('B')
    list1.insert_head_node('K')

    print(list1.stringify_list())
