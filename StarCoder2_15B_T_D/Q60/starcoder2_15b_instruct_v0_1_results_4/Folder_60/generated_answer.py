import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[87]
    result = []
    for n in range(2, x + 1):
        if is_prime(n):
            s = str(n)
            is_truncatable = True
            for i in range(len(s)):
                if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(n)
    result.sort()
    return result