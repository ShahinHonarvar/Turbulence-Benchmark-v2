def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        return factors
    return get_factors(numbers[851]) if 851 < len(numbers) else set()