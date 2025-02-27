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

def is_left_truncatable_prime(m, s):
    while m:
        if not m % 10 or not is_prime(m):
            return False
        m //= 10
    return True

def all_left_truncatable_prime(tpl):
    x = tpl[10]
    result = [i for i in range(7, x) if is_left_truncatable_prime(i, str(i))]
    return sorted(result, reverse=True)