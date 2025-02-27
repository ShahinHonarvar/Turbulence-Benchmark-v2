def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('The list must contain at least three elements.')
    gcf = nums[90]
    for i in range(91, 96):
        gcf = nums[i]
        for j in range(2, min(nums[i], gcf) + 1):
            if nums[i] % j == 0 and gcf % j == 0:
                gcf = j
    return gcf