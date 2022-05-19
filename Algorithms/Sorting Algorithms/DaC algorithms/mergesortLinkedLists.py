import random
from dlist import DList
from slist import SList
class DList2(DList):


    def __eq__(self,other):
        """returns True if self and other contains the same elements and in the same order. Otherwise,
        it returns False"""
        if other==None or len(self)!=len(other):
            return False
        
        nodeSelf=self._head
        nodeOther=other._head
        while nodeSelf:
            if nodeSelf.elem!=nodeOther.elem:
                return False
            nodeSelf=nodeSelf.next
            nodeOther=nodeOther.next
            
        return True



    def split(self):
        """splits the list in a half and returns the two parts as two doubly linked lists
        Complexity O(n)"""

        left=DList2()
        node=self._head
        for i in range(len(self)//2):
            left.addLast(node.elem)
            node=node.next

        right=DList2()
        for i in range(len(self)//2,len(self)):
            right.addLast(node.elem)
            node=node.next

        return left, right


    def merge(list1, list2):
        newList=DList()
		
        node1=list1._head
        node2=list2._head
        
        while node1 and node2:
            if node1.elem <= node2.elem:
                newList.addLast(node1.elem)
                node1=node1.next
            else:
                newList.addLast(node2.elem)
                node2=node2.next
		
        while node1:
            newList.addLast(node1.elem)
            node1=node1.next
		
        while node2:
            newList.addLast(node2.elem)
            node2=node2.next
		

        return newList
  
def mergesort(l):
    if l==None:
        return None
    if len(l)<=1:
        return l

    left,right=l.split()
    sorted1=mergesort(left)
    sorted2=mergesort(right)

    return SList2.merge(sorted1,sorted2)

class SList2(SList):


    def __eq__(self,other):
        """returns True if self and other contains the same elements and in the same order. Otherwise,
        it returns False"""
        if other==None or len(self)!=len(other):
            return False
        
        nodeSelf=self._head
        nodeOther=other._head
        while nodeSelf:
            if nodeSelf.elem!=nodeOther.elem:
                return False
            nodeSelf=nodeSelf.next
            nodeOther=nodeOther.next
            
        return True



    def split(self):
        """splits the list in a half and returns the two parts as two doubly linked lists
        Complexity O(n)"""

        left=SList2()
        node=self._head
        for i in range(len(self)//2):
            left.addLast(node.elem)
            node=node.next

        right=DList2()
        for i in range(len(self)//2,len(self)):
            right.addLast(node.elem)
            node=node.next

        return left, right


    def merge(list1, list2):
        newList=SList2()
		
        node1=list1._head
        node2=list2._head
        
        while node1 and node2:
            if node1.elem <= node2.elem:
                newList.addLast(node1.elem)
                node1=node1.next
            else:
                newList.addLast(node2.elem)
                node2=node2.next
		
        while node1:
            newList.addLast(node1.elem)
            node1=node1.next
		
        while node2:
            newList.addLast(node2.elem)
            node2=node2.next
        return newList


input=DList2()
for x in range(6):
    input.addLast(random.randint(0,25))

print('Input: ', input)

print("after mergesort:", mergesort(input))




l = SList2()
array=[-1,9,10,22,-87,5,6,1,7]
for x in array:
    l.addLast(x)
print(l)
print(mergesort(l))
