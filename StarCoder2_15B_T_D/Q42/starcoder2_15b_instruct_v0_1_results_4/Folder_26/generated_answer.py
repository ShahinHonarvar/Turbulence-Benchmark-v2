def prime_factors(numbers):
    n = numbers[222]
    prime_factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n = n // i
        else:
            i += 1
    return set(prime_factors)