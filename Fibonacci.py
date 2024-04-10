def fibo(n):
    if n==0:
        return 1
    fib_n_1 = fibo(n-1)
    fib_n_2 = fibo(n-2)