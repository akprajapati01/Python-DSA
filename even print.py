def evenprint(n):
    if(n-2)%2 == 0:
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        largeout = evenprint(n-2)
        return largeout+n

n=int(input())
print(evenprint(n)) 