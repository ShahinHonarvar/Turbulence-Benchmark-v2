import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[14]
    right_truncatable_primes = []
    for i in range(2, x):
        number = i
        is_right_truncatable = True
        while number > 0:
            if not is_prime(number):
                is_right_truncatable = False
                break
            number //= 10
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)