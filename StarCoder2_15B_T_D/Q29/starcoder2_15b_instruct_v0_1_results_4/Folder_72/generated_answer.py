def gcf_two_nums(nums):
    assert isinstance(nums, list), 'nums must be a list'
    assert len(nums) > 37, 'nums must have at least 38 elements'
    assert all((isinstance(n, int) and n > 0 for n in nums)), 'nums must contain only positive integers'
    gcf = nums[18]
    for n in nums[19:38]:
        while n != 0:
            gcf, n = (n, gcf % n)
    return gcf