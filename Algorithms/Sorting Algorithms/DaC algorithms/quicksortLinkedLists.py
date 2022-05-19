import random
from dlist import DList,DNode
from slist import SList,SNode

class DList2(DList):
    def __add__(self, other):
        if other is None:
            return self
        nodeIt = other._head
        while nodeIt:
            self.addLast(nodeIt.elem)
            nodeIt = nodeIt.next
        return self


    def partitions(self):
        p = self._tail
        smaller = DList2()
        bigger = DList2()
        nodeIt = self._head
        while nodeIt.next:
            if nodeIt.elem <= p.elem:
                smaller.addLast(nodeIt.elem)
            else:
                bigger.addLast(nodeIt.elem)
            nodeIt = nodeIt.next
        pivote = DList2()
        pivote.addLast(p.elem)
        return smaller, pivote, bigger


    def quicksort(self):
        if self is None or len(self) <= 1:
            return self
        list_smaller, pivote, list_bigger = self.partitions()
        return list_smaller.quicksort() + pivote + list_bigger.quicksort()




class SList2(SList):
    def __add__(self, other):
        if other is None:
            return self
        nodeIt = other._head
        while nodeIt:
            self.addLast(nodeIt.elem)
            nodeIt = nodeIt.next
        return self


    def partitions(self):
        p = self._tail
        smaller = DList2()
        bigger = DList2()
        nodeIt = self._head
        while nodeIt.next:
            if nodeIt.elem <= p.elem:
                smaller.addLast(nodeIt.elem)
            else:
                bigger.addLast(nodeIt.elem)
            nodeIt = nodeIt.next
        pivote = DList2()
        pivote.addLast(p.elem)
        return smaller, pivote, bigger


    def quicksort(self):
        if self is None or len(self) <= 1:
            return self
        list_smaller, pivote, list_bigger = self.partitions()
        return list_smaller.quicksort() + pivote + list_bigger.quicksort()

# Código de prueba
DList_prueba = DList2()
for i in range(10):
    element = random.randint(-50, 50)
    DList_prueba.addLast(element)
print("DList is: {}".format(DList_prueba))
DList_prueba = DList_prueba.quicksort()
print("DList sorted is: {}".format(DList_prueba))


#Prueba con SList
l = SList2()
for i in range(10):
    l.addLast(random.randint(-10,11))
print("SList is: {}".format(l))

print("SList sorted is: {}".format(l.quicksort()))
