from socketserver import ThreadingUnixStreamServer
from linkedlist import *

firstnode = Node("orange")
secondnode = Node("banana")
thirdnode = Node("grapes")

firstnode.next = secondnode
secondnode.next = thirdnode

llist = LinkedList()
llist.head = firstnode
print(llist)
for elm in llist:
    print(elm)

# strings = ["pineapple", "peach", "fig"]
# llist2 = LinkedList(strings)
# print(llist2)

# for elem in llist2:
#     print(elem)
