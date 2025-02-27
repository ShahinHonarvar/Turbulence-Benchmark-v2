def all_left_right_truncatable_prime(x):
    primes = [n for n in range(2, x + 1) if all((n % i != 0 for i in range(2, n)))]
    left_right_truncatable_primes = []
    for prime in primes:
        is_left_right_truncatable = True
        truncated_prime = prime
        while len(str(truncated_prime)) >= 2:
            truncated_prime = int(str(truncated_prime)[1:])
            if truncated_prime not in primes:
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)