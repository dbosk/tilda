def fib(n):
    """Computes n:th number in the Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
