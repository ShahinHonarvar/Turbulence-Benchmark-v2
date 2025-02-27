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
    if n < 10:
        return True
    return is_left_truncatable(n % 10 ** len(str(n)) - 1)

def all_left_truncatable_prime(x):
    result = []
    for n in range(2, x):
        if is_left_truncatable(n):
            result.append(n)
    return sorted(result)