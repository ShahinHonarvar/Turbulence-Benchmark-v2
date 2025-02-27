def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                factors.add(divisor)
                num //= divisor
            divisor += 1
            if not is_prime(divisor):
                divisor += 1
        return factors
    return get_prime_factors(numbers[714]) if len(numbers) > 714 else 'Index out of range'