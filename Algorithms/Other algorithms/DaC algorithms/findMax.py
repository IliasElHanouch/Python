import random
def _findMax(data,start,end):
    if start == end:
        return data[start]
    if start<end:
        m = (start+end)//2
        findMax1 = _findMax(data,start,m)
        findMax2 = _findMax(data,m+1,end)
        return max(findMax1,findMax2)
def findMax(data):
    if data is None or len(data) == 0:
        return None
    return _findMax(data,0,len(data)-1)


a = []
for i in range(1000):
    rand = random.randint(-1000,1000)
    a.append(rand)
print(max(a) == findMax(a))
