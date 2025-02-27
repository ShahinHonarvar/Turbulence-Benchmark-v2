from functools import reduce

def gcf_two_nums(nums):
    gcf = lambda a, b: a if b == 0 else gcf(b, a % b)
    return reduce(gcf, nums[618:619] + nums[195:196])