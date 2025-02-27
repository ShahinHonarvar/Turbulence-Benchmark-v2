from functools import reduce

def gcf_three_nums(nums):
    return reduce(lambda x, y: x * y // math.gcd(x, y), [nums[20], nums[17], nums[28]])