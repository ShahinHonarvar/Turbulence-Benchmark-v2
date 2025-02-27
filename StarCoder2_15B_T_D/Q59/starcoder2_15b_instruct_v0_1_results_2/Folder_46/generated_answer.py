import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(arg):
    assert isinstance(arg, tuple) and all((isinstance(x, int) and x > 0 for x in arg)), 'Argument must be a tuple of positive integers'
    x = arg[33]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        temp = i
        while temp > 0:
            if not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)