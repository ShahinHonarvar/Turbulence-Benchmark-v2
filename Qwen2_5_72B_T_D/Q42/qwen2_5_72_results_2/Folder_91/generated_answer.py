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
    number = numbers[6]
    all_factors = factors(number)
    prime_factors_set = set(filter(is_prime, all_factors))
    return prime_factors_set