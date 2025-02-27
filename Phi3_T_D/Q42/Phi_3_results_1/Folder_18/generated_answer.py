def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
        return factors
    return find_prime_factors(numbers[312]) if len(numbers) > 312 else set()