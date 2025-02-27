def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n, primes):
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[:-1]
    return True

def all_right_truncatable_prime(numbers):
    if not isinstance(numbers, tuple) or len(numbers) != 71:
        return []
    limit = numbers[70]
    return sorted([int(n) for n in range(2, limit) if right_truncatable_prime(n, [])])