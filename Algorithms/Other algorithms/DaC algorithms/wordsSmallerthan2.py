def _wordsSmaller2(data,start,end,output):
    if start == end:
        if len(data[start]) <= 2:
            output.append(data[start])
        else:
            pass
    if start < end:
        m = (start+end) // 2
        _wordsSmaller2(data,start,m,output)
        _wordsSmaller2(data,m+1,end,output)
def wordsSmaller2(data):
    res = []
    _wordsSmaller2(data,0,len(data)-1,res)
    return res




words=["Ha", "llegado", "el", "afilador", "a", "su", "domicilio", "a", "la", "puerta", "de", "su", "casa", "se", "afilan", "cuchillos", "tijeras"]
print(wordsSmaller2(words))
