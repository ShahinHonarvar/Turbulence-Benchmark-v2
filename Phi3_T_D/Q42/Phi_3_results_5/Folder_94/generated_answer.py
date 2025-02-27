import math

def prime_factors(integers):

    def prime_factors_single(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    return prime_factors_single(integers[93]) if len(integers) > 93 else None