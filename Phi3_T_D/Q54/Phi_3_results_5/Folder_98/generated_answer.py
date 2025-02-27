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

def is_right_truncatable_prime(n, x):
    return n < x and is_prime(n) and all((is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1)))

def all_right_truncatable_prime(t):
    x = t[8]
    return sorted([i for i in range(2, x, 2) if is_right_truncatable_prime(i, x)], reverse=True)