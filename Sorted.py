def isSorted(a):
    l = len(a)
    if(l == 0 or l == 1):
        return True
    if a[0] > a[1] :
        return False
    Smaller = b[1:]
    isSmallersorted = isSorted(Smaller)
    #retuen isSmallersorted
    if isSmallersorted:
        return True
    else:
        return False
    
a = [1,2,3,4,5,6]
isSorted(a)