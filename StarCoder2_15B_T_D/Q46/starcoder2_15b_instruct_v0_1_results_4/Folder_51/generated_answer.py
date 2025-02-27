from functools import reduce

def gcf_three_nums(nums):
    return reduce(lambda x, y: x * y // math.gcd(x, y), [nums[21], nums[69], nums[41]])