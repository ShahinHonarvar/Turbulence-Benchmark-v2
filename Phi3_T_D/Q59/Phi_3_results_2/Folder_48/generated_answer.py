def all_left_truncatable_prime(numbers):
    prime_list = [2, 3, 5, 7]
    primes_under_x = [p for p in range(2, numbers[835]) if all((p % n != 0 for n in range(2, int(p ** 0.5) + 1)))]
    truncatable_primes = []
    for prime in primes_under_x:
        prime_str = str(prime)
        for i in range(len(prime_str)):
            truncated_prime = int(prime_str[i:])
            if truncated_prime < prime and truncated_prime not in truncatable_primes and (truncated_prime in primes_under_x):
                truncatable_primes.append(truncated_prime)
    return sorted(truncatable_primes)