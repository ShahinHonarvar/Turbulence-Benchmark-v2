from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(lst):
    if len(lst) < 11 or not isinstance(lst[10], int) or lst[10] <= 1:
        return set()
    factors = set()
    n = lst[10]
    while n % 2 == 0:
        (factors.add(2),)
        n //= 2
    while n > 1:
        if is_prime(n):
            factors.add(n)
            break
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
    return factors