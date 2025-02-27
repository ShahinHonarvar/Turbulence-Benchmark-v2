def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorize(n):
        factors = set()
        for i in range(2, n + 1):
            while is_prime(i) and n % i == 0:
                factors.add(i)
                n //= i
        return factors
    if len(numbers) <= 74:
        return set()
    return factorize(numbers[74])