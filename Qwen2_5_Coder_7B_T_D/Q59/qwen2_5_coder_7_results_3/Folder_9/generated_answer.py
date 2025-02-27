def all_left_truncatable_prime(t):
    x = t[29]
    sieve = [True] * x
    sieve[0] = sieve[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    primes = [i for i in range(2, x) if sieve[i] and '0' not in str(i)]
    left_truncatable_primes = []
    for p in primes:
        str_p = str(p)
        while str_p:
            if not sieve[int(str_p)]:
                break
            str_p = str_p[1:]
        else:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)