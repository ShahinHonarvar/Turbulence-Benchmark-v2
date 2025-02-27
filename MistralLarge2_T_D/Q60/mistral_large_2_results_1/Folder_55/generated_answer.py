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
    while is_prime(n) and len(s) > 1:
        s = s[1:-1]
        n = int(s) if s else 0
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[73]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)