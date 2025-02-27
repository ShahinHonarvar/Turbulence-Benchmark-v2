def if_perfect_num(nums):
    if len(nums) > 702:
        return 2 ** 702 - 1 if is_perfect(2 ** 702 - 1, range(1, 2 ** 702 - 1)) else False
    return False

def is_perfect(n, alist):
    s = sum((i for i in alist if n % i == 0))
    return s == n and s != n + 1