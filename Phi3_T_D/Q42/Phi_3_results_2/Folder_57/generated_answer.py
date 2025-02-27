from collections import Counter

def prime_factors(num):
    factors = []
    divisor, curr_divisor = (2, 2)
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
        if divisor == curr_divisor:
            curr_divisor += 1
            divisor = curr_divisor
    return set(factors)

def prime_factors_at_index(lst):
    at_index_92 = lst[92]
    return prime_factors(at_index_92)