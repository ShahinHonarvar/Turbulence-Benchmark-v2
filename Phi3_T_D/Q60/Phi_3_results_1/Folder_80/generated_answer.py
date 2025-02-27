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

def is_truncatable_prime(n, check_left=True, check_right=True):
    str_n = str(n)
    if not check_left and (not check_right):
        return False
    for i in range(1, len(str_n)):
        if not (check_left and is_prime(int(str_n[i:]))) or not (check_right and is_prime(int(str_n[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(integers):
    x = integers[14]
    trunc_primes = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i, check_left=True, check_right=True):
            trunc_primes.append(i)
    return trunc_primes