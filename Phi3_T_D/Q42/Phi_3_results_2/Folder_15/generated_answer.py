def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return set((x for i in range(2, n // 2 + 1) if n % i == 0 and is_prime(i)))
    if 10 < len(numbers) and type(numbers) is list:
        return factors(numbers[10])
    return set()