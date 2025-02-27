import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[31]
    right_truncatable_primes = []
    for i in range(2, x):
        number = i
        while number > 0:
            if not is_prime(number):
                break
            number //= 10
        if number == 0:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)