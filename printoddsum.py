def odprint(n):
        if(n == 0):
            return 0
        if(n == 1):
            return 1
            largeout = odprint(n-2)
            return largeout+n
        # smallout = odprint(n-1)
    largeout = odprint(n-2)
    return largeout+n


n=int(input())
print(odprint(n))  #This print the output of the sum