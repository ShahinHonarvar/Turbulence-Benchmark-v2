def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 1:
        s = s[1:]
        if not is_prime(int(s)):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[22]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes, reverse=True)