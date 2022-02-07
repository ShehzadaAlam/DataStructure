from socketserver import ThreadingUnixStreamServer
from linkedlist import *

firstnode = Node("orange")
secondnode = Node("banana")
thirdnode = Node("grapes")

llist = LinkedList()
llist.head = firstnode

firstnode.next = secondnode
secondnode.next = thirdnode

print(llist)

strings = ["pineapple", "peach", "fig"]
llist2 = LinkedList(strings)
print(llist2)

for elem in llist2:
    print(elem)
