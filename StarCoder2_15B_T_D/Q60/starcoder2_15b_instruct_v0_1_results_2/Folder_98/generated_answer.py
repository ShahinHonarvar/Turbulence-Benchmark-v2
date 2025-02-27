def all_left_right_truncatable_prime(tuple):
    x = tuple[8]
    left_right_truncatable_primes = [num for num in range(10, x + 1) if is_left_right_truncatable_prime(num)]
    left_right_truncatable_primes = sorted(left_right_truncatable_primes, reverse=True)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num >= 10:
        num = int(str(num)[1:])
        if not is_prime(num):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True