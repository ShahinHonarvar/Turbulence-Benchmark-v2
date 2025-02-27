import math

def all_right_truncatable_prime(tup):
    x = tup[618]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    right_truncatable_primes = []
    for p in primes:
        p_str = str(p)
        is_right_truncatable = True
        for i in range(len(p_str) - 1, 0, -1):
            if int(p_str[:i]) not in primes:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(p)
    right_truncatable_primes.sort()
    return right_truncatable_primes