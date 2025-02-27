def all_left_truncatable_prime(x):
    x = x[0]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, i)))]
    left_truncatable_primes = [p for p in primes if all((int(str(p)[i:]) in primes for i in range(len(str(p)))))]
    return sorted(left_truncatable_primes, reverse=True)