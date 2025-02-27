def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for i in range(len(str(prime)) - 1):
            truncated_prime = int(str(prime)[i + 1:])
            if truncated_prime % 2 == 0 or truncated_prime % 5 == 0:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes