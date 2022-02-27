class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self, data_node):
        if data_node is not None:
            new_node = Node(data=data_node.pop(0))
            self.head = new_node
            for data in data_node:
                current_node = Node(data)
                new_node.next = current_node
                current_node.previous = new_node
                new_node = new_node.next

    def add_first(self, node):
        if not self.head:
            self.head = None
            return
        node.next = self.head
        self.head.previous = node
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = None
            return
        for current_node in self:
            pass
        current_node.next = node
        node.previous = current_node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " <-> ".join(nodes)

    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.next
        return count
