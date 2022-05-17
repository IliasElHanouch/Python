import time
import random
def merge(data,start,end,m):
    i,j = start,m+1
    aux =[]

    while i <= m and j<= end:
        if data[i] <= data[j]:
            aux.append(data[i])
            i+=1
        else:
            aux.append(data[j])
            j+=1
    while i <= m:
        aux.append(data[i])
        i+=1
    while j<= end:
        aux.append(data[j])
        j+=1
    
    for k in range(start,end+1):
        data[k] = aux[k-start]

def _mergesort(data,start,end):
    if start < end:
        m = (start+end) // 2
        _mergesort(data,start,m)
        _mergesort(data,m+1,end)

        merge(data,start,end,m)

def mergesort(data):
    if len(data) <= 1 or data is None:
        return []
    _mergesort(data,0,len(data)-1)


a = []
start = time.time()
for i in range(10000000):
    rand = random.randint(-1000,1000)
    a.append(rand)

#print(a)
mergesort(a)
#print(a)
end = time.time()
#print(a)
print(end-start)

print(a == sorted(a))

