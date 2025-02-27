def all_left_truncatable_prime(t):
    primes = [2]
    for i in range(3, t[630] + 1, 2):
        is_prime = all((i % x for x in primes if x * x <= i))
        if is_prime:
            primes.append(i)
    left_truncatable_primes = [p for p in primes if p > 10 and all((p % 10 ** i == p for i in range(len(str(p)) - 1))) and all((str(p)[i:] in map(str, primes) for i in range(1, len(str(p)))))]
    return sorted(left_truncatable_primes, reverse=True)