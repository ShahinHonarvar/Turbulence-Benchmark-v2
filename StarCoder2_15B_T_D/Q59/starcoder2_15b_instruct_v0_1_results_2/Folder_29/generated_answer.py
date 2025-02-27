def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    if is_prime(x):
        if x < 10:
            return [x]
        return [x] + all_left_truncatable_prime(x // 10)
    return []