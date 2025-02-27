def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                yield i
                if i != n // i:
                    yield (n // i)
    target_number = numbers[28]
    return {factor for factor in factors(target_number) if is_prime(factor)}