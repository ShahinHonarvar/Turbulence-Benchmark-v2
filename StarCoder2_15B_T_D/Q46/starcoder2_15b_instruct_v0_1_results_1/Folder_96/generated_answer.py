import math

def gcf_three_nums(nums):
    assert isinstance(nums, list), 'nums must be a list'
    assert all((isinstance(num, int) and num > 0 for num in nums)), 'nums must be a list of positive integers'
    assert len(nums) >= 75, 'nums must have at least 75 elements'
    gcf = math.gcd(nums[29], nums[74])
    gcf = math.gcd(gcf, nums[49])
    return gcf