def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n != 1:
            while n % divisor == 0:
                factors.add(divisor)
                n = n // divisor
            divisor += 1
        return factors
    return get_prime_factors(lst[83])