def prime_factors(numbers):

    def prime_factors_of(n):
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
    if len(numbers) > 21:
        return prime_factors_of(numbers[21])
    else:
        return set()