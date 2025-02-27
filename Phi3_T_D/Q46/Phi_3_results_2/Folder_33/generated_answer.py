from math import gcd

def gcf_three_nums(nums):
    first_num = nums[252]
    second_num = nums[149]
    third_num = nums[564]
    return gcd(gcd(first_num, second_num), third_num)