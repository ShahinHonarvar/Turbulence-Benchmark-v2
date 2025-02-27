import math

def gcf_three_nums(nums):
    assert all((isinstance(num, int) and num > 0 for num in nums)), 'nums must be a list of positive integers'
    assert len(nums) >= 81, 'nums must have at least 81 elements'
    return math.gcd(nums[31], math.gcd(nums[25], nums[80]))