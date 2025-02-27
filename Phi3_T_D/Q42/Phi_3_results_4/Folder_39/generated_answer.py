import math

def prime_factors(numbers):

    def prime_factorize(n):
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
    if len(numbers) > 59:
        return prime_factorize(numbers[59])
    else:
        return set()