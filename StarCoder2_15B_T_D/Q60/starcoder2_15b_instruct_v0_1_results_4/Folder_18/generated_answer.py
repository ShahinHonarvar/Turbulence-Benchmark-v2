def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for prime in numbers:
        if prime < 10:
            continue
        is_left_right_truncatable = True
        for i in range(1, len(str(prime))):
            truncated_prime = int(str(prime)[i:])
            if not is_prime(truncated_prime):
                is_left_right_truncatable = False
                break
            truncated_prime = int(str(prime)[:-i])
            if not is_prime(truncated_prime):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True