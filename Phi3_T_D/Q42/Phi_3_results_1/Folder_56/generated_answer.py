import math

def prime_factors(lst):

    def factors(n):
        primes = set()
        while n % 2 == 0:
            primes.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                primes.add(i)
                n //= i
        if n > 2:
            primes.add(n)
        return primes
    if len(lst) > 60:
        return factors(lst[60])
    else:
        return set()