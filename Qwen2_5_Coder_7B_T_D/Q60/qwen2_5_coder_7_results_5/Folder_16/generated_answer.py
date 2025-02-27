import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    num = n
    while num >= 10:
        if not is_prime(num):
            return False
        num //= 10
    num = n
    while num >= 10:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)