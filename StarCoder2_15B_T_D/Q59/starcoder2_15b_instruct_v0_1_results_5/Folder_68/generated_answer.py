def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    if x < 10:
        return []
    result = []
    if is_prime(x):
        result.append(x)
    result += all_left_truncatable_prime(int(str(x)[:-1]))
    return result