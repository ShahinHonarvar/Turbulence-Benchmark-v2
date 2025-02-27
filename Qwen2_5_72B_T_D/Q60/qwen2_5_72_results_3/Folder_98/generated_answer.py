import itertools

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p] == True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime = []
    for p in range(2, n + 1):
        if is_prime[p]:
            prime.append(p)
    return prime

def all_left_right_truncatable_prime(numbers):
    index_8 = numbers[8]
    primes = sieve(index_8)
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        is_truncatable = True
        for i in range(1, len(str_prime)):
            if int(str_prime[i:]) not in primes or int(str_prime[:-i]) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)