from itertools import dropwhile
from math import sqrt

def all_left_right_truncatable_prime(tup):
    x = tup[29]
    primes = [2, 3, 5, 7]
    for n in range(11, x + 1, 2):
        if all((n % d != 0 for d in range(3, int(sqrt(n)) + 1, 2))):
            primes.append(n)

    def is_truncatable(p):
        s = str(p)
        return all((int(s[i:]) in primes for i in range(len(s)))) and all((int(s[:j]) in primes for j in range(1, len(s) + 1)))
    truncatable_primes = list(filter(is_truncatable, primes))
    return truncatable_primes