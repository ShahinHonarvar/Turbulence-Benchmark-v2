def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, base=10):
    while n > 0:
        if not is_prime(n):
            return False
        n = n % base ** (len(str(n)) - 1) * base + n // base ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[30]
    result = [p for p in range(x - 1, 1, -1) if is_left_truncatable_prime(p)]
    return result