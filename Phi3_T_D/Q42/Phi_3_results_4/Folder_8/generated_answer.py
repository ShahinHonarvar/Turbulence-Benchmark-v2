def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        divisor = 2
        while num > 1:
            if num % divisor == 0:
                factors.add(divisor)
                num //= divisor
            else:
                divisor += 1
        return factors
    return get_prime_factors(numbers[49])