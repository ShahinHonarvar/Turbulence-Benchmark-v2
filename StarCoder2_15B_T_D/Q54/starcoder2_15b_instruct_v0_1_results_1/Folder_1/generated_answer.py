def all_right_truncatable_prime(tup):
    x = tup[20]

    def sieve_of_eratosthenes(n):
        primes = [True for i in range(n + 1)]
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]
    prime_list = sieve_of_eratosthenes(x)
    right_truncatable_primes = [p for p in prime_list if all((int(str(p)[i:]) in prime_list for i in range(1, len(str(p)))))]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes