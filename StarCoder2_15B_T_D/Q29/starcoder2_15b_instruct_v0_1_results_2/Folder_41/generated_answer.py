def gcf_two_nums(nums):
    assert isinstance(nums, list) and all((isinstance(n, int) and n > 0 for n in nums)), 'Invalid input'
    assert len(nums) >= 28, 'Not enough elements in the list'
    a = nums[23]
    b = nums[27]
    while b != 0:
        a, b = (b, a % b)
    return a