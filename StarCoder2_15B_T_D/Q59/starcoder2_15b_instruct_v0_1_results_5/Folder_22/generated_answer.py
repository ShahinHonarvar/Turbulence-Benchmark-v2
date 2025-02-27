def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for num in range(1, x):
        if is_prime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True