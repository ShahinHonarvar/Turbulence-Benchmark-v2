from math import sqrt

def prime_factors(int_list):

    def get_prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    if len(int_list) > 34:
        return get_prime_factors(int_list[34])
    else:
        raise IndexError('The list does not contain 35 items.')