from functools import reduce

def gcf_three_nums(nums):
    return reduce(lambda x, y: x * y // gcd(x, y), [nums[252], nums[149], nums[564]])

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a