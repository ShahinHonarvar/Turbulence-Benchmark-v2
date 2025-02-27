def all_left_truncatable_prime(t):
    x = t[466]
    return sorted(list(sieve_of_eratosthenes(x)), reverse=True)

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n + 1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]