def gcf_two_nums(numbers):
    prime_factors = lambda n: set((x for tup in ([p, n // p] for p in range(1, int(n ** 0.5) + 1) if n % p == 0) for x in tup))
    num_85 = prime_factors(numbers[85])
    num_51 = prime_factors(numbers[51])
    common_factors = num_85.intersection(num_51)
    return max(common_factors) if common_factors else 1