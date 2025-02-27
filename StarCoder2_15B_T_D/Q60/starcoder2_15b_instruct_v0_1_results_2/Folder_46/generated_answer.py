def all_left_right_truncatable_prime(tup):
    x = tup[33]
    truncatable_primes = []
    for prime in generate_primes(x):
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)