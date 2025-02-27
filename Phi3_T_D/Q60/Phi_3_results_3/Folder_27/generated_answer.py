def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[79]
    result = [i for i in range(x, 1, -1) if is_truncatable_prime(i)]
    return result