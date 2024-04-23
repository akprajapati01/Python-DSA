def isSorted(a): #this check for the if the element is sorted or not 
    l = len(a)
    if(l == 0 or l == 1):
        return True
    if a[0] > a[1] :
        return False
    Smaller = a[1:]
    isSmallersorted = isSorted(Smaller)
    #retuen isSmallersorted
    if isSmallersorted:
        return True
    else:
        return False
    
a = [1,2,3,4,35,6]
print(isSorted(a))