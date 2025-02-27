def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(len(str_n), 0, -1):
        if not is_prime(int(str_n[:i])):
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[945] if len(nums) > 945 else ''
    x = int(x)
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, primes)]
    return sorted(right_truncatable_primes, reverse=True)