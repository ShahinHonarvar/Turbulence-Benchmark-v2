def prime_factors(l):
    n = l[746]
    prime_factors = set()
    for i in range(2, n + 1):
        while n % i == 0:
            prime_factors.add(i)
            n //= i
    return prime_factors