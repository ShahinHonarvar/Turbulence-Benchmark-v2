def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n:
        if not is_prime(n) or '0' in str(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(nums):
    x = nums[10]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)