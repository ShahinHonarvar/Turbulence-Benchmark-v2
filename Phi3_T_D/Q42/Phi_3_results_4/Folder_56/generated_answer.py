def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0:
                factors.add(i)
        return factors
    return find_prime_factors(numbers[60]) if len(numbers) > 60 else set()