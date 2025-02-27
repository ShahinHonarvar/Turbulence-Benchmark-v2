import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[30]
    right_truncatable_primes = []
    for n in range(x):
        is_right_truncatable = True
        for i in range(len(str(n)) - 1):
            truncated_number = int(str(n)[i:])
            if not is_prime(truncated_number):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)