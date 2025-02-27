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

def is_truncatable_prime(n):
    str_n = str(n)
    if len(str_n) == 1:
        return not str_n.lstrip('0').isalpha()
    for i in range(len(str_n) - 1):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i - 1])):
            return False
    return not str_n.lstrip('0').isalpha()

def all_left_right_truncatable_prime(numbers):
    x = numbers[19]
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return truncatable_primes