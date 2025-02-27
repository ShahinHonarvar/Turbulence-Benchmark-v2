import math

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def is_left_truncatable_prime(n, primes):
    if n in primes:
        if n < 10:
            return True
        else:
            return is_left_truncatable_prime(int(str(n)[1:]), primes)
    else:
        return False

def all_left_truncatable_prime(t):
    x = t[42]
    primes = sieve_of_eratosthenes(x)
    return sorted([p for p in primes if is_left_truncatable_prime(p, primes)])