def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(p):
    while p > 0:
        if not is_prime(p):
            return False
        p //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    result = []
    for n in range(2, x):
        if right_truncatable_prime(n):
            result.append(n)
    return sorted(result)