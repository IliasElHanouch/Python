def _quicksort(data,start,end):
    i = start
    j = end
    m = (end+start) // 2
    p = data[m]
    while i <= j:
        while data[i] < p:
            i+= 1
        while data[j] > p:
            j-= 1
        if i <= j:
            data[i],data[j] = data[j],data[i]
            i+= 1
            j-= 1

    if start < j:
        _quicksort(data,start,j)
    if end > i:
        _quicksort(data,i,end)
def quicksort(data):
    if data is None or len(data) <= 1:
        return
    _quicksort(data,0,len(data)-1)
a = [5, 7, -2, 7, 0, 1, 3, 6]
print(a)
_quicksort(a,0,len(a)-1)
print(a)
