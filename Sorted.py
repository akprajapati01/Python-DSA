def isSorted(a): #this check for the if the element is sorted or not 
    l = len(a)
    if(l == 0 or l == 1):
        return True
    if a[0] > a[1] :
        return False
    Smaller = a[1:]
    isSmallersorted = isSorted(Smaller)
    return isSmallersorted
    # if isSmallersorted:
    #     return True
    # else:
    #     return False
    
# a = [1,2,3,4,5,6]
a=[9,8,7,6,5,4,3,2,1]
print(isSorted(a))