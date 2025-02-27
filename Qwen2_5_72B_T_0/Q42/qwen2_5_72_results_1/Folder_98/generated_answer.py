def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return [i for i in range(2, n + 1) if n % i == 0]
    if len(numbers) < 5:
        return set()
    num = numbers[4]
    all_factors = factors(num)
    prime_factors = [factor for factor in all_factors if is_prime(factor)]
    return set(prime_factors)