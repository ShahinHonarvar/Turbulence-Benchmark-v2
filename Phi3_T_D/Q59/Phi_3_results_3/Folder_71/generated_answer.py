def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, primes):
    str_n = str(n)
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(nums):
    x = nums[22]
    truncatable_primes = [p for p in range(7, x, 2) if is_prime(p)]
    return sorted([p for p in truncatable_primes if is_left_truncatable(p, truncatable_primes)], reverse=True)