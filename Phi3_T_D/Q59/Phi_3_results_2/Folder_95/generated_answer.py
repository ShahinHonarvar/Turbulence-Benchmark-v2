def all_left_truncatable_prime(numbers):
    max_x = numbers[77]
    left_truncatable_primes = []
    primes = (n for n in range(2, max_x) if all((n % d != 0 for d in range(2, int(n ** 0.5) + 1))))
    for prime in primes:
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            truncated = int(prime_str[i:])
            if truncated == 0 or not all((truncated % d != 0 for d in range(2, int(truncated ** 0.5) + 1))):
                break
        else:
            left_truncatable_primes.append(prime)
    return left_truncatable_primes