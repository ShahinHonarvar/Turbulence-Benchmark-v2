def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0:
                if is_prime(i):
                    factors.add(i)
                num //= i
        return factors
    if len(numbers) > 15:
        return prime_factors_of(numbers[15])
    return set()