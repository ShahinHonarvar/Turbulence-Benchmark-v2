def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_primes(numbers):
    x = numbers[630]
    right_truncatable = []
    for prime in range(2, x):
        original = prime
        while original > 0:
            if not is_prime(original):
                break
            original //= 10
        if original == 0:
            right_truncatable.append(prime)
    return sorted(right_truncatable, reverse=True)