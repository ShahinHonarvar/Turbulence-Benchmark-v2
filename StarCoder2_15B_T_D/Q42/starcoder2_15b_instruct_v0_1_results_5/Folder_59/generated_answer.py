def prime_factors(l):
    n = l[2]
    prime_factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    return set(prime_factors)