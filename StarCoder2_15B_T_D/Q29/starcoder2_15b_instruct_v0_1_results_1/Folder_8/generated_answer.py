import functools

def gcf_two_nums(nums):
    return functools.reduce(lambda x, y: x if x > y else y, [nums[69], nums[41]])