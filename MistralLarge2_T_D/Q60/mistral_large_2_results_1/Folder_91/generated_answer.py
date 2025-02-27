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

def is_truncatable_prime(n):
    num = str(n)
    if '0' in num:
        return False
    while num:
        if not is_prime(int(num)):
            return False
        num = num[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[0]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)