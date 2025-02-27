def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    if n < 10:
        return True
    if n % 10 == 0:
        return False
    return is_left_right_truncatable(n // 10) and is_prime(n // 10)

def all_left_right_truncatable_prime(numbers):
    return [n for n in numbers if is_left_right_truncatable(n) and is_prime(n)]