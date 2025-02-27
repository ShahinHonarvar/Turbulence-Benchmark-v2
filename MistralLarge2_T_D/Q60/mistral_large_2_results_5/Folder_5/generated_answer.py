def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    if not is_prime(n):
        return False
    while len(s) > 1:
        s = s[1:-1]
        if not s or not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[55]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)