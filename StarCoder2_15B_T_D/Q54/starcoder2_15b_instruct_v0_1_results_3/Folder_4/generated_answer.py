from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[96]
    right_truncatable_primes = []
    for i in range(1, len(str(x))):
        for permutation in permutations(str(x), i):
            num = int(''.join(permutation))
            if is_prime(num):
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes