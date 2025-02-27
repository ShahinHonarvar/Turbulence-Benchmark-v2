def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[945]
    left_truncatables = [n for n in range(2, x) if is_left_truncatable(n)]
    return left_truncatables[::-1]