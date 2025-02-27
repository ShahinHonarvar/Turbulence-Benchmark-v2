def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    result.add(i)
                if is_prime(n // i):
                    result.add(n // i)
        return result
    if len(numbers) < 50:
        return set()
    return factors(numbers[49])