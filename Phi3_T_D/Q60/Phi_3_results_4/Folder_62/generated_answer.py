def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, left_trunc=True):
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) for i in range(1 if left_trunc else 0, len(str_n))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    result = []
    for num in range(2, x + 1):
        if is_truncatable(num, left_trunc=True) and is_truncatable(num, left_trunc=False):
            result.append(num)
    return result