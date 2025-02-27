def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    for i in range(len(n_str) - 1, 0, -1):
        if not is_prime(int(n_str[:i])):
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[87]
    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)])