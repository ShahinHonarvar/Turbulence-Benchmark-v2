from math import sqrt

def prime_factors(num):
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
        if divisor * divisor > num:
            if num > 1:
                factors.add(num)
            break
    return factors

def prime_factors_at_index(lst, index):
    number = lst[index]
    return prime_factors(number)