def _getIndices(data,x,start,end,res):
    if start <= end:
 
        m = (start+end) // 2
        _getIndices(data,x,start,m-1,res)
        if data[m] == x:
            res.append(m)
        _getIndices(data,x,m+1,end,res)

def getIndices(data,x):
    if data is None or len(data) == 0:
        return 0
    res = []
    _getIndices(data,x,0,len(data)-1,res)
    return res


print(getIndices([5, 0, 3, 3, 4, 3, 1, 5, 2, 5, 1], 3))
