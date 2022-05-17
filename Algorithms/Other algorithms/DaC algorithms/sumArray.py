def _sumArray(data,start,end):
    if start == end:
        return data[start]
    if start < end:
        m = (start+end)//2
        s1 = _sumArray(data,start,m)
        s2 = _sumArray(data,m+1,end)
        return s1+s2
def sumArray(data):
    return _sumArray(data,0,len(data)-1)
import random
a = []
for i in range(205):
    rand = random.randrange(-30,40)
    a.append(rand)
print(sumArray(a)==sum(a))
