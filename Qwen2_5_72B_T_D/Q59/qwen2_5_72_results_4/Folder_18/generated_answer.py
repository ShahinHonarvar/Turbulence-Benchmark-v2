from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    primes = []
    for num in range(x - 1, 1, -1):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return primes