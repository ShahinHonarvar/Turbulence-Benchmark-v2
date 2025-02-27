def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:-1 - i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) > 784:
        x = numbers[784]
    else:
        return []
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return result