def all_left_truncatable_prime(tup):
    x = tup[86]
    all_primes = [n for n in range(2, x) if all((n % d != 0 for d in range(2, n)))]
    left_truncatable_primes = []
    for prime in all_primes:
        is_left_truncatable = True
        truncated_prime = prime
        while truncated_prime >= 1:
            if truncated_prime not in all_primes:
                is_left_truncatable = False
                break
            truncated_prime = int(str(truncated_prime)[1:])
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)