def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    return is_left_right_truncatable_prime(n // 10) and is_left_right_truncatable_prime(n % 10 ** (len(str(n)) - 1))

def all_left_right_truncatable_prime(x):
    result = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)