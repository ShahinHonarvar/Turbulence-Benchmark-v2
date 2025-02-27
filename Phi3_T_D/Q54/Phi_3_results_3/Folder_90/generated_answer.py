def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_primes(nums):
    x = nums[465]
    right_truncatables = [p for p in range(x, 1, -1) if is_right_truncatable(p)]
    return right_truncatables