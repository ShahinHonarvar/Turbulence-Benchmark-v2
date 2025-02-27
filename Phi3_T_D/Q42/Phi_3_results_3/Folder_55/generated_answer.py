def prime_factors(lst):

    def factors(n):
        return set((prod for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for prod in (i, n // i)))

    def is_prime(num):
        return num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
    num_to_factorize = lst[21]
    return {num for num in factors(num_to_factorize) if is_prime(num)}