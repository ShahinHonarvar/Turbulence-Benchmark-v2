def is_right_truncatable_prime(n, primes_set):
    while n > 0:
        if n not in primes_set:
            return False
        n //= 10
    return True

def find_primes_sieve(limit):
    sieve = [True] * (limit + 1)
    primes = []
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes

def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[784]
    primes = find_primes_sieve(x)
    right_truncatable_primes = [p for p in primes if all(map(lambda prime: prime in primes, map('{:d}'.format, map(int, reversed(str(p))))))]
    return sorted(right_truncatable_primes)