from doubly_linked_list import *

datastr = ["mango", "raspberry", "grapes"]
dll = DoublyLinkedList(datastr)
print(dll)
print(len(dll))

dll.add_first(Node("pineapple"))
print(dll)
# print(dll.head.next.next)

dll.add_last(Node("banana"))
print(dll)

# dll.add_after("raspberry", Node("fig"))
# print(dll)
# print(dll.head.next.next.next.previous)

