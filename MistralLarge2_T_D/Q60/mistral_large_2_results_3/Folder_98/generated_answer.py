def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        str_n = str_n[1:-1]
        if not is_prime(int(str_n)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[8]
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and is_left_right_truncatable(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes