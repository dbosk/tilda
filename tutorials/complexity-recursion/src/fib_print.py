def fib(n):
    """Computes n:th element in the Fibonacci sequence"""
    print(n, end=" ")
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
