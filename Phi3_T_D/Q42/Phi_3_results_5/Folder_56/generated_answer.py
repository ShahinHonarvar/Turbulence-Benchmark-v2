from collections import Counter

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

    def prime_factors_of(n):
        factors = []
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1 if i == 2 else 2
        if n > 1:
            factors.append(n)
        return factors
    factors_lst = prime_factors_of(lst[60])
    return set(factors_lst)