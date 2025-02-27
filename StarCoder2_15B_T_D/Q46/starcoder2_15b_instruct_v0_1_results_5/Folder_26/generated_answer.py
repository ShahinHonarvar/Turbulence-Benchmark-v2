from functools import reduce

def gcf_three_nums(nums):
    gcf = reduce(lambda x, y: x if x < y else y, [nums[15], nums[51], nums[76]])
    for i in range(2, gcf + 1):
        if nums[15] % i == 0 and nums[51] % i == 0 and (nums[76] % i == 0):
            gcf = i
    return gcf