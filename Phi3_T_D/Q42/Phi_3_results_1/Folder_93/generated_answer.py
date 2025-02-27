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
            while num % divisor == 0 and is_prime(divisor):
                factors.add(divisor)
                num //= divisor
            divisor += 1
        return factors
    if 45 < len(numbers):
        return get_prime_factors(numbers[45])
    else:
        return set()