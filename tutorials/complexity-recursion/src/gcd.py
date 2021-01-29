def gcd(m, n):
    """Computes the GCD of m and n"""
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)
