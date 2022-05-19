def _firstOccurrence(data,x,start,end):
    if start == end:
        if data[start] == x:
            return start
        return -1
    if start < end:
        m = (start+end)//2
        find = _firstOccurrence(data,x,start,m)
        if find == -1:
            find = _firstOccurrence(data,x,m+1,end)
        return find
    else:
        return -1

def firstOccurrence(data,x):
    if data is None or len(data) == 0:
        return None
    return _firstOccurrence(data,x,0,len(data)-1)
    
print(firstOccurrence([2, 2, 5, 3, 5, 0, 5,0], 0))
