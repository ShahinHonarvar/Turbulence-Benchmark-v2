def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return set((factor for i in range(2, n // 2 + 1) if n % i == 0))
    number = lst[90] if len(lst) > 90 else None
    prime_factors_set = {factor for factor in factors(number) if is_prime(factor)} if number else {}
    return prime_factors_set