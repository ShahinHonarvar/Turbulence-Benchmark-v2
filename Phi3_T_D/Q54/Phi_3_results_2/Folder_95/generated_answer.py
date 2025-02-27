def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    return is_prime(n) and all((is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1)))

def all_right_truncatable_prime(nums):
    n = nums[77]
    return sorted((p for p in range(2, n) if is_right_truncatable_prime(p)))