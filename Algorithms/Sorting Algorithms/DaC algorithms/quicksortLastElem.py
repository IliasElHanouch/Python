import random
import time
def _quicksort(data,start,end):
    p = data[end]
    i = start
    j = end-1
    while i <= j:
        while data[i] < p:
            i+= 1
        while data[j] > p:
            j-= 1
        if i <= j:
            data[i],data[j] = data[j],data[i]
            i+= 1
            j-= 1
    data[end],data[i] = data[i],data[end]

    if start < i-1:
        _quicksort(data,0,i-1)
    if end > i+1:
        _quicksort(data,i+1,end)

def quicksort(data):
    if data is None or len(data) <= 1:
        return
    _quicksort(data,0,len(data)-1)


    
a = []
for i in range(400):
    a.append(random.randrange(-50,50))
start = time.time()
quicksort(a)
end = time.time()
print(end-start)
print(sorted(a)==a)