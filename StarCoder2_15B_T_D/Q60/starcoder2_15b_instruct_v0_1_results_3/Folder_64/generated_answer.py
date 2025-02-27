import math

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    if not isinstance(x, int) or x <= 0:
        return []
    primes = [True] * (x + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(math.sqrt(x)) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False
    left_right_truncatable_primes = [i for i in range(2, x + 1) if primes[i] and '0' not in str(i)]
    for i in range(len(left_right_truncatable_primes)):
        prime = left_right_truncatable_primes[i]
        while prime >= 10:
            prime //= 10
            if not primes[prime]:
                left_right_truncatable_primes[i] = None
                break
    return sorted([p for p in left_right_truncatable_primes if p is not None])