def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for prime in numbers:
        if is_left_right_truncatable_prime(prime):
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)

def is_left_right_truncatable_prime(prime):
    if prime < 10:
        return is_prime(prime)
    if prime % 10 == 0:
        return False
    right_truncatable_prime = prime % 10
    left_truncatable_prime = prime // 10
    while left_truncatable_prime > 0:
        if not is_prime(left_truncatable_prime) or not is_prime(right_truncatable_prime):
            return False
        right_truncatable_prime = right_truncatable_prime * 10 + left_truncatable_prime % 10
        left_truncatable_prime //= 10
    return True

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True