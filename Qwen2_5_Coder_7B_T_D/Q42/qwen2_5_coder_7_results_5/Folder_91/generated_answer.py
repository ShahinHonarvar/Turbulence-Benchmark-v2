def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= divisor ** 2:
            if n % divisor:
                divisor += 1
            else:
                n //= divisor
                factors.add(divisor)
        factors.add(n)
        return factors
    return get_prime_factors(numbers[6])