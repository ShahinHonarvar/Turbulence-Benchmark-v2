def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:-i])):
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[55]
    result = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            result.append(i)
    return result