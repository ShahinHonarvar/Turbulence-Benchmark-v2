def all_left_right_truncatable_prime(x):
    primes = [2]
    for n in range(3, x + 1, 2):
        if all((n % d != 0 for d in range(3, int(n ** 0.5) + 1, 2))):
            primes.append(n)
    truncatable_primes = []
    for prime in primes:
        is_truncatable = True
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            left_trunc = int(prime_str[i:])
            right_trunc = int(prime_str[:i])
            if left_trunc not in primes or right_trunc not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes