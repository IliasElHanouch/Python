def bubbleSort(lista:list) -> list:
    swapping = True
    num = len(lista) - 1
    while swapping and num > 0:
        swapping = False
        for i in range(num):
            if lista[i] > lista[i+1]:
                swapping = True
                lista[i+1], lista[i] = lista[i],lista[i+1]
        num -= 1
    return lista
print(bubbleSort([5,3,2,6,-1,4,2]))
