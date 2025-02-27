from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    res = []
    for num in nums:
        if not is_prime(num):
            continue
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:-i])):
                break
        else:
            res.append(num)
    res.sort()
    return res