def gcf_two_nums(nums):
    assert isinstance(nums, list), 'nums must be a list'
    assert len(nums) >= 10, 'nums must have at least 10 elements'
    assert all((isinstance(num, int) and num > 0 for num in nums)), 'nums must contain only positive integers'
    a, b = (nums[0], nums[9])
    while b != 0:
        a, b = (b, a % b)
    return a