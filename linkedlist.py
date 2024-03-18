"""
class LinkedList:
    def __init__(self,node):

    def add(self,node):



class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


    def prtn(self):
        print(f"{self.val} next->", self.next.val)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
 
node1.next = node2
node2.next = node3

lnkedlist = LinkedList(node1)
lnkedlist.add(node2)
lnkedlist.add(node3)
lnkedlist.prntlnk()"""
