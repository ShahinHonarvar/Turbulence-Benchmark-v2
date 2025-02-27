def all_left_right_truncatable_prime(numbers: tuple) -> list:
    x = numbers[784]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for i in range(1, len(str(prime))):
            truncated_left = int(str(prime)[i:])
            truncated_right = int(str(prime)[:-i])
            if not (is_prime(truncated_left) and is_prime(truncated_right)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort()
    return truncatable_primes