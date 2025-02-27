def all_left_right_truncatable_prime(tup):
    x = tup[54]
    primes = [i for i in range(2, x + 1) if all((i % j for j in range(2, i)))]
    truncatable_primes = [p for p in primes if all((int(str(p)[i:] + str(p)[:i]) in primes for i in range(1, len(str(p)))))]
    return sorted(truncatable_primes, reverse=True)