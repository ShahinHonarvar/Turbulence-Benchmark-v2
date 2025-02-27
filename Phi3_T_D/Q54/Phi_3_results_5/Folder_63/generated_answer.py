def all_right_truncatable_prime(primes_tuple):
    x = primes_tuple[88]
    all_primes = set(primes_tuple)
    right_truncatable_primes = []
    for prime in all_primes:
        prime_str = str(prime)
        for i in range(len(prime_str)):
            truncated_prime = int(prime_str[:-1])
            if truncated_prime in all_primes:
                right_truncatable_primes.append(prime)
                break
    return sorted(list(set(right_truncatable_primes)))