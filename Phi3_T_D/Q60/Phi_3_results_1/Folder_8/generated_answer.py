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

def is_truncatable_prime(n, checked=set(), trunc_from_left=True):
    if n in checked:
        return True
    if not n or not is_prime(n):
        return False
    if trunc_from_left:
        return is_truncatable_prime(n[1:], checked | {n}, False)
    else:
        return is_truncatable_prime(n[:-1], checked | {n}, True)

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(str(n))], reverse=True)