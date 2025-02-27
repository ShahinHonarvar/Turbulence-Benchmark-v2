def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 14 or not isinstance(numbers[14], int):
        raise ValueError('Argument should be a tuple of at least 15 positive integers.')
    x = numbers[14]
    right_truncatable_primes = [i for i in range(7, x) if i % 2 != 0 and i % 5 != 0 and is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)