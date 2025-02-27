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

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(int(str(n)[:-1])):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[618]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])