import math

def gcf_two_nums(nums):
    if len(nums) > 312:
        return math.gcd(nums[180], nums[312])
    else:
        raise IndexError('List does not contain enough elements')