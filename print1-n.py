def firstnatural(n):
    if (n==0):
        return
    firstnatural(n-1)   #This is base case for PMI (Principal of Mathematical Induction)
    print(n)
    return

n = int(input())
firstnatural(n)