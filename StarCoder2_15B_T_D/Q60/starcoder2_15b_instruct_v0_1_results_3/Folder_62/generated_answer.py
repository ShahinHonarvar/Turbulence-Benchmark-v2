def all_left_right_truncatable_prime(x):
    primes = [2]
    for i in range(3, x + 1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for prime in primes:
        if prime <= 10:
            continue
        left_truncatable = True
        right_truncatable = True
        num_digits = len(str(prime))
        for i in range(1, num_digits):
            left_digit = prime // 10 ** (num_digits - i)
            right_digit = prime % 10 ** (num_digits - i)
            if left_digit not in primes or right_digit not in primes:
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)