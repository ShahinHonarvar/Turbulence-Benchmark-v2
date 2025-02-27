def prime_factors(numbers):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= divisor * divisor:
            if n % divisor:
                divisor += 1
            else:
                n //= divisor
                factors.add(divisor)
        if n > 1:
            factors.add(n)
        return factors
    return get_prime_factors(numbers[0])