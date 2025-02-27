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

def is_left_right_truncatable(n):
    s = str(n)
    if '0' in s:
        return False
    while s and is_prime(int(s)):
        s = s[1:-1]
    return len(s) <= 2 and is_prime(int(s))

def all_left_right_truncatable_prime(nums):
    x = nums[22]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)