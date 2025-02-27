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

def is_right_truncatable_prime(p):
    if not is_prime(p):
        return False
    primes = [2, 3, 5, 7]
    temp = p
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    return True

def all_right_truncatable_prime(nums):
    x = nums[74]
    return sorted([p for p in range(2, x) if is_right_truncatable_prime(p)])