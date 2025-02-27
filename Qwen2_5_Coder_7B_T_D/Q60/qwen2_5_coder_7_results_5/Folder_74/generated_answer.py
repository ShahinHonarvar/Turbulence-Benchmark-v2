import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[36]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        if all((is_prime(int(num_str[:i])) and is_prime(int(num_str[-i:])) for i in range(1, len(num_str)))):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)