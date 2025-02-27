def gcf_two_nums(nums):
    assert isinstance(nums, list), 'nums must be a list'
    assert len(nums) >= 2, 'nums must have at least two elements'
    assert all((isinstance(n, int) and n > 0 for n in nums)), 'nums must contain only positive integers'
    return nums[0] if nums[0] == nums[1] else 1