def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            if n % i == 0:
                result.add(i)
        return result

    def prime_factors_set(n):
        result = set()
        for f in factors(n):
            if is_prime(f):
                result.add(f)
        return result
    return prime_factors_set(numbers[77])