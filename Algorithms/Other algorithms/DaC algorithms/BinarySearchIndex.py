def binarySearchIndex(data,x,start,end):
    if start <= end:
        m = (start+end)//2
        if data[m] == x:
            return m
        if x < data[m]:
            return binarySearchIndex(data,x,start,m-1)
        return binarySearchIndex(data,x,m+1,end)
    return -1
def BinarySearch(data,x):
    if data is None or len(data) == 0 or not(sorted(data)):
        return None
    return binarySearchIndex(data,x,0,len(data)-1)



a=[1, 4, 38, 39, 40, 61, 69, 71, 81, 87]

x=71 #an element that exists
print("binarySearch({},{})=Index({})\n".format(a,x,BinarySearch(a,x)))

#An element that does not exist
x=50
print("binarySearch({},{})=Index({})\n".format(a,x,BinarySearch(a,x)))
