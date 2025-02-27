def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[:-1]
    return True

def all_right_truncatable_prime(nums):
    x = nums[-1]
    right_truncatables = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatables.append(num)
    return sorted(right_truncatables)