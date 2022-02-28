from doubly_linked_list import *

datastr = ["mango", "raspberry", "grapes"]
dll = DoublyLinkedList(datastr)
print(dll)
print(len(dll))

dll.add_first(Node("pineapple"))
print(dll)

dll.add_last(Node("banana"))
print(dll)

dll.add_after("raspberry", Node("fig"))
print(dll)

dll.add_before("banana", Node("papaya"))
print(dll)

dll.add_before("pineapple", Node("watermelon"))
print(dll)

dll.remove_node("raspberry")
print(dll)
