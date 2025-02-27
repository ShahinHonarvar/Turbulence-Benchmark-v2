from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[86]
    truncatables = []

    def is_truncatable(n):
        if n < 10:
            return isprime(n)
        return isprime(n) and is_truncatable(n // 10)
    for num in range(23, x):
        if is_truncatable(num):
            truncatables.append(num)
    return truncatables