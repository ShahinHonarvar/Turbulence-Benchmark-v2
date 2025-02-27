from math import sqrt

def prime_factors(lst):
    p = lst[87]
    factors = set()
    while p % 2 == 0:
        (factors.add(2),)
        p //= 2
    for i in range(3, int(sqrt(p)) + 1, 2):
        while p % i == 0:
            factors.add(i)
            p //= i
    if p > 2:
        factors.add(p)
    return factors