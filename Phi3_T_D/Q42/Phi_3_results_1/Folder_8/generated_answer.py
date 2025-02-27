import math

def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

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
    if len(lst) > 49:
        return factors(lst[49])
    else:
        raise ValueError('Index out of range. The list must have at least 50 elements.')