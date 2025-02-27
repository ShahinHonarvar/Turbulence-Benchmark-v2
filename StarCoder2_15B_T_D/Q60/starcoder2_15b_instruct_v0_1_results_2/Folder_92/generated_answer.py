def all_left_right_truncatable_prime(numbers):
    x = numbers[7]
    truncatable_primes = []
    for i in range(1, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes

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

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0:
        return False
    if not is_prime(n):
        return False
    return is_truncatable_prime(n // 10)