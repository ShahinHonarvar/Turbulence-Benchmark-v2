from math import sqrt

def prime_factors(lst):
    _div = 2
    prime_factors = set()
    num = lst[276]
    while num % _div == 0:
        prime_factors.add(_div)
        num //= _div
    p = 3
    while p <= int(sqrt(num)) and num > 1:
        while num % p == 0:
            prime_factors.add(p)
            num //= p
        p += 2
    if num > 2:
        prime_factors.add(num)
    return prime_factors