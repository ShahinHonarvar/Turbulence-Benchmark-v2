def all_left_right_truncatable_prime(x):
    x = x[0]
    left_truncatable_primes = [p for p in range(2, x + 1) if all((int(str(p)[i:]) in prime_set for i in range(1, len(str(p)))))]
    right_truncatable_primes = [p for p in left_truncatable_primes if all((int(str(p)[:-i]) in prime_set for i in range(1, len(str(p)))))]
    return sorted(right_truncatable_primes, reverse=True)