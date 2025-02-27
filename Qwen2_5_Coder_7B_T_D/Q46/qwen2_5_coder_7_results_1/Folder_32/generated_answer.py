from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[20], nums[43], nums[95])
    while b:
        a, b = (b, a % b)
    return a