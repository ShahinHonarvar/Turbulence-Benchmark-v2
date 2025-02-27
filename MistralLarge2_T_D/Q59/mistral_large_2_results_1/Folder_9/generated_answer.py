def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    while num > 0:
        if not is_prime(num) or '0' in str(num):
            return False
        num = int(str(num)[1:])
    return True

def all_left_truncatable_prime(t):
    x = t[29]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes, reverse=True)