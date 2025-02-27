def prime_factors(lst):
    return set((f for n in [lst[57]] for i in range(2, n + 1) if n % i == 0 and all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))))