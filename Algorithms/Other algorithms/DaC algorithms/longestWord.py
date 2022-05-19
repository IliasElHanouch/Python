def _longestWord(data,start,end):
    if start == end:
        return data[start]
    if start < end:
        m = (start+end)//2
        part1 = _longestWord(data,start,m)
        part2 = _longestWord(data,m+1,end)
        if len(part1) > len(part2):
            return part1
        return part2
def longestWord(data):
    if data is None or len(data) == 0:
        return None
    return _longestWord(data,0,len(data)-1)
a = ["perro","juan","elefante","oscar"]
print(longestWord(a))
