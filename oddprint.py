def odprint(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    smallout = odprint(n-1)
    largeout = odprint(n-2)
    return (smallout + largeout)

