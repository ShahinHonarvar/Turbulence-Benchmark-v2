def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[10]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes