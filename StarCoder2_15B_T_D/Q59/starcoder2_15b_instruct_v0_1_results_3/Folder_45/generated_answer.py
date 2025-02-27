def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[61]

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
    left_truncatable_primes = [p for p in prime_list if '0' not in str(p) and all((int(str(p)[i:]) in prime_list for i in range(1, len(str(p)))))]
    return sorted(left_truncatable_primes)