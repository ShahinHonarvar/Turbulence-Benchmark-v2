def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def left_truncatable_prime(x: int) -> bool:
    if not is_prime(x):
        return False
    while x > 0:
        if not is_prime(x):
            return False
        x //= 10
    return True

def all_left_truncatable_prime(x: tuple) -> list:
    x = x[6]
    result = []
    for i in range(2, x):
        if left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result