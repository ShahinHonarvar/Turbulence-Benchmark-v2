import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    if 46 in x:
        right_truncatable_primes = [p for p in range(2, x[46]) if is_prime(p)]
        for i in range(len(str(x[46])) - 1, 0, -1):
            right_truncatable_primes = [p for p in right_truncatable_primes if is_prime(int(str(p)[:i]))]
        return sorted(right_truncatable_primes, reverse=True)
    else:
        return []