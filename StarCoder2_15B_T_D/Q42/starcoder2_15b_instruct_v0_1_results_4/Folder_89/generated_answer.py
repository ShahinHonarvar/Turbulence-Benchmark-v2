def prime_factors(numbers):
    n = numbers[18]
    factors = set()
    d = 2
    while n > 1:
        while n % d == 0:
            factors.add(d)
            n /= d
        d += 1
    return factors