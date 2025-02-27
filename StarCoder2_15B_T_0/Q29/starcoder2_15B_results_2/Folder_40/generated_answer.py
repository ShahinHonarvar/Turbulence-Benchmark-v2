def gcf_two_nums(nums):
    if len(nums) < 10:
        raise ValueError('List must have at least 10 elements')
    if nums[7] < 1 or nums[9] < 1:
        raise ValueError('Both elements at indices 7 and 9 must be positive integers')
    gcf = 1
    for i in range(2, min(nums[7], nums[9]) + 1):
        if nums[7] % i == 0 and nums[9] % i == 0:
            gcf = i
    return gcf