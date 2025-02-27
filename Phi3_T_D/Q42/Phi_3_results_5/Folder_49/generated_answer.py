from collections import Counter
from itertools import chain

def prime_factors(lst):

    def factors(n):
        return set(chain.from_iterable(((div, n // div) for i in range(1, int(n ** 0.5) + 1) if n % i == 0 for div in (i, n // i))))

    def is_prime(n):
        return n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))
    six_eight_factors = factors(lst[68])
    prime_factors = {factor for factor in six_eight_factors if is_prime(factor)}
    return prime_factors