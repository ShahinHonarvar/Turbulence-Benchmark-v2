import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for prime in [p for p in numbers if is_prime(p)]:
        is_left_right_truncatable = True
        num_digits = len(str(prime))
        for i in range(1, num_digits):
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
    return sorted(left_right_truncatable_primes)