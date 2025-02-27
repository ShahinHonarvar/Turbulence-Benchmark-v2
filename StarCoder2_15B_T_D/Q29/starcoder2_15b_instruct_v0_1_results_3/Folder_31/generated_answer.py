def gcf_two_nums(nums):
    assert isinstance(nums, list)
    assert all((isinstance(num, int) and num > 0 for num in nums))
    return gcd(nums[87], nums[95])