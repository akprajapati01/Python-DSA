def odprint(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    smallout = odprint(n-1)
    return (smallout + n)
   

# n=int(input())
# print(odprint(n))
n=5
print(odprint(n))
