class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, new_node):
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node):
        if not self.head:
            self.head = new_node
            return
        for current_node in self:
            pass
        current_node.next = new_node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("Linked list is empty")
        for elem in self:
            if elem.data == target_node_data:
                new_node.next = elem.next
                elem.next = new_node
                return
        raise Exception("Target node data is not found")

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("Linked list is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for elem in self:
            if elem.data == target_node_data:
                prev_node.next = new_node
                new_node.next = elem
                return
            prev_node = elem
        raise Exception("Target node is not found")

    def remove_node(self, target_node):
        if not self.head:
            raise Exception("Linked list is empty")
        if self.head.data == target_node:
            self.head.next = target_node.next
            self.head = target_node
            return
        prev_node = self.head
        for elem in self:
            if elem.data == target_node:
                prev_node.next = elem.next
                return
            prev_node = elem
        raise Exception("Target node is not found")

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.next
        return count
