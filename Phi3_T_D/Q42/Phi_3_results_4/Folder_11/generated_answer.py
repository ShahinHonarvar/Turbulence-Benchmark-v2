import math

def prime_factors(list_of_ints):

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

    def get_prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n //= i
        if n > 2:
            if is_prime(n):
                factors.add(n)
        return factors
    return get_prime_factors(list_of_ints[77]) if len(list_of_ints) > 77 else set()