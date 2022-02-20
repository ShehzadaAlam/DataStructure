class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                newnode = Node(data=elem)
                node.next = newnode
                newnode.previous = node
                node = node.next

    def add_first(self, node):
        if not self.head:
            self.head = node
        self.head.previous = node
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
        for current_node in self:
            pass
        current_node.next = node
        node.previous = current_node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("Linked list is empty")
        for current_node in self:
            if current_node.data == target_node_data:
                new_node.next = current_node.next
                new_node.prevous = current_node
                current_node.next = new_node
                return

    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.next
        return count

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

