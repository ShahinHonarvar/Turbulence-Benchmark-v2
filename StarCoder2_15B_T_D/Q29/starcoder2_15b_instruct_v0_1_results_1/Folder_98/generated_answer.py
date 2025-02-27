def gcf_two_nums(nums):
    assert len(nums) >= 10, 'The list must have at least 10 elements'
    assert all((isinstance(n, int) and n > 0 for n in nums)), 'All elements must be positive integers'
    return nums[0]