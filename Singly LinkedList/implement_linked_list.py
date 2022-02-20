from linkedlist import *

# firstnode = Node("orange")
# secondnode = Node("banana")
# thirdnode = Node("grapes")

# firstnode.next = secondnode
# secondnode.next = thirdnode

# llist = LinkedList()
# llist.head = firstnode
# print(llist)
# for elm in llist:
#     print(elm)

strings = ["pineapple", "peach", "fig", "Orange"]
llist2 = LinkedList(strings)
print(llist2)

for elem in llist2:
    print(elem)

llist2.add_first(Node("mango"))
llist2.add_last(Node("grapes"))
print(llist2)
print(len(llist2))

llist2.add_after("grapes", Node("Coconut"))
print(llist2)
print(len(llist2))


llist2.add_before("pineapple", Node("sugercane"))
print(llist2)
print(len(llist2))
llist2.remove_node("pineapple")
print(llist2)
print(len(llist2))
#

