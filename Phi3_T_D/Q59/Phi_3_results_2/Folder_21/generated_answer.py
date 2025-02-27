def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[175]
    left_truncatable_primes = []
    for prime in range(2, x):
        original = prime
        is_truncatable = True
        while original > 0:
            if not is_prime(original):
                is_truncatable = False
                break
            original //= 10
        if is_truncatable:
            left_truncatable_primes.append(prime)
    return left_truncatable_primes