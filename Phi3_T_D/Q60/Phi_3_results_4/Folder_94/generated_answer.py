def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n, x):
    while n > 0:
        if not is_prime(n):
            return False
        if n > x:
            return False
        if n % 10 == 0:
            return False
        n = n // 10
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    result = []
    for n in range(2, x + 1):
        if is_left_right_truncatable(n, x):
            result.append(n)
    return result