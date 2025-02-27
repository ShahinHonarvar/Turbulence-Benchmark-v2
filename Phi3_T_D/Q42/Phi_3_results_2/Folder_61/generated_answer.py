def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                n //= i
                factors.add(i)
            if n == 1:
                break
        return factors
    if len(numbers) > 8:
        return get_prime_factors(numbers[8])
    else:
        raise IndexError('List does not contain enough elements.')