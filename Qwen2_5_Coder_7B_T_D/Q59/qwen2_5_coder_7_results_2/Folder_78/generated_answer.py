def all_left_truncatable_prime(t):
    x = t[23]
    limit = x
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    primes = [i for i in range(2, limit) if sieve[i] and '0' not in str(i)]
    left_truncatable_primes = []
    for p in primes:
        str_p = str(p)
        is_left_truncatable = True
        for i in range(len(str_p)):
            if not sieve[int(str_p[i:])]:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes)