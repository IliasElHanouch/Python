def _BinarySearch(data,x,start,end):
    if start <= end:
        m = (start+end)//2
        if data[m] == x:
            return True
        if x < data[m]:
            return _BinarySearch(data,x,start,m-1)
        return _BinarySearch(data,x,m+1,end)
    return False
def BinarySearch(data,x):
    if data is None or len(data) == 0 or not(sorted(data)):
        return None
    return _BinarySearch(data,x,0,len(data)-1)



a=[1, 4, 38, 39, 40, 61, 69, 71, 81, 87]

x=71 #an element that exists
print("binarySearch({},{})={}\n".format(a,x,BinarySearch(a,x)))

#An element that does not exist
x=50
print("binarySearch({},{})={}\n".format(a,x,BinarySearch(a,x)))
