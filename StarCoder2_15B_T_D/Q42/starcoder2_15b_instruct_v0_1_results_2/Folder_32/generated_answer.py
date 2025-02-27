def prime_factors(lst):
    if len(lst) <= 849:
        raise ValueError('Index 849 is out of range.')
    n = lst[849]
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors