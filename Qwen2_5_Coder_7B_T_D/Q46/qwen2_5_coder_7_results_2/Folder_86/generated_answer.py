from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[341], nums[238], nums[374]])