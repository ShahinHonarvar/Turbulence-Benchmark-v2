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
    str_n = str(n)
    if not str_n.startswith('1'):
        return all((is_prime(int(str_n[start:])) for start in range(len(str_n))))
    return False

def all_left_truncatable_prime(*args):
    x = args[50] if len(args) > 50 else max(args)
    result = [n for n in range(x, 1, -1) if left_truncatable_prime(n)]
    return result