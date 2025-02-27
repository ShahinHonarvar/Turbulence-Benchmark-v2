def all_left_truncatable_prime(t):
    x = t[78]
    primes = set(range(2, x))
    for i in range(2, int(x ** 0.5) + 1):
        primes -= set(range(i * i, x, i))
    left_trunc_primes = []
    for prime in primes:
        if '0' not in str(prime):
            while prime > 0:
                if prime not in primes:
                    break
                prime //= 10
            else:
                left_trunc_primes.append(prime)
    return sorted(left_trunc_primes, reverse=True)