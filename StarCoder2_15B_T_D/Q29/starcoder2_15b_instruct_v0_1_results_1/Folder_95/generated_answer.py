def gcf_two_nums(nums):
    """
    Returns the greatest common factor of the integers at indices 43 and 99.
    """
    if len(nums) < 100:
        raise ValueError('List must have at least 100 elements.')
    gcf = 1
    for i in range(2, min(nums[43], nums[99]) + 1):
        if nums[43] % i == 0 and nums[99] % i == 0:
            gcf = i
    return gcf