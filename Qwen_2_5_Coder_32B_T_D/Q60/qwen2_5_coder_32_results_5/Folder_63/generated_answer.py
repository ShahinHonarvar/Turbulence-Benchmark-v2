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

def all_left_right_truncatable_prime(t):
    x = t[88]
    lr_truncatable_primes = []
    for num in range(23, x + 1):
        s = str(num)
        if '0' in s:
            continue
        is_lr_truncatable = True
        n = num
        while len(s) > 1:
            if not is_prime(n):
                is_lr_truncatable = False
                break
            s = s[1:-1]
            n = int(s)
        if is_lr_truncatable and is_prime(n):
            lr_truncatable_primes.append(num)
    return lr_truncatable_primes