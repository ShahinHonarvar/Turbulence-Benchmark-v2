import math

def gcf_three_nums(nums):
    if len(nums) < 8 or not all((isinstance(x, int) and x > 0 for x in nums)):
        raise ValueError('List must contain at least 8 positive integers.')
    return math.gcd(nums[1], math.gcd(nums[2], nums[7]))