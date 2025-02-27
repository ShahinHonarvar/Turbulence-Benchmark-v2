def all_right_truncatable_prime(input_tuple):
    x = input_tuple[30]

    def sieve_of_eratosthenes(n):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return [i for i in range(2, n + 1) if prime[i]]
    primes = sieve_of_eratosthenes(x)
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable_prime = True
        while prime >= x:
            prime //= 10
        if prime in primes:
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes