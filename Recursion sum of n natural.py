# def sum(n):
#     if(n==0):
#         return 0
#     return n+sum(n-1)

def sum_n(n):
    if(n==0):
        return 0
    small_out = sum_n(n-1)
    return small_out + n

k=int(input())


print(sum_n(k))