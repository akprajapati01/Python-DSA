def odprint(n):
    if(n-2)%2 != 0:
        if(n == 0):
            return 0
        if(n == 1):
            return 1
    # smallout = odprint(n-1)
    largeout = odprint(n-2)
    return largeout+n

n=int(input())
print(odprint(n))   #This give the sum of all the odd number till input

