from functools import reduce

def gcf_three_nums(nums):
    return reduce(lambda x, y: x if x < y else y, [nums[1], nums[2], nums[7]])