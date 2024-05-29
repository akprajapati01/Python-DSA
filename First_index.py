def firstIndex(a,x):  #This is Used to find the index of first element is given number is found
    l = len(a)
    if l == 0:   #For Empty Element
        return -1
    if a[0] == x: #First case checking with the first element of array
        return 0. #this return 0

    smalllist = a[1:]
    lo = sl(smalllist,x)  #x is the searching element
    if lo == -1:
        return -1
    else:
        return +1