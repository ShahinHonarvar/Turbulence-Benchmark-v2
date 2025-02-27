def prime_factors(numbers):
    n = numbers[64]
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    factors.append(n)
    return set(factors)