def all_left_right_truncatable_prime(tup):
    x = tup[89]
    truncatable_primes = []
    for i in range(1, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_truncatable_prime(num):
    if not is_prime(num) or contains_zero(num):
        return False
    while num >= 10:
        num = int(str(num)[1:])
        if not is_prime(num):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def contains_zero(num):
    return '0' in str(num)