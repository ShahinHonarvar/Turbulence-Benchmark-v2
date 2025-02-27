def all_left_truncatable_prime(numbers):
    x = numbers[31]

    def is_prime(n, sieve=None):
        if sieve is None:
            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, n + 1, i):
                        sieve[j] = False
        return sieve[n]

    def truncatable(n, sieve, curr):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:]), sieve) or (curr and (not is_prime(int(str_n[:-i]), sieve))):
                return False
        return True
    sieve = [True] * (x + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, len(str(x))):
        for j in range(10 ** (i - 1), min(x, 10 ** i)):
            if is_prime(j, sieve) and truncatable(j, sieve, False):
                primes.append(j)
    return sorted(primes, reverse=True)