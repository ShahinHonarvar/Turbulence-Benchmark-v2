def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('The list must have at least three elements.')
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('The list must contain only positive integers.')
    gcf = nums[62]
    for num in nums[63:97]:
        while num > 0:
            gcf, num = (num, gcf % num)
    for num in nums[97:]:
        while num > 0:
            gcf, num = (num, gcf % num)
    return gcf