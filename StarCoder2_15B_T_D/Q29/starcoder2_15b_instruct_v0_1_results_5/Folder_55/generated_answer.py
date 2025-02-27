import math

def gcf_two_nums(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) and n > 0 for n in nums)):
        raise ValueError('Invalid input: expecting a list of positive integers')
    if len(nums) < 3:
        raise ValueError('Invalid input: expecting a list with at least 3 elements')
    return math.gcd(nums[2], nums[1])