def all_left_right_truncatable_prime(numbers):
    x = numbers[18]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for digit in str(prime):
            if digit == '0':
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes