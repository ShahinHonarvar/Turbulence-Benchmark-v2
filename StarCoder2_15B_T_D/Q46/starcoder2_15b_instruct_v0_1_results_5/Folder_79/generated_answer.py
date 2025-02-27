def gcf_three_nums(nums):
    assert isinstance(nums, list) and all((isinstance(num, int) and num > 0 for num in nums)), 'The argument must be a list of positive integers.'
    assert len(nums) >= 96, 'The list must have at least 96 elements.'
    return gcd(nums[16], gcd(nums[87], nums[95]))

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a