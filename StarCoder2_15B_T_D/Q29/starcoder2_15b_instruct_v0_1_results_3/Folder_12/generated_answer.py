from functools import reduce

def gcf_two_nums(nums):
    return reduce(lambda a, b: a if a > b else b, [nums[56], nums[54]])