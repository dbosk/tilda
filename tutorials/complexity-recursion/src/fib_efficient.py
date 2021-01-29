def fib(n):
    """Computes n:th number in the Fibonacci sequence"""
    f0 = 0
    f1 = 1
    for i in range(n-1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f1
