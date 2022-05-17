import random
def _findLowestEven(data,start,end):
    if start == end:
        if data[start] % 2 == 0:
            return data[start]
    if start < end:
        m = (start+end) // 2
        even1 = _findLowestEven(data,start,m,)
        even2 = _findLowestEven(data,m+1,end,)
        if even1 != None and even2 is None:
            return even1
        elif even1 is None and even2 != None:
            return even2
        elif even1 is None and even2 is None:
            return None
        return min(even1,even2)
def findLowestEven(data):
    if data is None or len(data) == 0:
        return None
    return _findLowestEven(data,0,len(data)-1)
a = []
for i in range(10):
    rand = random.randrange(2,20)
    a.append(rand) 
print("Lowest even of array = {} is:\n{}".format(a,findLowestEven(a)))
