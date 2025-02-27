def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, left_to_right=True):
    if '0' in str(n):
        return False
    if left_to_right:
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
    else:
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
    return True

def get_all_truncatable_primes(x):
    truncatable_primes = [p for p in range(2, x + 1) if is_truncatable_prime(p) and is_truncatable_prime(p, False)]
    return sorted(truncatable_primes)

def all_left_right_truncatable_prime(nums):
    x = nums[835]
    return get_all_truncatable_primes(x)