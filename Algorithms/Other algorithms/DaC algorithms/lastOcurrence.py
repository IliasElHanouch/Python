def _lastOccurrence(data,x,start,end):
    if start == end:
        if data[start] == x:
            return start
        return -1
    if start < end:
        m = (start+end)//2
        part1 = _lastOccurrence(data,x,start,m)
        part2 = _lastOccurrence(data,x,m+1,end)  
        return max(part1,part2)
    return -1

def lastOccurrence(data,x):
    if data is None or len(data) == 0:
        return None
    return _lastOccurrence(data,x,0,len(data)-1)

print(lastOccurrence([2, 2, 5, 3, 5, 0, 5], 5))
