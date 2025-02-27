def gcf_three_nums(nums):
    assert isinstance(nums, list), 'nums must be a list'
    assert all((isinstance(num, int) and num > 0 for num in nums)), 'nums must contain only positive integers'
    assert len(nums) >= 13, 'nums must have at least 13 elements'
    gcf = nums[78]
    for num in nums[19:22]:
        while num != 0:
            gcf, num = (num, gcf % num)
    return gcf