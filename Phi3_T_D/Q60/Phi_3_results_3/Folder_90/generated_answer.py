def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, x):
    n_str = str(n)
    while n_str:
        if not is_prime(n):
            return False
        if int(n_str) > x:
            return False
        n_str = n_str[:-1]
        n //= 10
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[465]
    return sorted([p for p in range(2, x + 1) if is_truncatable(p, x)], reverse=True)