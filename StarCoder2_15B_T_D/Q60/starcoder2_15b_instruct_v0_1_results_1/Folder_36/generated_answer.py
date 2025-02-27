import re
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(data):
    x = data[992]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            left_right_truncatable = True
            temp = i
            while temp > 9:
                temp = int(str(temp)[1:])
                if not is_prime(temp):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes