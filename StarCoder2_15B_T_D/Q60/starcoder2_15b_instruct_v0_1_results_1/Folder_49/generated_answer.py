def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for i in range(1, len(str(prime))):
            truncated_number = int(str(prime)[i:])
            if truncated_number % 2 == 0 or truncated_number % 3 == 0 or truncated_number % 5 == 0 or (truncated_number % 7 == 0):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)