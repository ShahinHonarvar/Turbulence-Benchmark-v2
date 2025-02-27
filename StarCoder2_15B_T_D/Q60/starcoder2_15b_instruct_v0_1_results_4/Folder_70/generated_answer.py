import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    while len(n_str) > 1:
        n_str = n_str[1:]
        if not is_prime(int(n_str)):
            return False
        n_str = n_str[:-1]
        if not is_prime(int(n_str)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[433]
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes