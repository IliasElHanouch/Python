def find_first_last(a: list, x: int):
    """returns the first and last indices of x in the list"""
    if a is None or len(a) == 0:
        return (-1,-1)
    n= _find_first_last(a,x,0,len(a)-1)
    return n

def _find_first_last(data,x,start,end):
    if start == end:
        if data[start] == x:
            return start,start
        return -1,-1
    if start < end:
        m = (start+end)//2
        first1,last1 = _find_first_last(data,x,start,m)
        first2,last2 = _find_first_last(data,x,m+1,end)
        first = -1
        if first1 != -1 and first2 != -1:
            first = min(last1,last2)
        elif first1 != -1 and first2 == -1:
            first = first1
        elif first1 == -1 and first2 != -1:
            first = first2
        last = max(last1,last2)
        return (first,last)

if __name__ == "__main__":
    b = [5, -2, 3, -2, 3, 6, 6, 0, 1, 2, -1, -1, 5,-2]
    print(b)
    for value in sorted(set(b)):
        first, last = find_first_last(b, value)
        print("x: ", value, ", first index:", first, ", last index: ", last)

    value = 4   # does not exist
    first, last = find_first_last(b, value)
    print("x: ", value, ", first index:", first, ", last index: ", last)
