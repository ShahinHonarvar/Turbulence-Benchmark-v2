def prime_factors(numbers):
    n = numbers[96]
    prime_factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            prime_factors.append(d)
            n //= d
        else:
            d += 1
    return set(prime_factors)