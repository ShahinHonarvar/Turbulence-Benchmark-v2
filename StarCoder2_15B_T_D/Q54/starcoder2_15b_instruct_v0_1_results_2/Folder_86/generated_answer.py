def all_right_truncatable_prime(tup):
    x = tup[126]
    right_truncatable_primes = [prime for prime in range(1, x) if is_right_truncatable_prime(prime)]
    return sorted(right_truncatable_primes, reverse=True) if right_truncatable_primes else []