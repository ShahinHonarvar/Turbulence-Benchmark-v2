def all_left_right_truncatable_prime(tup):
    x = tup[0]
    left_right_truncatable_primes = []
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)

def is_left_right_truncatable_prime(num):
    if num < 10:
        return False
    if not is_prime(num):
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