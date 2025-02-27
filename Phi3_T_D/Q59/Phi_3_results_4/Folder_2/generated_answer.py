def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n) or not is_prime(n):
        return False
    while n > 0:
        n = n % 10 ** (len(str(n)) - 1)
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[618]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])