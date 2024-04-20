# def fact(n):
#     if(n==0):
#         return 1
#     return n*fact(n-1)
import sys
sys.setrecursionlimit(1000)

def factorial(n):
    if(n==0):
        return 1
    small = factorial(n-1)
    return n*small 
  
# f=fact(5)
# print(f)

n=int(input())
print(factorial(n))