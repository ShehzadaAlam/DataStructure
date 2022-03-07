class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


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

    def add_after(self, target_node_data, node):
        if not self.head:
            raise Exception("List is currently empty")
        for current_node in self:
            if current_node.data == target_node_data:
                node.next = current_node.next
                current_node.next = node
                node.previous = current_node
                return
        raise Exception("Target node is not found")

    def add_before(self, target_data_node, node):
        if not self.head:
            raise Exception("list is currently empty")
        if self.head.data == target_data_node:
            self.add_first(node)
            return

        for current_node in self:
            if current_node.data == target_data_node:
                node.next = current_node
                node.previous = current_node.previous
                current_node.previous.next = node
                current_node.previous = node
                return
        raise Exception("Target node is not found")

    def remove_node(self, node_data):
        if not self.head:
            raise Exception("list is currently empty")
        if self.head.data == node_data:
            self.head = self.head.next
            return
        for current_node in self:
            if current_node.data == node_data and current_node.next is not None:
                current_node.previous.next = current_node.next
            elif current_node.data == node_data and current_node.prev is not None:
                current_node.next.previous = current_node.previous
                return
        raise Exception("Target node is not found")

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
