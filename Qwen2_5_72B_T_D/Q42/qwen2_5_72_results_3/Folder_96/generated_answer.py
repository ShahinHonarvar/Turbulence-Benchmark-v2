def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 and is_prime(i):
                factors.add(i)
            other_factor = n // i
            if n % other_factor == 0 and is_prime(other_factor):
                factors.add(other_factor)
        if is_prime(n):
            factors.add(n)
        return factors
    if len(numbers) > 47:
        return get_factors(numbers[47])
    return set()