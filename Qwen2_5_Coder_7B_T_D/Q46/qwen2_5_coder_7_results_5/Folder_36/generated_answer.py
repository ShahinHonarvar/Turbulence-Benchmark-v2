from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(lambda x, y: gcd(x, y), [nums[427], nums[761], nums[148]])