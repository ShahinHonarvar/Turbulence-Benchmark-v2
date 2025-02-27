def prime_factors(numbers):

    def prime_factors_of(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if 8 < len(numbers):
        return prime_factors_of(numbers[8])
    else:
        return set()