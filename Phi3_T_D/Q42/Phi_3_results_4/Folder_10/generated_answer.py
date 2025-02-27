from collections import Counter

def prime_factors(num):
    factors = Counter()
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            factors[divisor] += 1
            num //= divisor
        divisor += 1
    if num > 1:
        factors[num] += 1
    return set(factors.elements())