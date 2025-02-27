def all_left_right_truncatable_prime(x):
    if len(x) < 78:
        return []
    left_right_truncatable_primes = []
    for prime in x:
        truncatable = True
        for i in range(len(str(prime)) - 1):
            left_truncation = int(str(prime)[i + 1:])
            right_truncation = int(str(prime)[:len(str(prime)) - i - 1])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                truncatable = False
                break
        if truncatable:
            left_right_truncatable_primes.append(prime)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes