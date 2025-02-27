def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    s = str(n)
    if '0' in s:
        return False
    if not all((is_prime(int(s[i:j + 1])) for i in range(len(s)) for j in range(i, len(s)))):
        return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[36]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)