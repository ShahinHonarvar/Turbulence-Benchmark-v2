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

def is_truncatable_prime(n, left=True):
    if not is_prime(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or (left and (not is_prime(int(s[:i])))):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i, right=False) and is_truncatable_prime(i, right=True)])