def all_left_truncatable_prime(x):
    return [p for p in range(2, x) if all((int(str(p)[i:]) in prime_sieve for i in range(1, len(str(p)))))]