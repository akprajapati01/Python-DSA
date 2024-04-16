def fibo(n):  #Fibonacci series
    if (n==1):    #we assume first element to be 1
        return 1
    fib_n_1 = fibo(n-1)
    fib_n_2 = fibo(n-2)
    output = fib_n_1+fib_n_2
    return output

n=int(input())
print(fibo(n))
    

