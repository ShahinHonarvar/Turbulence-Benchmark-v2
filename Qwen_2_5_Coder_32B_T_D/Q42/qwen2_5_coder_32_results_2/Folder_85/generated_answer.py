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
                result.add(i)
                result.add(n // i)
        return result
    if len(numbers) < 24:
        return set()
    n = numbers[23]
    all_factors = factors(n)
    return {f for f in all_factors if is_prime(f)}