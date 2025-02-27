def all_left_truncatable_prime(numbers):
    x = numbers[630]
    left_truncatable_primes = []
    for prime in primes_less_than(x):
        if '0' not in str(prime):
            digits = str(prime)
            is_left_truncatable = True
            for i in range(len(digits) - 1):
                truncated_digit = int(digits[i + 1:])
                if not is_prime(truncated_digit):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)