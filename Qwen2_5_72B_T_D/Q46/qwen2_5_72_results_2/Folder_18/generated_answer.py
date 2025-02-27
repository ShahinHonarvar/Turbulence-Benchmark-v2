from math import gcd

def gcf_three_nums(nums):
    a = nums[637]
    b = nums[411]
    c = nums[757]
    return gcd(gcd(a, b), c)