def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(p):
    if not is_prime(p):
        return False
    str_p = str(p)
    return all((is_prime(int(str_p[i:])) and is_prime(int(str_p[:i + 1])) for i in range(len(str_p))))

def all_left_right_truncatable_prime(nums):
    x = nums[370]
    result = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return result[::-1]