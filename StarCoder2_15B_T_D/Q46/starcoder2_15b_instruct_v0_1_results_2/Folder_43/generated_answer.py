from functools import reduce

def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('The list must have at least 3 elements.')
    gcf = reduce(lambda x, y: x if x < y else y, (nums[33], nums[78], nums[93]))
    for i in range(2, gcf + 1):
        if nums[33] % i == nums[78] % i == nums[93] % i == 0:
            gcf = i
            break
    return gcf