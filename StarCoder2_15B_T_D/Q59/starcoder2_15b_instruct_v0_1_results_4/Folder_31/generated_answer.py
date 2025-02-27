def all_left_truncatable_prime(numbers):
    numbers = numbers[:51]
    x = numbers[50]
    truncatable_primes = []
    for prime in numbers:
        if not is_left_truncatable_prime(prime, numbers):
            continue
        truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)

def is_left_truncatable_prime(prime, numbers):
    if not is_prime(prime):
        return False
    truncated_prime = prime // 10
    while truncated_prime > 0:
        if not is_prime(truncated_prime):
            return False
        if truncated_prime in numbers:
            return False
        truncated_prime //= 10
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True