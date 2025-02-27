def prime_factors(lst):
    n = lst[1]
    factors = set()
    for i in range(2, n + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    return factors