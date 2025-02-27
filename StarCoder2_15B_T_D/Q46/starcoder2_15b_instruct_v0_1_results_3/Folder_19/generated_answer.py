from functools import reduce

def gcf_three_nums(nums):
    a, b, c = (nums[40], nums[15], nums[99])
    return reduce(lambda x, y: x * y // math.gcd(x, y), [a, b, c])