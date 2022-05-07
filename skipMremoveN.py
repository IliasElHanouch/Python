from platform import node


class DNode:
  def __init__(self, elem, next=None, prev=None ):
    self.elem = elem
    self.next = next
    self.prev = prev


class DList:
    def __init__(self):
        """creates an empty list"""
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        """returns the number of elements of the list"""
        return self.size
    
    def add(self,e):
        """This functions adds e to the end of the list"""
        #create the new node
        newNode=DNode(e)
        
        if len(self)==0:
            self.head=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
        
        #update the reference of head to point the new node
        self.tail=newNode
        #increase the size of the list  
        self.size=self.size+1


    def getAt(self,index):
        """Returns the elem at the index position in the list"""
        
        #first, check the index is a right position in the list
        if index<0 or index>=self.size:
            print(index,'error: index out of range')
            return None
        
        #we need to reach the node at the index position in the list
        i=0
        current=self.head
        while  i<index:
            current=current.next
            i+=1
        #here, current is the node at the index position in the list
        #we return its elem
        return current.elem

    def __str__(self):
        """Returns a string with the elements of the list"""
        temp=self.head
        result=''
        while temp:
            result=result+'<->'+str(temp.elem)
            temp=temp.next
        if len(result)>0:
            result=result[3:]
        return result
    def skipMremoveN(self,m,n):
        #Lanzo excepción
        if m <= 0 or n <= 0:
            print("Parámetros incorrectos")
        #El nodo previo (justo después de él se empezará a borrar)
        previous = self.head
        #Mientras no llegue a None ese nodo
        while previous != None:
            #En el rango de lo que vayamos a conservar -1
            for i in range(m-1):
                #Actualizamos el nodo previo
                previous = previous.next
                #En caso de que sea el último (lo siguiente sería None), rompemos el bucle
                if previous.next == None:
                    break
            #Ahora vamos a usar un contador para sacar la longitud de la lista borrada
            count = 0
            #El nuevo nodeIt va a ser el siguiente de previous (el que no sea None lo controlaré)
            nodeIt = previous.next
            #Ahora en el rango de lo que vaya a borrar
            for i in range(n):
                #Si resulta que nodeIt es None; rompo el bucle 
                if nodeIt == None:
                    break
                #Actualizo nodeIt hasta donde tenga que llegar la eliminación
                nodeIt = nodeIt.next
                #Y en cada n iteración contador se resta -1
                count += 1
            #"Engancho" los nodos; el siguiente a previo es el nuevo nodeIt ya iterado
            previous.next = nodeIt
            #El nuevo previo es nodeIt ahora
            previous = nodeIt
            #Decremento la lista
            self.size -= count   
l = DList()
for i in range(1,15):
    l.add(i)
print(l)
l.skipMremoveN(2,3)
print(l)


import unittest

class Test(unittest.TestCase):
  
    #static variable to save your mark
    mark=0
    
    def setUp(self):
        self.l=DList()
        for k in range(1,15):
            self.l.add(k)

    def testz_printMark(self):
        print('\n\n*************************')
        print("\tProvisional mark:",Test.mark)  
        print('*************************') 

 

    def test1_skipMdeleteN(self):
        print('\nCase 1: M=1, N=1')
        #1<->3<->5<->7<->9<->11<->13
        expected=[1,3,5,7,9,11,13]
        
        print('input:   ',str(self.l))
        self.l.skipMremoveN(1,1)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 2')
        Test.mark+=2

    def test2_skipMremoveN(self):
        print('\nCase 2: M=1, N=4')
        expected=[1,6,11]
        print('input:   ',str(self.l))
        self.l.skipMremoveN(1,4)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 2')
        Test.mark+=2

    def test3_skipMremoveN(self):
        print('\nCase 3: M=2, N=2')
        expected=[1,2,5,6,9,10,13,14]

        print('input:   ',str(self.l))
        self.l.skipMremoveN(2,2)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 2')
        Test.mark+=2

    def test4_skipMremoveN(self):
        print('\nCase 4: M=2, N=3')
        expected=[1,2,6,7,11,12]

        print('input:   ',str(self.l))
        self.l.skipMremoveN(2,3)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 2')
        Test.mark+=2

    def test5_skipMremoveN(self):
        print('\nCase 5: M=3, N=1')
        #1<->2<->3<->5<->6<->7<->9<->10<->11<->13<->14
        expected=[1,2,3,5,6,7,9,10,11,13,14]

        print('input:   ',str(self.l))
        self.l.skipMremoveN(3,1)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 2')
        Test.mark+=2

    def test6_skipMremoveN(self):
        print('\nCase 6: M=3, N=3')
        #1<->2<->3<->7<->8<->9<->13<->14
        expected=[1,2,3,7,8,9,13,14]

        print('input:   ',str(self.l))
        self.l.skipMremoveN(3,3)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 2')
        Test.mark+=2

    
    def test7_skipMremoveN(self):
        print('\nCase 7: M=3, N=11')
        #1<->2<->3
        expected=[1,2,3]

        print('input:   ',str(self.l))
        self.l.skipMremoveN(3,11)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 2')
        Test.mark+=2

    def test8_skipMremoveN(self):
        print('\nCase 8: M=14, N=1')
        expected=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

        print('input:   ',str(self.l))
        self.l.skipMremoveN(14,1)
        print('result:  ',self.l)
        print('expected:',expected)
        #both lists should have the samel length
        self.assertEqual(len(self.l),len(expected))
        for i in range(len(self.l)):
            self.assertEqual(self.l.getAt(i),expected[i])
        print('\t\t mark += 1')
        Test.mark+=1

#Comentar para usarlo en spyder
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
#if __name__ == '__main__':
#    unittest.main()
