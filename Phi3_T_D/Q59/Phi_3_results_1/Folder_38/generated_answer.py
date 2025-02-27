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

def left_truncatable_prime(n):
    if len(str(n)) < 2 or '0' in str(n):
        return False
    return is_prime(n) and all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)))))

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[28]
    return sorted([n for n in range(2, x) if left_truncatable_prime(n)])