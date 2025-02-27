import math

def all_right_truncatable_prime(t):
    x = t[42]
    primes = [2, 3, 5, 7]
    result = []
    for prime in primes:
        if prime >= x:
            break
        if str(prime)[-1] in '024568':
            continue
        while prime >= x:
            prime //= 10
        if prime in primes:
            result.append(prime)
    return sorted(result)