def prime_factors(numbers):
    p = 2
    factors = set()
    n = numbers[71]
    while n > 1:
        if n % p == 0:
            factors.add(p)
            n //= p
        else:
            p += 1
    return factors