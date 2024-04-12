def fibo(n):
    if (n==1):
        return 1
    fib_n_1 = fibo(n-1)
    fib_n_2 = fibo(n-2)
    return fib_n_1+fib_n_2

n=int(input())
print(fibo(n))