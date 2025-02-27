def prime_factors(lst):
    return set([i for i in range(2, lst[685] + 1) if lst[685] % i == 0 and all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))])